"""Recipe cards for Clementine Brooks's kitchen.

Quantities are stored as numbers so a servings change can rescale them.
Anything under ``fixed`` (a pinch, a splash, cream for the table) stays put.
"""

from __future__ import annotations

RECIPES: list[dict] = [
    {
        "slug": "skillet-peach-spoon-cake",
        "title": "Skillet Peach Spoon Cake",
        "emoji": "🍑",
        "blurb": "Peaches go jammy in brown sugar, then a cornmeal batter bakes over them in the same skillet.",
        "time_label": "45 min",
        "difficulty": "One skillet",
        "yield_label": "One 10-inch skillet",
        "portion": "servings",
        "servings": 8,
        "tags": ["vegetarian", "dessert"],
        "timer_presets": [6, 28],
        "timer_hint": "The peaches want about 6 minutes. The cake wants 28.",
        "note": "The center should still quiver when you pull it. Cold cream is not optional in this kitchen.",
        "ingredients": [
            {"qty": 4, "unit": "", "item": "ripe peaches, cut in wedges"},
            {"qty": 3, "unit": "tbsp", "item": "unsalted butter"},
            {"qty": 1 / 3, "unit": "cup", "item": "packed brown sugar"},
            {"qty": 1, "unit": "tbsp", "item": "lemon juice"},
            {"qty": 1, "unit": "cup", "item": "whole milk"},
            {"qty": 3 / 4, "unit": "cup", "item": "fine cornmeal"},
            {"qty": 1 / 4, "unit": "cup", "item": "all-purpose flour"},
            {"qty": 1 / 3, "unit": "cup", "item": "sugar"},
            {"qty": 1, "unit": "", "item": "large egg"},
            {"qty": 1, "unit": "tsp", "item": "baking powder"},
            {"qty": 1 / 2, "unit": "tsp", "item": "kosher salt"},
            {"qty": 1, "unit": "tsp", "item": "vanilla extract"},
            {"fixed": "to serve", "item": "cold cream"},
        ],
        "steps": [
            "Heat the oven to 375°F. Slice the peaches into thick wedges and fish out the pits.",
            "Melt the butter in a 10-inch oven-safe skillet over medium heat. Stir in the brown sugar and lemon juice until the sugar turns glossy, about 2 minutes.",
            "Add the peaches. Cook, stirring once, until they soften and the juices look like syrup, about 6 minutes. Take the skillet off the heat.",
            "Whisk the milk, cornmeal, flour, sugar, egg, baking powder, salt, and vanilla in a bowl until the batter is smooth.",
            "Pour the batter over the peaches. Tilt the skillet so it settles in an even layer. Do not stir.",
            "Bake until the top is golden and the center still quivers, 26 to 30 minutes. Start the timer at 28.",
            "Cool 10 minutes. Spoon it out warm, with cold cream.",
        ],
    },
    {
        "slug": "tomato-butter-noodles",
        "title": "Fifteen-Minute Tomato Butter Noodles",
        "emoji": "🍝",
        "blurb": "Cherry tomatoes burst into butter while the spaghetti boils. Dinner is the pot and one skillet.",
        "time_label": "15 min",
        "difficulty": "Tuesday fast",
        "yield_label": "Two generous bowls",
        "portion": "servings",
        "servings": 2,
        "tags": ["vegetarian", "quick"],
        "timer_presets": [8],
        "timer_hint": "Give the tomatoes 8 minutes to slump.",
        "note": "Vegetarian here means no meat or fish. The cheese can be parmesan or a hard sheep cheese.",
        "ingredients": [
            {"qty": 6, "unit": "oz", "item": "spaghetti"},
            {"qty": 3, "unit": "tbsp", "item": "unsalted butter"},
            {"qty": 2, "unit": "", "item": "garlic cloves, sliced thin"},
            {"qty": 1, "unit": "pint", "item": "cherry tomatoes"},
            {"qty": 1 / 2, "unit": "tsp", "item": "kosher salt, plus more for the pasta water"},
            {"qty": 1 / 4, "unit": "tsp", "item": "red pepper flakes"},
            {"qty": 1 / 3, "unit": "cup", "item": "finely grated hard cheese"},
            {"fixed": "a splash", "item": "starchy pasta water"},
            {"fixed": "a handful", "item": "basil leaves"},
            {"fixed": "to finish", "item": "black pepper"},
        ],
        "steps": [
            "Boil a pot of well-salted water and add the spaghetti.",
            "While it cooks, melt the butter in a skillet over medium heat. Add the garlic and pepper flakes. Stir until the garlic smells sweet, about 1 minute.",
            "Add the tomatoes and the measured salt. Cook, pressing them with a spoon, until most have burst, about 8 minutes.",
            "Scoop out a mug of pasta water, then drain the noodles.",
            "Add the noodles to the skillet with a splash of that water and the cheese. Toss until the sauce looks glossy and sticks to the strands.",
            "Tear the basil over the top, grind pepper, and eat it from the skillet if the bowls are still in the drainer.",
        ],
    },
    {
        "slug": "honey-chili-carrots",
        "title": "Honey-Chili Carrots with Yogurt",
        "emoji": "🥕",
        "blurb": "A hot sheet pan, honey that catches, and a cold garlic yogurt so the plate isn't only sweet.",
        "time_label": "25 min",
        "difficulty": "Sheet pan",
        "yield_label": "A side that can be dinner",
        "portion": "servings",
        "servings": 4,
        "tags": ["vegetarian", "quick"],
        "timer_presets": [22],
        "timer_hint": "The carrots roast for 22 minutes.",
        "note": "If the carrots are skinny, check them at 18 minutes. Thick ones like the full 22.",
        "ingredients": [
            {"qty": 1.5, "unit": "lb", "item": "carrots, scrubbed and halved lengthwise"},
            {"qty": 2, "unit": "tbsp", "item": "olive oil"},
            {"qty": 1, "unit": "tsp", "item": "kosher salt"},
            {"qty": 2, "unit": "tbsp", "item": "honey"},
            {"qty": 1, "unit": "tbsp", "item": "unsalted butter"},
            {"qty": 1 / 2, "unit": "tsp", "item": "chili flakes"},
            {"qty": 1 / 2, "unit": "cup", "item": "plain yogurt"},
            {"qty": 1, "unit": "tbsp", "item": "lemon juice"},
            {"qty": 1, "unit": "", "item": "small garlic clove, grated"},
            {"fixed": "a handful", "item": "dill or cilantro"},
            {"fixed": "to finish", "item": "flaky salt"},
        ],
        "steps": [
            "Heat the oven to 425°F. Toss the carrots with the olive oil and kosher salt on a sheet pan.",
            "Roast until the cut sides are browned and a knife slides in, about 22 minutes.",
            "Stir the yogurt, lemon juice, and grated garlic in a small bowl. Set it in the fridge if you have room.",
            "When the carrots come out, dot them with butter, drizzle the honey, and sprinkle the chili flakes. Toss on the hot pan so the honey goes shiny.",
            "Spread the yogurt on a plate, pile the carrots on top, and finish with herbs and flaky salt.",
        ],
    },
    {
        "slug": "apricot-pan-sauce-chicken",
        "title": "Apricot Pan-Sauce Chicken",
        "emoji": "🍗",
        "blurb": "Thighs brown in a skillet, then a jam-and-vinegar sauce turns the drippings into dinner.",
        "time_label": "30 min",
        "difficulty": "One skillet",
        "yield_label": "Enough for rice or toast",
        "portion": "servings",
        "servings": 4,
        "tags": ["quick"],
        "timer_presets": [6, 4],
        "timer_hint": "Six minutes for the first side. Four for the sauce to go syrupy.",
        "note": "Boneless thighs stay tender if you don't rush the browning. The sauce should coat a spoon.",
        "ingredients": [
            {"qty": 4, "unit": "", "item": "boneless chicken thighs"},
            {"qty": 1, "unit": "tsp", "item": "kosher salt"},
            {"qty": 1 / 2, "unit": "tsp", "item": "black pepper"},
            {"qty": 1, "unit": "tbsp", "item": "olive oil"},
            {"qty": 1, "unit": "", "item": "shallot, minced"},
            {"qty": 2, "unit": "", "item": "garlic cloves, minced"},
            {"qty": 1 / 2, "unit": "cup", "item": "apricot jam"},
            {"qty": 2, "unit": "tbsp", "item": "apple cider vinegar"},
            {"qty": 1, "unit": "tbsp", "item": "soy sauce"},
            {"qty": 1 / 4, "unit": "cup", "item": "water"},
            {"qty": 1, "unit": "tsp", "item": "fresh thyme leaves, or 1/2 tsp dried"},
        ],
        "steps": [
            "Pat the thighs dry. Season both sides with salt and pepper.",
            "Heat the oil in a skillet over medium-high heat. Cook the thighs until deep golden, about 6 minutes on the first side and 4 on the second. Move them to a plate.",
            "Lower the heat. Cook the shallot and garlic in the drippings until soft, about 1 minute.",
            "Add the jam, vinegar, soy sauce, water, and thyme. Simmer until the sauce looks syrupy, about 4 minutes.",
            "Return the chicken and any juices. Turn to coat, and simmer until the thickest part is cooked through, about 6 minutes more.",
            "Rest 3 minutes. Spoon the sauce over rice, or onto buttered toast if the rice never happened.",
        ],
    },
    {
        "slug": "olive-oil-almond-cake",
        "title": "Olive Oil Almond Cake",
        "emoji": "🍰",
        "blurb": "A tender lemon cake with almond flour and a pour of olive oil. No mixer, one bowl.",
        "time_label": "55 min",
        "difficulty": "One bowl",
        "yield_label": "One 8-inch cake",
        "portion": "servings",
        "servings": 8,
        "tags": ["vegetarian", "dessert"],
        "timer_presets": [40],
        "timer_hint": "Bake it for 40 minutes, then test the center.",
        "note": "Use an olive oil you would put on bread. A bitter oil makes a bitter cake.",
        "ingredients": [
            {"qty": 1, "unit": "cup", "item": "sugar"},
            {"qty": 2, "unit": "", "item": "large eggs"},
            {"qty": 1 / 2, "unit": "cup", "item": "extra-virgin olive oil"},
            {"qty": 1 / 2, "unit": "cup", "item": "whole milk"},
            {"qty": 1, "unit": "tbsp", "item": "lemon zest"},
            {"qty": 1 / 2, "unit": "tsp", "item": "almond extract"},
            {"qty": 1, "unit": "cup", "item": "almond flour"},
            {"qty": 1 / 2, "unit": "cup", "item": "all-purpose flour"},
            {"qty": 1, "unit": "tsp", "item": "baking powder"},
            {"qty": 1 / 2, "unit": "tsp", "item": "kosher salt"},
            {"fixed": "to finish", "item": "powdered sugar"},
        ],
        "steps": [
            "Heat the oven to 350°F. Butter an 8-inch cake pan and line the bottom with parchment.",
            "Whisk the sugar, eggs, olive oil, milk, lemon zest, and almond extract until the mixture looks creamy.",
            "Add both flours, the baking powder, and the salt. Whisk just until you can't see dry streaks.",
            "Pour the batter into the pan. Bake until the top is deep gold and a toothpick comes out with a few moist crumbs, about 40 minutes.",
            "Cool 15 minutes in the pan, then turn it out. Dust with powdered sugar once it is only warm.",
        ],
    },
    {
        "slug": "coconut-lime-greens",
        "title": "Coconut-Lime Rice with Charred Greens",
        "emoji": "🥬",
        "blurb": "Rice simmered in coconut milk, lime, and a skillet of greens that get a little black at the edges.",
        "time_label": "35 min",
        "difficulty": "Two pans",
        "yield_label": "A full plate",
        "portion": "servings",
        "servings": 4,
        "tags": ["vegetarian"],
        "timer_presets": [15, 6],
        "timer_hint": "The rice simmers for 15 covered minutes. The greens take about 6.",
        "note": "Chard, kale, or a bag of mixed greens all work. Keep the stems. They stay sweet if you start them first.",
        "ingredients": [
            {"qty": 1, "unit": "cup", "item": "long-grain rice, rinsed"},
            {"qty": 1, "unit": "cup", "item": "full-fat coconut milk"},
            {"qty": 1, "unit": "cup", "item": "water"},
            {"qty": 1 / 2, "unit": "tsp", "item": "kosher salt, divided"},
            {"qty": 1, "unit": "", "item": "lime, zest and juice"},
            {"qty": 1, "unit": "bunch", "item": "Swiss chard, stems chopped and leaves torn"},
            {"qty": 2, "unit": "tbsp", "item": "olive oil"},
            {"qty": 2, "unit": "", "item": "garlic cloves, sliced"},
            {"qty": 1 / 4, "unit": "tsp", "item": "red pepper flakes"},
            {"qty": 2, "unit": "", "item": "scallions, sliced"},
        ],
        "steps": [
            "Put the rice, coconut milk, water, lime zest, and 1/4 teaspoon of salt in a saucepan. Bring it to a simmer.",
            "Cover, drop the heat to low, and cook 15 minutes. Take it off the heat and leave the lid on for 5 minutes more.",
            "Meanwhile, warm the olive oil in a wide skillet over medium-high heat. Add the chard stems and cook until they soften, about 3 minutes.",
            "Add the garlic, pepper flakes, and a pinch of the remaining salt. Stir for 30 seconds.",
            "Add the leaves in handfuls. Cook until they collapse and a few edges char, about 3 minutes. Finish with the lime juice.",
            "Fluff the rice, fold in the scallions, and serve the greens on top with the rest of the salt if it needs it.",
        ],
    },
    {
        "slug": "molasses-ginger-crinkles",
        "title": "Molasses Ginger Crinkles",
        "emoji": "🍪",
        "blurb": "Crackled cookies rolled in sugar. The batch scales cleanly if you only want a half dozen.",
        "time_label": "40 min",
        "difficulty": "One bowl",
        "yield_label": "About 20 cookies",
        "portion": "cookies",
        "servings": 20,
        "tags": ["vegetarian", "dessert"],
        "timer_presets": [11],
        "timer_hint": "Each tray bakes for 11 minutes.",
        "note": "They look soft in the middle when they come out. That is the cookie, not a mistake. They set as they cool.",
        "ingredients": [
            {"qty": 3 / 4, "unit": "cup", "item": "unsalted butter, softened"},
            {"qty": 1, "unit": "cup", "item": "sugar, plus more for rolling"},
            {"qty": 1 / 4, "unit": "cup", "item": "molasses"},
            {"qty": 1, "unit": "", "item": "large egg"},
            {"qty": 2, "unit": "cups", "item": "all-purpose flour"},
            {"qty": 2, "unit": "tsp", "item": "ground ginger"},
            {"qty": 1, "unit": "tsp", "item": "cinnamon"},
            {"qty": 1 / 4, "unit": "tsp", "item": "ground cloves"},
            {"qty": 2, "unit": "tsp", "item": "baking soda"},
            {"qty": 1 / 4, "unit": "tsp", "item": "kosher salt"},
        ],
        "steps": [
            "Heat the oven to 350°F. Line two sheet pans with parchment.",
            "Stir the butter, sugar, molasses, and egg together until the mixture is even. A wooden spoon is enough.",
            "Add the flour, ginger, cinnamon, cloves, baking soda, and salt. Stir until a soft dough forms and no dry flour remains.",
            "Roll tablespoons of dough into balls, then roll the balls in sugar. Set them 2 inches apart.",
            "Bake until the edges are set and the tops have cracked, about 11 minutes.",
            "Cool on the pan for 5 minutes before moving them. Hide a few, or they will not make it to tomorrow.",
        ],
    },
    {
        "slug": "sheet-pan-sausage-grapes",
        "title": "Sheet-Pan Sausage and Grapes",
        "emoji": "🍇",
        "blurb": "Sausage, red grapes, and onion roast until the grapes burst and glaze the pan.",
        "time_label": "30 min",
        "difficulty": "Sheet pan",
        "yield_label": "Dinner with bread on the side",
        "portion": "servings",
        "servings": 4,
        "tags": ["quick"],
        "timer_presets": [25],
        "timer_hint": "Roast the pan for 25 minutes.",
        "note": "Any smoked or Italian sausage works. Prick the links so they don't split all at once.",
        "ingredients": [
            {"qty": 1.25, "unit": "lb", "item": "sausage, cut into chunks"},
            {"qty": 3, "unit": "cups", "item": "red grapes"},
            {"qty": 1, "unit": "", "item": "red onion, cut in wedges"},
            {"qty": 2, "unit": "tbsp", "item": "olive oil"},
            {"qty": 1, "unit": "tbsp", "item": "whole-grain mustard"},
            {"qty": 1, "unit": "tsp", "item": "maple syrup"},
            {"qty": 1, "unit": "tsp", "item": "chopped fresh rosemary"},
            {"qty": 1 / 2, "unit": "tsp", "item": "black pepper"},
            {"fixed": "to serve", "item": "crusty bread"},
        ],
        "steps": [
            "Heat the oven to 425°F.",
            "Toss the sausage, grapes, and onion on a sheet pan with the olive oil, mustard, maple syrup, rosemary, and pepper.",
            "Spread everything into one layer. The grapes should touch the pan, not sit in a pile.",
            "Roast until the sausage is browned and the grapes have burst and gone jammy, about 25 minutes. Stir once halfway.",
            "Scrape the pan juices over the top and serve with bread for the glaze.",
        ],
    },
    {
        "slug": "brown-sugar-banana-cups",
        "title": "Brown-Sugar Banana Cups",
        "emoji": "🍌",
        "blurb": "Bananas cooked in butter and brown sugar, spooned over cold yogurt. A dessert that fits a weeknight.",
        "time_label": "15 min",
        "difficulty": "Tuesday fast",
        "yield_label": "Four cups",
        "portion": "servings",
        "servings": 4,
        "tags": ["vegetarian", "quick", "dessert"],
        "timer_presets": [4],
        "timer_hint": "The bananas need 4 minutes in the skillet.",
        "note": "Use bananas with a few brown spots. Green ones stay starchy and won't go saucy.",
        "ingredients": [
            {"qty": 4, "unit": "", "item": "ripe bananas, halved lengthwise"},
            {"qty": 1, "unit": "tbsp", "item": "unsalted butter"},
            {"qty": 2, "unit": "tbsp", "item": "packed brown sugar"},
            {"qty": 1 / 4, "unit": "tsp", "item": "cinnamon"},
            {"qty": 1, "unit": "tsp", "item": "vanilla extract"},
            {"fixed": "a pinch", "item": "kosher salt"},
            {"qty": 1, "unit": "cup", "item": "plain yogurt"},
            {"qty": 4, "unit": "tbsp", "item": "toasted pecans"},
        ],
        "steps": [
            "Spoon the yogurt into four cups and keep them cold.",
            "Melt the butter in a skillet over medium heat. Lay in the bananas, cut side down.",
            "Sprinkle the brown sugar, cinnamon, and salt over them. Cook until the cut sides are caramelized, about 2 minutes, then turn.",
            "Cook another 2 minutes. Pull the pan off the heat and stir in the vanilla.",
            "Spoon the bananas and their syrup over the yogurt. Finish with the pecans.",
        ],
    },
]

