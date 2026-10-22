"""Shared chrome, cards, and the fixed painting canvas."""

import reflex as rx

from clementine.data import RECIPES
from clementine.state import KitchenState


def tag_pill(label: str, kind: str) -> rx.Component:
    return rx.box(label, class_name=f"pill pill-{kind}")


def live_pills(info) -> rx.Component:
    return rx.box(
        rx.cond(info["vegetarian"] == "yes", tag_pill("Vegetarian", "veg"), rx.fragment()),
        rx.cond(info["quick"] == "yes", tag_pill("Quick", "quick"), rx.fragment()),
        rx.cond(info["dessert"] == "yes", tag_pill("Dessert", "dessert"), rx.fragment()),
        class_name="pill-row",
    )


def static_pills(recipe: dict) -> rx.Component:
    tags = recipe["tags"]
    pills = []
    if "vegetarian" in tags:
        pills.append(tag_pill("Vegetarian", "veg"))
    if "quick" in tags:
        pills.append(tag_pill("Quick", "quick"))
    if "dessert" in tags:
        pills.append(tag_pill("Dessert", "dessert"))
    return rx.box(*pills, class_name="pill-row")


def card_body(emoji, title, blurb, time, servings_label, difficulty, pills) -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(emoji, class_name="emoji"),
            rx.box(time, class_name="pill pill-plain"),
            class_name="card-top",
        ),
        rx.heading(title, as_="h3", class_name="card-title"),
        rx.text(blurb, class_name="muted"),
        pills,
        rx.box(
            rx.text(difficulty, class_name="pill pill-plain"),
            rx.text(servings_label, class_name="pill pill-plain"),
            class_name="pill-row",
        ),
        class_name="card",
    )


def static_card(recipe: dict) -> rx.Component:
    return rx.link(
        card_body(
            recipe["emoji"],
            recipe["title"],
            recipe["blurb"],
            recipe["time_label"],
            f"{recipe['servings']} {recipe['portion']}",
            recipe["difficulty"],
            static_pills(recipe),
        ),
        href=f"/recipe/{recipe['slug']}",
        class_name="card-link",
    )


def live_card(info) -> rx.Component:
    return rx.link(
        card_body(
            info["emoji"],
            info["title"],
            info["blurb"],
            info["time"],
            info["servings_label"],
            info["difficulty"],
            live_pills(info),
        ),
        href="/recipe/" + info["slug"],
        class_name="card-link",
    )


def filter_chip(label: str, active, handler, on_color: str) -> rx.Component:
    return rx.button(
        label,
        on_click=handler,
        class_name="chip",
        background_color=rx.cond(active, on_color, "rgba(255,246,234,0.06)"),
        color=rx.cond(active, "#241408", "#FFF6EA"),
        border=rx.cond(
            active,
            "1px solid transparent",
            "1px solid rgba(255,196,140,0.35)",
        ),
    )


def site_nav() -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger(
                "Home",
                value="home",
                on_click=rx.redirect("/"),
                class_name="site-tab",
            ),
            rx.tabs.trigger(
                "Recipes",
                value="recipes",
                on_click=rx.redirect("/recipes"),
                class_name="site-tab",
            ),
            rx.tabs.trigger(
                "About",
                value="about",
                on_click=rx.redirect("/about"),
                class_name="site-tab",
            ),
            class_name="site-tablist",
        ),
        value=KitchenState.nav_tab,
        on_change=KitchenState.go_tab,
    )


def site_header() -> rx.Component:
    return rx.box(
        rx.box(
            rx.link(
                rx.box(
                    rx.box("C", class_name="mark"),
                    rx.box(
                        rx.text("Clementine's Skillet", class_name="wordmark"),
                        rx.text("Savannah apartment kitchen", class_name="wordmark-sub"),
                        class_name="stack tight",
                    ),
                    class_name="brand",
                ),
                href="/",
                class_name="wordmark-link",
            ),
            site_nav(),
            class_name="topbar",
        ),
        class_name="header",
    )


def site_footer() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text("Clementine Brooks · Savannah"),
            rx.text("Tick the card. Trust the timer."),
            class_name="footer-inner",
        ),
        class_name="footer",
    )


def shell(*children) -> rx.Component:
    """Page root. The painting is applied once here and stays fixed while the page scrolls."""
    return rx.box(
        site_header(),
        rx.box(*children, class_name="page"),
        site_footer(),
        background_image="url('/background.jpg')",
        background_size="cover",
        background_position="center",
        background_attachment="fixed",
        background_color="#070b16",
        class_name="canvas",
        min_height="100vh",
        width="100%",
    )


