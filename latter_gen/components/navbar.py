import reflex as rx
import latter_gen.styles.styles as styles
#from latter_gen.routes import Route
from latter_gen.styles.styles import Size
from latter_gen.styles.colors import Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("moure", as_="span", color=Color.PRIMARY.value),
                rx.text("dev", as_="span", color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            ),
            href="/"
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )