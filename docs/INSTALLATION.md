# Installation

## Prerequisites

Before installing `otranscribe` you need:

- **Python 3.9+** – the code is tested with 3.9 and newer.
- **ffmpeg** – used to extract audio from videos and normalise input. You must install this separately and ensure the `ffmpeg` binary is on your `PATH`.
- **Requests** – installed automatically via package dependencies.
- **OpenAI API key** – only required when using the OpenAI engine.

Optional backends:
- **openai-whisper** – required only if you plan to use the local engine.
- **faster-whisper** – required only if you plan to use the faster engine (depends on [CTranslate2](https://github.com/OpenNMT/CTranslate2); can leverage GPU).

### Installing ffmpeg

`otranscribe` relies on the external `ffmpeg` program. Install via your operating system:

- **macOS**: `brew install ffmpeg`
- **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
- **Windows**: Install via [Chocolatey](https://chocolatey.org/) (`choco install ffmpeg`) or download the static build from [ffmpeg.org](https://ffmpeg.org/) and add the `bin` directory to your `PATH`.

Verify: `ffmpeg -version`

## Install otranscribe

### Option A: From PyPI (core + OpenAI API only)

```bash
# install globally using pipx (recommended)
pipx install otranscribe

# or install into the current environment
pip install otranscribe

# with local Whisper engine
pip install otranscribe[local]

# with faster-whisper engine
pip install otranscribe[faster]

# with both offline engines
pip install otranscribe[local,faster]
```

### Option B: From source (recommended for development)

```bash
git clone <repo-url>
cd otranscribe
python3 -m venv .venv
source .venv/bin/activate  # on Windows: .\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -e .
```

With optional engines:

```bash
pip install -e ".[local]"       # local Whisper
pip install -e ".[faster]"      # faster-whisper
pip install -e ".[dev]"         # development (pytest, linting, etc.)
pip install -e ".[local,faster,dev]"  # all
```

### Option C: Requirements files (source only)

```bash
git clone <repo-url>
cd otranscribe
python3 -m venv .venv
source .venv/bin/activate

pip install -U pip
pip install -r requirements.txt        # core
pip install -r requirements-local.txt  # optional: local engine
pip install -r requirements-faster.txt # optional: faster engine
pip install -e .
```

### Verify installation

```bash
which otranscribe          # or: where otranscribe (Windows)
otranscribe --help
python -c "import otranscribe; print(otranscribe.__file__)"
```

If `otranscribe` is not found:
- Make sure your virtualenv is active: `source .venv/bin/activate`
- Reinstall: `pip install -e .`

## Set your OpenAI API key

When using the OpenAI engine, set the `OPENAI_API_KEY` environment variable:

```bash
export OPENAI_API_KEY="sk-..."
```

On Windows (PowerShell):

```powershell
$env:OPENAI_API_KEY="sk-..."
```

> The local and faster engines (`--engine local` and `--engine faster`) do not require this variable.

## Hugging Face token (optional)

Offline engines download models from Hugging Face Hub on first run. This works without authentication, but setting a token suppresses warnings and enables faster downloads:
```bash
export HF_TOKEN="hf_..."
```

On Windows (PowerShell):
```powershell
$env:HF_TOKEN="hf_..."
```

Get a free token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

## Uninstall

### From PyPI/pipx

```bash
pipx uninstall otranscribe
# or
pip uninstall otranscribe
```

### From source

```bash
# deactivate virtualenv
deactivate

# remove the project directory
rm -rf /path/to/otranscribe
```

---

## Development

For development setup, testing, formatting, linting, and pre-commit configuration, see [DEVELOPMENT.md](./docs/DEVELOPMENT.md).

To contribute, see [CONTRIBUTING.md](./docs/CONTRIBUTING.md).