def home_page() -> rx.Component:
    featured = RECIPES[0]
    return shell(
        rx.box(
            rx.box(
                rx.box(
                    rx.text("Weeknight cards", class_name="kicker"),
                    rx.heading("Clementine's Skillet", as_="h1", class_name="display hero-title"),
                    rx.text(
                        "Eight-and-a-bit recipes she actually makes on a Tuesday, written like the stained index cards on her fridge.",
                        class_name="lede",
                    ),
                    rx.text(
                        "If it needs a stand mixer, it doesn't live here.",
                        class_name="quote",
                    ),
                    rx.box(
                        rx.link(
                            "Open the recipe box",
                            href="/recipes",
                            class_name="btn-link",
                        ),
                        rx.link(
                            "Meet Clementine",
                            href="/about",
                            class_name="btn-link ghost",
                        ),
                        class_name="button-row",
                    ),
                    class_name="stack",
                ),
                static_card(featured),
                class_name="split",
            ),
            class_name="panel",
        ),
        rx.box(
            rx.box(
                rx.text("01", class_name="kicker"),
                rx.heading("Turn the servings knob", as_="h2", class_name="display"),
                rx.text(
                    "Every amount on the card is a number. Change the servings and the butter, the jam, and the peaches multiply with you.",
                    class_name="muted",
                ),
                class_name="panel stack",
            ),
            rx.box(
                rx.text("02", class_name="kicker"),
                rx.heading("Tick the steps", as_="h2", class_name="display"),
                rx.text(
                    "Check a step off when the garlic smells sweet. The card remembers, so a phone call doesn't send you back to the top.",
                    class_name="muted",
                ),
                class_name="panel stack",
            ),
            rx.box(
                rx.text("03", class_name="kicker"),
                rx.heading("Start the timer", as_="h2", class_name="display"),
                rx.text(
                    "Each recipe keeps the minutes she actually uses. Hit 6 for the peaches, 28 for the cake, or type your own.",
                    class_name="muted",
                ),
                class_name="panel stack",
            ),
            class_name="trio",
        ),
        rx.box(
            rx.box(
                rx.text("From the box", class_name="kicker"),
                rx.heading("Cook one of these next", as_="h2", class_name="display"),
                class_name="stack tight",
            ),
            rx.box(
                *[static_card(recipe) for recipe in RECIPES[1:]],
                class_name="card-grid",
            ),
            class_name="stack",
        ),
    )


def recipes_page() -> rx.Component:
    return shell(
        rx.box(
            rx.text("The recipe box", class_name="kicker"),
            rx.heading("Find a card", as_="h1", class_name="display hero-title"),
            rx.text(
                "Search a title, a fruit, or a pantry staple. Tags match all at once: vegetarian and dessert means both.",
                class_name="lede",
            ),
            rx.input(
                placeholder="Search peaches, noodles, molasses…",
                value=KitchenState.query,
                on_change=KitchenState.set_query,
                class_name="search",
            ),
            rx.box(
                filter_chip(
                    "Vegetarian",
                    KitchenState.show_vegetarian,
                    KitchenState.toggle_vegetarian,
                    "#C6E59A",
                ),
                filter_chip(
                    "Quick",
                    KitchenState.show_quick,
                    KitchenState.toggle_quick,
                    "#8EC5FF",
                ),
                filter_chip(
                    "Dessert",
                    KitchenState.show_dessert,
                    KitchenState.toggle_dessert,
                    "#FFB088",
                ),
                rx.cond(
                    KitchenState.filters_on,
                    rx.button(
                        "Clear",
                        on_click=KitchenState.clear_filters,
                        class_name="btn btn-ghost btn-small",
                    ),
                    rx.fragment(),
                ),
                class_name="chip-row",
            ),
            rx.text(KitchenState.match_label, class_name="muted"),
            class_name="panel stack",
        ),
        rx.cond(
            KitchenState.match_count == 0,
            rx.box(
                rx.heading("No card matches", as_="h2", class_name="display"),
                rx.cond(
                    KitchenState.query_blank,
                    rx.text(
                        "Nothing has every tag you picked. Untick one and look again.",
                        class_name="muted",
                    ),
                    rx.text(
                        "Nothing in the box matches “",
                        KitchenState.query,
                        "”.",
                        class_name="muted",
                    ),
                ),
                class_name="panel stack",
            ),
            rx.box(
                rx.foreach(KitchenState.filtered_recipes, live_card),
                class_name="card-grid",
            ),
        ),
    )


