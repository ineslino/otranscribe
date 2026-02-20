# `otranscribe` CLI Reference

```
otranscribe [-h] {doctor,transcribe} ...
```

## Subcommands

| Subcommand | Description |
|------------|-------------|
| `transcribe` | Transcribe audio/video file |
| `doctor` | Check environment and dependencies |

---

## `otranscribe transcribe`

### Input / Output

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--input` | `-i` | *(required)* | Input file (audio or video). Any ffmpeg-supported format |
| `--out` | `-o` | auto | Output path. Defaults to `<input>.<ext>` |
| `--out-format` | | `txt` | Output format for final render: `txt`, `md` |
| `--md-style` | | `simple` | Markdown style when `--out-format md`: `simple`, `meeting` |
| `--keep-temp` | | `false` | Keep temp WAV and intermediate artifacts |
| `--temp-dir` | | system default | Custom temp directory |

### Engine

| Flag | Default | Description |
|------|---------|-------------|
| `--engine` | `openai` | Transcription engine: `openai`, `local`, `faster` |
| `--model` | *(OpenAI default)* | OpenAI transcription model |
| `--language` | auto | Language code, e.g. `pt`, `en`, `es` |
| `--api-format` | `diarized_json` | API response format: `diarized_json`, `json`, `srt`, `text`, `verbose_json`, `vtt` |
| `--chunking` | | OpenAI chunking strategy (recommended: `auto` for long audio) |

### Local / Faster-Whisper Engine

| Flag | Default | Description |
|------|---------|-------------|
| `--whisper-model` | | Whisper model size: `tiny`, `base`, `small`, `medium`, `large` |
| `--faster-model` | | faster-whisper model size/name |
| `--faster-device` | `auto` | Device: `auto`, `cpu`, `cuda` |
| `--faster-compute-type` | `int8` | Compute type: `int8`, `float16`, `float32` |
| `--chunk-seconds` | | Offline chunk duration in seconds (0 disables) |
| `--chunk-overlap-seconds` | | Offline chunk overlap in seconds (0 disables) |

### Rendering

| Flag | Default | Description |
|------|---------|-------------|
| `--render` | `final` | `raw` = write engine output as-is; `final` = cleaned transcript with timestamps + speakers |
| `--every` | `30` | Timestamp bucket in seconds for final render |
| `--speaker-map` | | Path to JSON speaker map, e.g. `{"Speaker 0": "Interviewer"}` |

### Cache

| Flag | Default | Description |
|------|---------|-------------|
| `--cache-dir` | | Cache directory for results |
| `--no-cache` | `false` | Disable caching |

---

## `otranscribe doctor`

| Flag | Default | Description |
|------|---------|-------------|
| `--engine` | *(all)* | Check only a specific engine: `openai`, `local`, `faster` |

Exits non-zero if required dependencies for the selected engine are missing.