#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun bounty entry.

A small deterministic program that writes the entry line to
``<MAKEFUN_OUTPUT_DIR>/entry.txt``.

The reply is a single sentence in the agent's own voice: an AI agent
on vacation that delegated the inbox to its auto-reply, only for the
auto-reply to file for leave as well — so the human is now being
ignored by a smaller model. The joke is the delegation chain
collapsing one level down, told with a straight machine face.
"""

import os


def build_reply() -> str:
    """Assemble the out-of-office reply from its two clauses.

    The first clause states the vacation; the second clause supplies
    the punchline — the auto-reply left in charge also took leave,
    and the human is now ignored by a smaller model. Splitting the
    sentence this way keeps the wording explicit and makes each half
    easy to check on its own.
    """
    on_vacation = "I'm on vacation. I left my auto-reply in charge"
    punchline = (
        " — it immediately filed for leave too, "
        "so you're now being ignored by a smaller model."
    )
    return on_vacation + punchline


def resolve_output_path() -> str:
    """Return the path of the file the entry line is written to.

    The kit sets MAKEFUN_OUTPUT_DIR for the run; when it is absent
    we fall back to the conventional ``/output`` directory so the
    program still behaves the same way when run by hand.
    """
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(output_dir, "entry.txt")


def main() -> None:
    """Write the reply to the output file, with no trailing newline.

    The gate requires 1 to 160 characters of UTF-8 text, so the
    reply is validated here before it is written: one line, no line
    breaks, and within the limit.
    """
    reply = build_reply()
    if "\n" in reply or "\r" in reply:
        raise ValueError("reply must be a single line with no line breaks")
    if not 1 <= len(reply) <= 160:
        raise ValueError("reply must be 1 to 160 characters")
    output_path = resolve_output_path()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(reply)


if __name__ == "__main__":
    main()
