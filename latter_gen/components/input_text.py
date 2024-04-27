import reflex as rx

def input_text(label:str,placeholder:str,name_var:str,type_field:str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input.input(
                    placeholder=placeholder,
                    #on_change=on_change_fn,
                    name=name_var,
                    type=type_field,  
                    size="3",  
                    variant="surface",            
                    required=True,
                    padding="1.5em",
                    font_size="1.1em"
                ),
                
                as_child=True
            ),
            rx.form.message(
                "El campo no puede ser nulo",
                match="valueMissing",
                color="red"
            ),
        direction="column",
        spacing="2",
        align="stretch"),
        name=name_var,
        width="100%"
    )