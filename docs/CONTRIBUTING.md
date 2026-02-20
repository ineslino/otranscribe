# Contributing

Thanks for contributing! This repo uses a PR-only workflow.

## Quick rules

- Do **not** push to `main`. Direct updates to `main` are blocked by branch protection.
- Open a Pull Request from:
  - a feature branch (if you have write access), or
  - a fork (most common for external contributors).
- CI must pass before a PR can be merged.

## Branch naming (recommended)

Use one of:

- `feat/<short-description>`
- `fix/<short-description>`
- `docs/<short-description>`
- `chore/<short-description>`
- `ci/<short-description>`
- `refactor/<short-description>`

Examples:

- `feat/add-speaker-map`
- `fix/doctor-cache-import`
- `docs/update-installation`

## Local development

See [DEVELOPMENT.md](./docs/DEVELOPMENT.md).

## Running checks

```bash
pre-commit run --all-files
pytest
```

### If pre-commit is not found

Install dev dependencies:

```bash
pip install -e ".[dev]"
```

Then run:

```bash
pre-commit run --all-files
```

Alternatively, run via Python:

```bash
python -m pre_commit run --all-files
```
