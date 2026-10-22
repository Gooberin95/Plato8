"""Interactive state for search, servings, step ticks, and the kitchen timer."""

import asyncio

import reflex as rx

from clementine.data import (
    RECIPE_BY_SLUG,
    bar_width,
    build_ingredients,
    build_steps,
    clock_text,
    filter_recipes,
    recipe_view_dict,
    scale_sentence,
    steps_sentence,
    timer_chip_rows,
)

MAX_PORTIONS = 60


class KitchenState(rx.State):
    """One cook's session: filters, the open card, and a running timer."""

    query: str = ""
    show_vegetarian: bool = False
    show_quick: bool = False
    show_dessert: bool = False

    current_slug: str = ""
    servings: int = 4
    checked: list[bool] = []
    recipe_tab: str = "ingredients"

    minute_draft: str = "10"
    timer_total: int = 10 * 60
    timer_remaining: int = 10 * 60
    timer_running: bool = False
    timer_done: bool = False
    _timer_token: int = 0

    @rx.event
    def set_query(self, value: str):
        self.query = value

    @rx.event
    def set_minute_draft(self, value: str):
        self.minute_draft = value

    @rx.event
    def toggle_vegetarian(self):
        self.show_vegetarian = not self.show_vegetarian

    @rx.event
    def toggle_quick(self):
        self.show_quick = not self.show_quick

    @rx.event
    def toggle_dessert(self):
        self.show_dessert = not self.show_dessert

    @rx.event
    def clear_filters(self):
        self.query = ""
        self.show_vegetarian = False
        self.show_quick = False
        self.show_dessert = False

    @rx.event
    def go_tab(self, value: str):
        destinations = {
            "home": "/",
            "recipes": "/recipes",
            "about": "/about",
        }
        return rx.redirect(destinations.get(str(value), "/"))

    @rx.event
    def select_recipe_tab(self, value: str):
        self.recipe_tab = str(value)

    @rx.var
    def nav_tab(self) -> str:
        path = (self.router.url.path or "/").rstrip("/") or "/"
        if path.startswith("/recipe"):
            return "recipes"
        if path.startswith("/about"):
            return "about"
        if path.startswith("/recipes"):
            return "recipes"
        return "home"

    @rx.var
    def filtered_recipes(self) -> list[dict[str, str]]:
        return filter_recipes(
            self.query, self.show_vegetarian, self.show_quick, self.show_dessert
        )

    @rx.var
    def match_count(self) -> int:
        return len(
            filter_recipes(
                self.query, self.show_vegetarian, self.show_quick, self.show_dessert
            )
        )

    @rx.var
    def match_label(self) -> str:
        count = len(
            filter_recipes(
                self.query, self.show_vegetarian, self.show_quick, self.show_dessert
            )
        )
        noun = "recipe" if count == 1 else "recipes"
        return f"{count} {noun}"

    @rx.var
    def filters_on(self) -> bool:
        return bool(
            self.query.strip()
            or self.show_vegetarian
            or self.show_quick
            or self.show_dessert
        )

    @rx.var
    def query_blank(self) -> bool:
        return self.query.strip() == ""

    @rx.var
    def recipe_loading(self) -> bool:
        return self.current_slug == ""

    @rx.var
    def recipe_found(self) -> bool:
        return self.current_slug in RECIPE_BY_SLUG

    @rx.var
    def recipe_view(self) -> dict[str, str]:
        return recipe_view_dict(self.current_slug)

    @rx.var
    def ingredient_rows(self) -> list[dict[str, str]]:
        return build_ingredients(self.current_slug, self.servings)

    @rx.var
    def step_rows(self) -> list[dict[str, str]]:
        return build_steps(self.current_slug, self.checked)

    @rx.var
    def scale_note(self) -> str:
        return scale_sentence(self.current_slug, self.servings)

    @rx.var
    def steps_label(self) -> str:
        return steps_sentence(self.checked)

    @rx.var
    def timer_chips(self) -> list[dict[str, str]]:
        return timer_chip_rows(self.current_slug)

    @rx.var
    def timer_clock(self) -> str:
        return clock_text(self.timer_remaining)

    @rx.var
    def timer_bar_width(self) -> str:
        return bar_width(self.timer_total, self.timer_remaining)

    @rx.var
    def at_min_servings(self) -> bool:
        return self.servings <= 1

    @rx.var
    def at_max_servings(self) -> bool:
        return self.servings >= MAX_PORTIONS

    def _route_slug(self) -> str:
        path = str(self.router.url.path or "")
        marker = "/recipe/"
        if marker not in path:
            return ""
        return path.split(marker, 1)[1].strip("/")

    def _set_minutes(self, minutes: int) -> None:
        minutes = max(1, min(180, int(minutes)))
        self.timer_running = False
        self.timer_done = False
        self._timer_token += 1
        self.timer_total = minutes * 60
        self.timer_remaining = self.timer_total
        self.minute_draft = str(minutes)

    @rx.event
    def load_recipe(self):
        slug = self._route_slug()
        self.current_slug = slug
        self.recipe_tab = "ingredients"
        recipe = RECIPE_BY_SLUG.get(slug)
        if recipe is None:
            self.checked = []
            return
        self.servings = int(recipe["servings"])
        self.checked = [False] * len(recipe["steps"])
        if not self.timer_running:
            self._set_minutes(int(recipe["timer_presets"][0]))

    @rx.event
    def bump_servings(self, delta: int):
        try:
            step = int(delta)
        except (TypeError, ValueError):
            return
        self.servings = min(MAX_PORTIONS, max(1, self.servings + step))

    @rx.event
    def reset_servings(self):
        recipe = RECIPE_BY_SLUG.get(self.current_slug)
        if recipe is not None:
            self.servings = int(recipe["servings"])

    @rx.event
    def toggle_step(self, index: str, value: bool):
        try:
            position = int(index)
        except (TypeError, ValueError):
            return
        if isinstance(value, str):
            value = value.lower() in {"true", "1", "on", "yes"}
        checked = list(self.checked)
        if position < 0 or position >= len(checked):
            return
        checked[position] = bool(value)
        self.checked = checked

    @rx.event
    def reset_checks(self):
        recipe = RECIPE_BY_SLUG.get(self.current_slug)
        count = len(recipe["steps"]) if recipe else 0
        self.checked = [False] * count

    @rx.event
    def set_minutes(self, minutes: str):
        digits = "".join(character for character in str(minutes) if character.isdigit())
        if not digits:
            return
        self._set_minutes(int(digits))

    @rx.event
    def apply_minute_draft(self):
        digits = "".join(character for character in self.minute_draft if character.isdigit())
        if not digits:
            return
        self._set_minutes(int(digits))

    @rx.event
    def start_timer(self):
        if self.timer_remaining <= 0:
            self.timer_remaining = self.timer_total or 60
            self.timer_total = max(self.timer_total, self.timer_remaining)
        self.timer_done = False
        self.timer_running = True
        self._timer_token += 1
        return KitchenState.tick

    @rx.event
    def pause_timer(self):
        self.timer_running = False
        self._timer_token += 1

    @rx.event
    def reset_timer(self):
        self.timer_running = False
        self.timer_done = False
        self._timer_token += 1
        self.timer_remaining = self.timer_total or 60

    @rx.event(background=True)
    async def tick(self):
        async with self:
            token = self._timer_token
        while True:
            await asyncio.sleep(1)
            async with self:
                if token != self._timer_token or not self.timer_running:
                    return
                if self.timer_remaining <= 1:
                    self.timer_remaining = 0
                    self.timer_running = False
                    self.timer_done = True
                    return
                self.timer_remaining -= 1
