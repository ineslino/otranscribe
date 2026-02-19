# Publishing

This project uses **GitHub Actions + Trusted Publishing (OIDC)** to publish releases to PyPI and TestPyPI.

**Do not publish from your local machine.** All releases go through GitHub Actions.

## Prerequisites

- You must be a maintainer of the project repo
- Trusted Publishing must be configured in:
  - **PyPI** for this GitHub repo/workflow
  - **TestPyPI** for this GitHub repo/workflow
- The workflow file `.github/workflows/publish.yml` must exist on the commit you tag

## Versioning

Publishing is triggered by pushing a git tag starting with `v`.

**Two tag types:**

### Test releases (TestPyPI only)
Use release candidate tags with `rc`:

```
v0.1.1-rc.1
v0.1.1-rc.2
v1.0.0-rc.1
```

### Final releases (PyPI only)
Use final tags without `rc`:

```
v0.1.1
v0.2.0
v1.0.0
```

## Release workflow

### 1. Prepare main branch

Ensure `main` is ready:

```bash
git checkout main
git pull
git log -1 --oneline
```

Verify the workflow file exists:

```bash
ls .github/workflows/publish.yml
```

### 2. Update version

Update the version in your version source (typically `pyproject.toml` or `otranscribe/__init__.py`):

```toml
[project]
version = "0.2.0"
```

Commit:

```bash
git add pyproject.toml
git commit -m "bump: version 0.2.0"
git push
```

### 3. Tag the release

For a final release:

```bash
git tag -a v0.2.0 -m "Release 0.2.0"
git push origin v0.2.0
```

For a test release:

```bash
git tag -a v0.2.0-rc.1 -m "Release candidate 0.2.0-rc.1"
git push origin v0.2.0-rc.1
```

### 4. Monitor the workflow

Go to your GitHub repo → **Actions** tab. You should see the publish workflow running.

- **Test release** (`*-rc.*`): publishes to TestPyPI
- **Final release** (no `rc`): publishes to PyPI

Check the workflow logs for errors. If it fails, fix and re-tag (increment the `rc` number or create a new final tag).

### 5. Verify the release

**For TestPyPI:**

```bash
pip install -i https://test.pypi.org/simple/ otranscribe==0.2.0rc1
```

**For PyPI:**

```bash
pip install --upgrade otranscribe
```

Check the package page:
- TestPyPI: https://test.pypi.org/project/otranscribe/
- PyPI: https://pypi.org/project/otranscribe/

## Troubleshooting

### Workflow didn't trigger

- Tag must start with `v` (e.g., `v0.2.0`, not `0.2.0`)
- `.github/workflows/publish.yml` must exist on the tagged commit
- Check GitHub Actions logs for errors

### TestPyPI and PyPI both published

- You tagged with `rc` but it published to PyPI (shouldn't happen)
- Check the workflow logic in `.github/workflows/publish.yml`

### Need to re-publish the same version

- You can't re-push the same tag
- Create a new `rc` tag and test again, or bump to the next version

### Forgot to update version number

- Delete the tag locally and remotely, fix version, and retag:
  ```bash
  git tag -d v0.2.0
  git push origin :refs/tags/v0.2.0
  # fix version
  git tag -a v0.2.0 -m "Release 0.2.0"
  git push origin v0.2.0
  ```

## Notes

- **Trusted Publishing (OIDC)**: GitHub Actions authenticates with PyPI/TestPyPI without storing API keys. Credentials are short-lived and tied to the workflow run.
- **No local publishing**: Never generate and upload distributions manually. Always use the GitHub Actions workflow.
- **Pre-release workflow**: Test releases on TestPyPI first. Install and verify before publishing to PyPI.
