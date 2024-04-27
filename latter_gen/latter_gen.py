import reflex as rx
#import latter_gen.constants as const
import latter_gen.styles.styles as styles
from latter_gen.pages.index import index
#from latter_gen.pages.courses import courses
#from latter_gen.api.api import repo, live, featured, schedule

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    theme=rx.theme(
        appearance="light",radius="large", accent_color="teal"
    ),
    head_components=[

    ],
    
)

#app.api.add_api_route("/repo", repo)
#app.api.add_api_route("/live/{user}", live)
#app.api.add_api_route("/featured", featured)
#app.api.add_api_route("/schedule", schedule)
