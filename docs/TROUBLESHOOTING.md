# Troubleshooting

## Run diagnostics

`otranscribe` includes built-in diagnostics to check your setup:

```bash
# full diagnostic
otranscribe doctor

# check specific engine
otranscribe doctor --engine openai
otranscribe doctor --engine local
otranscribe doctor --engine faster
```

The `doctor` command:
- Checks Python version
- Verifies `ffmpeg` is installed
- Checks for required and optional dependencies per engine
- Exits with non-zero code if critical dependencies are missing

Non-blocking check with Make:

```bash
make doctor      # print what is missing (don't fail)
make doctor-openai
make doctor-local
make doctor-faster
```

---

## Common issues

### `otranscribe: command not found`

**Problem**: The CLI is not in your `PATH`.

**Solution**:
- Activate your virtualenv: `source .venv/bin/activate`
- Or reinstall from the repo root: `pip install -e .`
- Verify: `which otranscribe`

If using `pipx`, ensure `~/.local/bin` is in your `PATH`:

```bash
echo $PATH | grep .local/bin
# if not found, add to ~/.bashrc, ~/.zshrc, or equivalent:
export PATH="$HOME/.local/bin:$PATH"
```

### `ffmpeg: command not found`

**Problem**: `ffmpeg` is not installed or not on your `PATH`.

**Solution**:
- Install ffmpeg (see [INSTALLATION.md](./INSTALLATION.md#installing-ffmpeg))
- Verify: `ffmpeg -version`

### `OPENAI_API_KEY not set` or API authentication fails

**Problem**: The OpenAI engine can't authenticate with the API.

**Solution**:
- Set your API key: `export OPENAI_API_KEY="sk-..."`
- Verify: `echo $OPENAI_API_KEY` (should print your key)
- On Windows PowerShell: `$env:OPENAI_API_KEY="sk-..."`
- Check your key is valid at [openai.com/api/keys](https://openai.com/api/keys)
- Make sure you have API credits available

### `ModuleNotFoundError: No module named 'whisper'`

**Problem**: The local Whisper engine is not installed.

**Solution**:
- Install: `pip install -e ".[local]"`
- Or: `pip install openai-whisper`

### `ModuleNotFoundError: No module named 'faster_whisper'`

**Problem**: The faster-whisper engine is not installed.

**Solution**:
- Install: `pip install -e ".[faster]"`
- Or: `pip install faster-whisper`
- For GPU support, follow [faster-whisper's installation guide](https://github.com/guillaumekln/faster-whisper)

### `Error reading input file: ffmpeg exited with code X`

**Problem**: `ffmpeg` failed to process your audio/video file.

**Common causes**:
- File format not supported
- File is corrupted
- Insufficient disk space
- Audio codec issues

**Solution**:
- Verify the file exists: `ls -lh input.mp3`
- Test ffmpeg directly: `ffmpeg -i input.mp3 -f null -` (should output duration)
- Try converting to a standard format first:
  ```bash
  ffmpeg -i input.m4v -acodec aac -ar 16000 -ac 1 output.wav
  otranscribe -i output.wav
  ```
- Check `ffmpeg -codecs` for supported formats

### Output file is empty or incomplete

**Problem**: Transcription ran but produced no output.

**Possible causes**:
- Audio was silent or very short
- Wrong engine selected (no speakers detected, etc.)
- API rate limit hit (OpenAI)

**Solution**:
- Check raw output: `otranscribe -i input.mp3 --render raw -o raw.json`
- Inspect the JSON to see what the engine returned
- For OpenAI: check your API usage at [openai.com/account/billing](https://openai.com/account/billing)
- Run diagnostics: `otranscribe doctor --engine openai`

### Timestamps are wrong or missing

**Problem**: Output has no timestamps or they're inaccurate.

**Solution**:
- Only the clean render includes timestamps. Use default render: `otranscribe -i audio.mp3`
- Adjust frequency: `otranscribe -i audio.mp3 --every 10` (insert every 10 seconds)
- Raw output doesn't include cleaned timestamps: `--render raw` skips timestamp insertion

### Performance is slow (local or faster-whisper)

**Problem**: Transcription takes too long.

**For local Whisper**:
- Use a smaller model: `--whisper-model tiny` or `--whisper-model small`
- Local Whisper is slower on CPU. Install CUDA for GPU acceleration if possible.

**For faster-whisper**:
- Use smaller model: `--faster-model tiny` or `--faster-model small`
- Enable GPU: `--faster-device cuda --faster-compute-type float16`
- Enable quantisation: `--faster-compute-type int8` (trades quality for speed)

**For OpenAI**:
- API should be fast. If slow, check your network connection and API status.

### Diarisation (speaker labels) is not working

**Problem**: Output doesn't have speaker labels or says "Speaker 0" for everyone.

**Reason**:
- Local Whisper and faster-whisper don't support diarisation
- OpenAI API does (with `gpt-4o-transcribe-diarize` model)

**Solution**:
- Use the OpenAI engine: `otranscribe -i audio.mp3 --engine openai`
- If using OpenAI already, ensure you're using the diarised model:
  ```bash
  otranscribe -i audio.mp3 --engine openai --api-format diarized_json
  ```

### Pre-commit hooks are blocking commits

**Problem**: `git commit` fails with formatting or linting errors.

**Solution**:
- Run fixes locally:
  ```bash
  pre-commit run --all-files
  black .
  ruff check --fix .
  ```
- Then commit again: `git commit`
- To skip hooks temporarily (not recommended):
  ```bash
  git commit --no-verify
  ```

### Line ending issues (`CRLF` vs `LF`)

**Problem**: Files show as modified after cloning or formatting.

**Solution**:
- The repo uses `.gitattributes` to enforce LF (Unix line endings)
- Pre-commit normalizes line endings automatically
- If needed manually:
  ```bash
  git config core.autocrlf false
  pre-commit run --all-files
  ```

---

## Getting more help

1. Run `otranscribe doctor` and paste the output
2. Include your Python version: `python --version`
3. Include your `ffmpeg` version: `ffmpeg -version`
4. Include the exact command you ran
5. Include the full error message (not just the last line)
6. Open an issue on the project repository

## Development troubleshooting

### Tests fail

```bash
pip install -e ".[dev]"
pytest -v
```

Check that all dev dependencies are installed.

### Import errors during development

```bash
# reinstall in editable mode
pip install -e . --force-reinstall --no-deps
```

### Make targets don't work

```bash
# install Make if missing
# macOS: brew install make
# Ubuntu: sudo apt-get install make
# Windows: use WSL or run commands manually (see make targets in Makefile)
```

### Hugging Face authentication warning

When using offline engines (`--engine local` or `--engine faster`), you may see:
```
Warning: You are sending unauthenticated requests to the HF Hub.
```

This is harmless — models download without authentication. To suppress it and get faster downloads, create a free token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) and set:
```bash
export HF_TOKEN="hf_..."
```