def ingredient_row(row) -> rx.Component:
    return rx.box(
        rx.text(row["amount"], class_name="amount"),
        rx.text(row["item"], class_name="ing-item"),
        class_name="ing-row",
    )


def step_row(row) -> rx.Component:
    return rx.box(
        rx.checkbox(
            checked=row["done"] == "yes",
            on_change=lambda value: KitchenState.toggle_step(row["index"], value),
            color_scheme="orange",
            size="3",
            variant="soft",
        ),
        rx.text(row["number"], class_name="step-no"),
        rx.text(
            row["text"],
            class_name="step-copy",
            text_decoration=rx.cond(row["done"] == "yes", "line-through", "none"),
            color=rx.cond(row["done"] == "yes", "rgba(255,246,234,0.45)", "#FFF6EA"),
        ),
        class_name="step-row",
    )


def timer_chip(chip) -> rx.Component:
    return rx.button(
        chip["label"],
        on_click=KitchenState.set_minutes(chip["minutes"]),
        class_name="btn btn-ghost btn-small",
    )


def ingredients_tab() -> rx.Component:
    return rx.box(
        rx.foreach(KitchenState.ingredient_rows, ingredient_row),
        class_name="stack",
    )


def steps_tab() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(KitchenState.steps_label, class_name="muted"),
            rx.button(
                "Clear ticks",
                on_click=KitchenState.reset_checks,
                class_name="btn btn-ghost btn-small",
            ),
            class_name="spread",
        ),
        rx.box(rx.foreach(KitchenState.step_rows, step_row), class_name="step-list"),
        class_name="stack",
    )


def timer_tab() -> rx.Component:
    view = KitchenState.recipe_view
    return rx.box(
        rx.text(view["timer_hint"], class_name="muted"),
        rx.box(rx.foreach(KitchenState.timer_chips, timer_chip), class_name="chip-row"),
        rx.box(
            rx.input(
                value=KitchenState.minute_draft,
                on_change=KitchenState.set_minute_draft,
                class_name="minutes",
            ),
            rx.button(
                "Set minutes",
                on_click=KitchenState.apply_minute_draft,
                class_name="btn btn-small",
            ),
            class_name="row",
        ),
        rx.heading(KitchenState.timer_clock, as_="h2", class_name="timer-digits"),
        rx.box(
            rx.box(class_name="fill", width=KitchenState.timer_bar_width),
            class_name="track",
        ),
        rx.cond(
            KitchenState.timer_done,
            rx.box(
                "Time's up. Check the pan.",
                class_name="banner",
            ),
            rx.fragment(),
        ),
        rx.box(
            rx.cond(
                KitchenState.timer_running,
                rx.button("Pause", on_click=KitchenState.pause_timer, class_name="btn"),
                rx.button("Start", on_click=KitchenState.start_timer, class_name="btn"),
            ),
            rx.button(
                "Reset",
                on_click=KitchenState.reset_timer,
                class_name="btn btn-ghost",
            ),
            class_name="button-row",
        ),
        class_name="stack",
    )


def recipe_workspace() -> rx.Component:
    view = KitchenState.recipe_view
    return rx.box(
        rx.box(
            rx.link("← The recipe box", href="/recipes", class_name="text-link"),
            rx.box(
                rx.box(view["emoji"], class_name="emoji large"),
                rx.box(
                    rx.heading(view["title"], as_="h1", class_name="display recipe-title"),
                    rx.text(view["blurb"], class_name="lede"),
                    class_name="stack tight",
                ),
                class_name="row",
            ),
            rx.box(
                rx.box(view["time"], class_name="pill pill-plain"),
                rx.box(view["difficulty"], class_name="pill pill-plain"),
                rx.box(view["yield_label"], class_name="pill pill-plain"),
                class_name="pill-row",
            ),
            rx.text(view["note"], class_name="muted"),
            class_name="panel stack",
        ),
        rx.box(
            rx.box(
                rx.text(view["portion_label"], class_name="kicker"),
                rx.box(
                    rx.button(
                        "–",
                        on_click=KitchenState.bump_servings(-1),
                        disabled=KitchenState.at_min_servings,
                        class_name="btn btn-ghost btn-small",
                        aria_label="Fewer servings",
                    ),
                    rx.text(KitchenState.servings, class_name="stepper-num"),
                    rx.button(
                        "+",
                        on_click=KitchenState.bump_servings(1),
                        disabled=KitchenState.at_max_servings,
                        class_name="btn btn-ghost btn-small",
                        aria_label="More servings",
                    ),
                    class_name="stepper",
                ),
                class_name="stack tight",
            ),
            rx.box(
                rx.text(KitchenState.scale_note, class_name="muted"),
                rx.button(
                    "Back to the card",
                    on_click=KitchenState.reset_servings,
                    class_name="btn btn-ghost btn-small",
                ),
                class_name="stack tight",
            ),
            class_name="panel spread",
        ),
        rx.box(
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger(
                        "Ingredients",
                        value="ingredients",
                        class_name="folder-tab",
                    ),
                    rx.tabs.trigger("Steps", value="steps", class_name="folder-tab"),
                    rx.tabs.trigger("Timer", value="timer", class_name="folder-tab"),
                    class_name="folder-list",
                ),
                rx.tabs.content(ingredients_tab(), value="ingredients", class_name="folder-panel"),
                rx.tabs.content(steps_tab(), value="steps", class_name="folder-panel"),
                rx.tabs.content(timer_tab(), value="timer", class_name="folder-panel"),
                value=KitchenState.recipe_tab,
                on_change=KitchenState.select_recipe_tab,
                width="100%",
            ),
            class_name="tab-card",
        ),
        class_name="stack",
    )


