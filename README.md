# otranscribe
<img width="1024" height="288" alt="image" src="https://github.com/user-attachments/assets/60c3ba0d-4f1a-421d-b095-be476e85239a" />

`otranscribe` is a tiny command line interface for turning any audio or video into text. It primarily wraps the [OpenAI speech-to-text API](https://developers.openai.com/api/reference/resources/audio/subresources/transcriptions), but also includes two **offline** backends so you can avoid network calls and API costs entirely. The CLI handles all of the boilerplate: it extracts audio from arbitrary input, normalises it, runs the transcription on your chosen engine and optionally renders a cleaned transcript with timestamps and speaker labels.

## Quick start

```bash
pip install otranscribe
export OPENAI_API_KEY="sk-..."
otranscribe -i audio.mp3
```

See [INSTALLATION.md](./docs/INSTALLATION.md) for detailed setup including offline engines.

## Features

- **Any input format** – as long as `ffmpeg` can read it, it can be transcribed.
- **Diarisation support** – by default it uses the `gpt-4o-transcribe-diarize` model and requests `diarized_json` output so that speakers are labelled. When you don't need diarisation or want to avoid API costs, you can select the local Whisper engine.
- **Clean rendering** – remove filler words, collapse whitespace and insert timestamps every N seconds and on speaker change.
- **Raw output** – choose `--render raw` to write the exact response from the engine (JSON, text, SRT, VTT, etc.).
- **Choice of engine** – use the OpenAI API (`--engine openai`) for high-quality diarised transcripts or choose one of the offline backends when you want to work without an internet connection:
  * **Local Whisper** (`--engine local`) – runs the reference [openai-whisper](https://github.com/openai/whisper) model on your machine. This backend produces accurate transcriptions but can be relatively slow on CPU and does not assign speaker labels.
  * **faster-whisper** (`--engine faster`) – uses the [faster-whisper](https://github.com/guillaumekln/faster-whisper) reimplementation based on CTranslate2. It is up to four times faster than the original open source Whisper implementation and uses less memory, with optional quantisation and GPU acceleration for even greater speed. Since diarisation is not available locally, the engine assigns all words to a single speaker (`Speaker 0`).
- **Minimal dependencies** – uses `requests` instead of the heavy `openai` client when talking to the API. The local engine only imports Whisper if you choose `--engine local`. The faster engine pulls in the `faster-whisper` package only when selected.

## Documentation

- [**INSTALLATION.md**](./docs/INSTALLATION.md) – Install, uninstall, and API key setup
- [**USAGE.md**](./docs/USAGE.md) – How to use `otranscribe`, examples, and common workflows
- [**TROUBLESHOOTING.md**](./docs/TROUBLESHOOTING.md) – Common errors, diagnostics, and solutions
- [**DEVELOPMENT.md**](./docs/DEVELOPMENT.md) – Development setup, testing, formatting, and linting
- [**CONTRIBUTING.md**](./docs/CONTRIBUTING.md) – PR workflow and contribution guidelines
- [**PUBLISHING.md**](./docs/PUBLISHING.md) – Release workflow and PyPI publishing

## Demo
![Demo: installing otranscribe](demos/otranscribe-install.gif)

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for PR workflow and [DEVELOPMENT.md](./docs/DEVELOPMENT.md) for setup instructions.

## Maintenance

This project is maintained by Ines. For governance, branch protection rules, and release workflow, see [MAINTAINERS.md](./docs/MAINTAINERS.md).

## License

Released under the terms of the MIT license. See `LICENSE` for details.
