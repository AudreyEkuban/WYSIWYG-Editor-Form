import reflex as rx
from app.states.state import EditorState
from app.components.quill import quill


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.h1(
                "WYSIWYG Editor", class_name="text-3xl font-bold mb-6 text-gray-800"
            ),
            quill(
                value=EditorState.content,
                on_change=EditorState.handle_change,
                theme="snow",
                class_name="mb-6 h-64",
            ),
            rx.el.h2(
                "Live Preview",
                class_name="text-2xl font-semibold mt-8 mb-4 text-gray-700",
            ),
            rx.el.div(
                dangerously_set_inner_html=EditorState.content,
                class_name="p-4 border border-gray-200 rounded-md min-h-[100px] bg-gray-50 prose max-w-none",
            ),
            class_name="w-full",
        ),
        class_name="font-['Inter'] bg-white min-h-screen p-4 sm:p-8 md:p-12 flex items-center justify-center",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
        rx.el.link(
            rel="stylesheet", href="https://unpkg.com/quill@1.3.7/dist/quill.snow.css"
        ),
        rx.el.link(
            href="https://cdn.jsdelivr.net/npm/@tailwindcss/typography@0.5.x/dist/typography.min.css",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)