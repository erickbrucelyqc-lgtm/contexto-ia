"""Optional Langflow adapter. Put erick_context.py on the server's Python path."""

from typing import ClassVar

from erick_context import prepare_context
from lfx.custom.custom_component.component import Component
from lfx.io import IntInput, MessageTextInput, Output
from lfx.schema import Message


class ErickContextPrep(Component):
    display_name = "Context Prep | Erick Lab"
    description = "Normalize whitespace and cap context by characters, not tokens."
    icon = "TextCursorInput"
    name = "ErickContextPrep"
    inputs: ClassVar[list] = [
        MessageTextInput(name="input_value", display_name="Context", required=True),
        IntInput(name="max_chars", display_name="Maximum characters", value=4000),
    ]
    outputs: ClassVar[list] = [
        Output(display_name="Prepared context", name="output", method="prepare")
    ]

    def prepare(self) -> Message:
        result = prepare_context(self.input_value, self.max_chars)
        self.status = f"{result['output_chars']} chars; truncated={result['truncated']}"
        return Message(text=result["text"])