RECIPE_BY_SLUG: dict[str, dict] = {recipe["slug"]: recipe for recipe in RECIPES}

TAG_ORDER = ("vegetarian", "quick", "dessert")

_FRACTIONS: tuple[tuple[float, str], ...] = (
    (0.0, ""),
    (0.125, "1/8"),
    (1 / 6, "1/6"),
    (0.25, "1/4"),
    (1 / 3, "1/3"),
    (0.375, "3/8"),
    (0.5, "1/2"),
    (0.625, "5/8"),
    (2 / 3, "2/3"),
    (0.75, "3/4"),
    (5 / 6, "5/6"),
    (0.875, "7/8"),
    (1.0, "1"),
)


def pretty_number(value: float) -> str:
    """Turn a scaled quantity into a cook-friendly number."""
    if value <= 0:
        return "0"
    whole = int(value)
    frac = value - whole
    nearest = min(_FRACTIONS, key=lambda pair: abs(frac - pair[0]))
    if abs(frac - nearest[0]) > 0.04:
        return f"{value:.2f}".rstrip("0").rstrip(".")
    base, label = nearest
    if base == 1:
        whole += 1
        label = ""
    if base == 0:
        label = ""
    if whole and label:
        return f"{whole} {label}"
    if label:
        return label
    return str(whole)


