import reflex as rx
import latter_gen.meta as meta
import latter_gen.styles.styles as styles
from latter_gen.components.navbar import navbar
from latter_gen.components.input_text import input_text
#from latter_gen.components.footer import footer
#from latter_gen.views.header import header
#from latter_gen.views.index_links import index_links
#from latter_gen.views.sponsors import sponsors
from latter_gen.styles.styles import Size

default_content = """

<p>Asunto: Canditura al puesto de Programador</p>
<p>Perú, 23 de abril 2024</p><br>

<p>Estimado Señor Bod</p><br>

<p>is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it 
to make a type specimen book</p><br>

<p>is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it 
to make a type specimen book</p><br>

<p>is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make 
a type specimen book</p><br><br>



<p>Cordialmente,</p>

<p>Amador</p>"""

class EditorState(rx.State):
    content: str = default_content

    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content


@rx.page(
    title=meta.index_title,
    description=meta.index_description,
    image=meta.preview,
    meta=meta.index_meta
)
def index() -> rx.Component:
    return rx.box(
        meta.lang(),
        navbar(),
        rx.vstack(
            rx.grid(
                rx.box(
                    rx.heading(
                        "Datos del remitente",
                        margin_bottom="1em"
                    ),
                    rx.form(
                        rx.flex(
                            input_text("Nombre(s)","Ingresa tus nombres","name","text"),  
                            input_text("Apellidos(s)","Ingresa tus apellidos","last_name","text"),
                            spacing="4",
                            margin_y="1em"
                        ),
                        rx.vstack(
                             
                            input_text("Correo electrónico","Ingresa tu correo","mail","text"), 
                            input_text("Tel. Celular","Ingresa tú número de celular","phone","text") 
                            
                        ),
                        rx.flex(
                            input_text("País","Ingresa tú país","country","text"),                           
                            input_text("Ciudad","Ingresa ciudad","city","text"),
                            spacing="4",
                            margin_y="1em" 
                        )
                    ),
                    rx.box(
                        rx.heading(
                            "Datos del destinatario"
                        ),
                        rx.text(
                            """Si conoces al destinatario de tu carta de presentación, 
                            puedes añadir sus datos aquí. No te preocupes si no los tienes; 
                            tu carta de presentación seguirá siendo estupenda sin ellos."""
                        )
                    ),
                    rx.form(
                        rx.vstack(
                            input_text("Empresa","Ej. Google","company","text"), 
                            input_text("Persona de contacto","Ej. Tio Bob","company_manager","text"),
                            input_text("País","Ej. Estados Unidos","company_country","text"),                           
                            input_text("Ciudad","Ej. Los Angeles","company_city","text"), 
                        )
                    ),
                    #Detalles
                    rx.box(
                        rx.heading(
                            "contenido de tu carta"
                        ),
                        rx.text(
                            """Describe en 3 o 4 párrafos los motivos por los que eres el candidato perfecto"""
                        )
                    ),  
                    rx.editor(
                        lang="es",
                        set_options=rx.EditorOptions(
                            button_list=[
                                ["fontSize", "formatBlock"],
                                ["fontColor", "hiliteColor"],
                                [
                                    "bold",
                                    "underline",
                                    "italic",
                                    "strike",
                                    "subscript",
                                    "superscript",
                                ],
                                ["removeFormat"],
                                ["outdent", "indent"],
                                ["align", "horizontalRule", "list"],
                                ["link"],
                                ["codeView"]
                            ]
                        ),
                        set_contents=EditorState.content,
                        on_change=EditorState.handle_change,
                        min_height="200px"
                    )          
                ),
                rx.flex(
                    rx.box(
                        #Emisor
                        rx.box(
                            rx.heading("Amador Quispe H",color="purple"),
                            
                            rx.text("Calle Miguel Grau 800-A"),
                            rx.text("Arequipa, Perú"),
                            rx.text("aquispe@gmail.com"),
                            margin_bottom="1em"
                        ),
                        #Destinatario
                        rx.box(
                            rx.text("GOOGLE", align="right"),
                            rx.text("Av. Loa Condes 112",align="right"),
                            rx.text("Santiago, Chile",align="right"),
                            rx.text("CHILE",align="right"),                        
                            margin_bottom="1em",
                        ),
                        #Cuerpo
                        rx.box(
                            rx.html(EditorState.content),
                            margin_bottom="1em",
                        ),
                        direction="column",
                        class_name=["a4"],
                        padding="3em",
                        background_color="white",
                        color="black"
                    ),
                    margin_x="auto"
                ),
                columns="2",
                spacing="4",
                width="100%",
                max_width=styles.MAX_WIDTH,
                margin="auto"
            ),
            
            margin_y="2em",
            margin_x="2em"
        ),
  
    
    )

#"sm": '30em',
#"md": '48em',
#"lg": '62em',
#"xl": '80em',
#"2xl": '96em',