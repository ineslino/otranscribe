"""otranscribe

This module exposes a command‑line interface for transcribing audio and
video files using OpenAI's speech‑to‑text API. It converts any ffmpeg
supported input to a 16 kHz mono WAV file before calling the API.  The
package supports speaker diarisation via the `gpt‑4o‑transcribe‑diarize`
model and can output both raw API responses and a cleaned, human friendly
transcript with timestamps and speaker labels.

Usage as a library is not the primary goal; use the ``otranscribe`` CLI
installed by this package.
"""

__all__ = []
