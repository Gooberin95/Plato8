import reflex as rx

config = rx.Config(
    app_name="clementine",
    disable_plugins=[rx.plugins.SitemapPlugin],
    plugins=[
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                accent_color="orange",
                radius="large",
                has_background=False,
            )
        )
    ],
)