_PLURALS = {"cup": "cups", "pint": "pints", "bunch": "bunches"}


def format_qty(qty: float, unit: str) -> str:
    if unit in {"g", "ml"}:
        number = str(max(1, int(round(qty))))
    else:
        number = pretty_number(qty)
    if qty > 1 and unit in _PLURALS:
        unit = _PLURALS[unit]
    return f"{number} {unit}".strip()


def card_payload(recipe: dict) -> dict[str, str]:
    tags = set(recipe["tags"])
    return {
        "slug": recipe["slug"],
        "title": recipe["title"],
        "blurb": recipe["blurb"],
        "time": recipe["time_label"],
        "servings_label": f"{recipe['servings']} {recipe['portion']}",
        "emoji": recipe["emoji"],
        "difficulty": recipe["difficulty"],
        "vegetarian": "yes" if "vegetarian" in tags else "no",
        "quick": "yes" if "quick" in tags else "no",
        "dessert": "yes" if "dessert" in tags else "no",
    }


def filter_recipes(
    query: str, vegetarian: bool, quick: bool, dessert: bool
) -> list[dict[str, str]]:
    needle = query.strip().lower()
    wanted = [
        tag
        for tag, enabled in (
            ("vegetarian", vegetarian),
            ("quick", quick),
            ("dessert", dessert),
        )
        if enabled
    ]
    matches: list[dict[str, str]] = []
    for recipe in RECIPES:
        haystack = " ".join(
            [
                recipe["title"],
                recipe["blurb"],
                recipe["note"],
                recipe["difficulty"],
                " ".join(ingredient["item"] for ingredient in recipe["ingredients"]),
            ]
        ).lower()
        if needle and needle not in haystack:
            continue
        if any(tag not in recipe["tags"] for tag in wanted):
            continue
        matches.append(card_payload(recipe))
    return matches


