import reflex as rx


class EditorState(rx.State):
    """The state for the editor app."""

    content: str = "<p>Start typing here...</p>"

    def handle_change(self, value: str):
        """Handle the change in the editor's content."""
        self.content = value