def recipe_page() -> rx.Component:
    return shell(
        rx.cond(
            KitchenState.recipe_loading,
            rx.box(
                rx.heading("Pulling the card from the box…", as_="h1", class_name="display"),
                class_name="panel",
            ),
            rx.cond(
                KitchenState.recipe_found,
                recipe_workspace(),
                rx.box(
                    rx.heading("That card isn't in the box", as_="h1", class_name="display"),
                    rx.text(
                        "This address doesn't match a recipe. The rest of the cards are where you left them.",
                        class_name="muted",
                    ),
                    rx.link("Back to the recipe box", href="/recipes", class_name="text-link"),
                    class_name="panel stack",
                ),
            ),
        )
    )


def about_page() -> rx.Component:
    return shell(
        rx.box(
            rx.text("The cook", class_name="kicker"),
            rx.heading("Clementine Brooks", as_="h1", class_name="display hero-title"),
            rx.text(
                "She rents a one-bedroom above a shoe repair shop on Bull Street. The kitchen is a four-burner stove, a window that sticks, and a painting she bought because the colors looked like cut fruit.",
                class_name="lede",
            ),
            class_name="panel stack",
        ),
        rx.box(
            rx.box(
                rx.heading("How a card gets in the box", as_="h2", class_name="display"),
                rx.text(
                    "She cooks a recipe three times before it earns a card. Once as written. Once for a friend who is hungry at 7:15. Once halved, to be sure the jam and the salt still make sense.",
                    class_name="muted",
                ),
                rx.text(
                    "The servings knob is that third test, left on the card. Tick the steps if the phone rings. The timer is the one she actually sets, not the hopeful number from someone else's book.",
                    class_name="muted",
                ),
                class_name="panel stack",
            ),
            rx.box(
                rx.heading("Always in the pantry", as_="h2", class_name="display"),
                rx.box(
                    tag_pill("Butter", "dessert"),
                    tag_pill("Lemons", "quick"),
                    tag_pill("Cornmeal", "veg"),
                    tag_pill("Apricot jam", "dessert"),
                    tag_pill("Olive oil", "veg"),
                    tag_pill("Brown sugar", "dessert"),
                    tag_pill("Chili flakes", "quick"),
                    tag_pill("Yogurt", "veg"),
                    class_name="pantry",
                ),
                rx.text(
                    "If a recipe asks for something that would spoil before Thursday, it doesn't get written down.",
                    class_name="muted",
                ),
                class_name="panel stack",
            ),
            class_name="split even",
        ),
        rx.box(
            rx.box(
                rx.heading("The painting over the stove", as_="h2", class_name="display"),
                rx.text(
                    "The navy canvas behind these cards is the yard-sale painting that hangs above her burners. Orange, blue, green, red, yellow. She stares at it while a skillet heats.",
                    class_name="muted",
                ),
                rx.text(
                    "It stays put when you scroll, the way it stays put when she walks from the stove to the fridge.",
                    class_name="muted",
                ),
                class_name="panel stack",
            ),
            rx.box(
                rx.heading("What this kitchen is", as_="h2", class_name="display"),
                rx.text(
                    "A home cook's box. Not a restaurant, not a class. Vegetarian on these cards means no meat or fish. Quick means she can start after work and still eat at a reasonable hour.",
                    class_name="muted",
                ),
                rx.link("Pick a card and cook", href="/recipes", class_name="text-link"),
                class_name="panel stack",
            ),
            class_name="split even",
        ),
    )