def recipe_view_dict(slug: str) -> dict[str, str]:
    recipe = RECIPE_BY_SLUG.get(slug)
    if recipe is None:
        return {
            "title": "That card isn't in the box",
            "blurb": "This address doesn't match a recipe. The box is still on the counter.",
            "time": "",
            "difficulty": "",
            "yield_label": "",
            "note": "",
            "emoji": "🥄",
            "timer_hint": "Set a few minutes and keep an eye on the pan.",
            "portion_label": "Servings",
        }
    return {
        "title": recipe["title"],
        "blurb": recipe["blurb"],
        "time": recipe["time_label"],
        "difficulty": recipe["difficulty"],
        "yield_label": recipe["yield_label"],
        "note": recipe["note"],
        "emoji": recipe["emoji"],
        "timer_hint": recipe["timer_hint"],
        "portion_label": recipe["portion"].capitalize(),
    }


def build_ingredients(slug: str, servings: int) -> list[dict[str, str]]:
    recipe = RECIPE_BY_SLUG.get(slug)
    if recipe is None:
        return []
    factor = servings / recipe["servings"]
    rows: list[dict[str, str]] = []
    for ingredient in recipe["ingredients"]:
        if "fixed" in ingredient:
            amount = ingredient["fixed"]
        else:
            amount = format_qty(ingredient["qty"] * factor, ingredient["unit"])
        rows.append({"amount": amount, "item": ingredient["item"]})
    return rows


