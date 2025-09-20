import reflex as rx


class Quill(rx.Component):
    """A custom component for the react-quill editor."""

    library = "react-quill-new"
    tag = "ReactQuill"
    is_default = True
    value: rx.Var[str]
    on_change: rx.EventHandler[lambda value, delta, source, editor: [value]]
    theme: rx.Var[str] = "snow"

    def get_custom_attrs(self) -> dict:
        return {"style": {"height": "300px"}}


quill = Quill.create