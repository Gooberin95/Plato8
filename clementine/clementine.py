"""Clementine's Skillet application entrypoint."""

import reflex as rx

from clementine.components import about_page, home_page, recipe_page, recipes_page
from clementine.state import KitchenState

app = rx.App(
    stylesheets=[
        "/styles.css",
        "https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700;800&display=swap",
    ],
)

app.add_page(
    recipe_page,
    route="/recipe/[slug]",
    title="Recipe · Clementine's Skillet",
    description="A Clementine Brooks recipe card with scalable ingredients, steps, and a kitchen timer.",
    on_load=KitchenState.load_recipe,
)
app.add_page(
    home_page,
    route="/",
    title="Clementine's Skillet",
    description="Weeknight recipe cards from Clementine Brooks's Savannah apartment kitchen.",
)
app.add_page(
    recipes_page,
    route="/recipes",
    title="Recipes · Clementine's Skillet",
    description="Search and filter Clementine's recipe box by vegetarian, quick, and dessert.",
)
app.add_page(
    about_page,
    route="/about",
    title="About Clementine · Clementine's Skillet",
    description="Meet Clementine Brooks, the home cook behind the skillet.",
)