def build_steps(slug: str, checked: list[bool]) -> list[dict[str, str]]:
    recipe = RECIPE_BY_SLUG.get(slug)
    if recipe is None:
        return []
    rows: list[dict[str, str]] = []
    for index, text in enumerate(recipe["steps"]):
        done = index < len(checked) and bool(checked[index])
        rows.append(
            {
                "index": str(index),
                "number": str(index + 1),
                "text": text,
                "done": "yes" if done else "no",
            }
        )
    return rows


def scale_sentence(slug: str, servings: int) -> str:
    recipe = RECIPE_BY_SLUG.get(slug)
    if recipe is None:
        return ""
    base = recipe["servings"]
    word = recipe["portion"]
    if servings == base:
        return f"Amounts as written, for {base} {word}."
    factor = servings / base
    pretty = f"{factor:.2f}".rstrip("0").rstrip(".")
    return f"Amounts ×{pretty}, scaled from {base} {word}."


def steps_sentence(checked: list[bool]) -> str:
    total = len(checked)
    if total == 0:
        return ""
    done = sum(1 for item in checked if item)
    return f"{done} of {total} ticked"


def timer_chip_rows(slug: str) -> list[dict[str, str]]:
    recipe = RECIPE_BY_SLUG.get(slug)
    presets = recipe["timer_presets"] if recipe else [5, 10, 15, 25]
    return [{"label": f"{minutes} min", "minutes": str(minutes)} for minutes in presets]


def clock_text(remaining: int) -> str:
    remaining = max(int(remaining), 0)
    minutes, seconds = divmod(remaining, 60)
    return f"{minutes:02d}:{seconds:02d}"


def bar_width(total: int, remaining: int) -> str:
    if total <= 0:
        return "0%"
    elapsed = max(total - max(remaining, 0), 0)
    percent = int(round(elapsed / total * 100))
    return f"{max(0, min(100, percent))}%"
