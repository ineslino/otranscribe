# Maintainers

This document describes the repository governance and the GitHub settings that enforce it.

## Goals

- `main` is protected: changes must go through Pull Requests.
- CI must pass before merging.
- PR authors cannot approve their own PRs (GitHub restriction in this repo), so we do not rely on “required approvals” for solo maintenance.

## Current enforcement model

### Branch protection: `main`

Enabled (expected):

- Require a pull request before merging
- Require status checks to pass before merging
- (Optional but recommended) Require conversation resolution before merging
- Lock branch: OFF (never enable unless you intentionally want read-only)

Not used (by design):

- Required approvals: OFF
  - Reason: GitHub blocks PR authors from approving their own PRs. In a solo-maintainer repo this creates deadlocks.
- Require Code Owners approval: OFF when approvals are OFF

### Merge authority

On personal repositories, GitHub may not expose “Restrict who can push” in branch protection.
In that case, merge authority is controlled by **repo permissions**:

- Only maintainers/collaborators with **Write/Maintain/Admin** can merge PRs.
- External contributors can still open PRs from forks, but cannot merge.

To allow a trusted person to merge:
- Repo Settings → Collaborators and teams → Add collaborator → grant **Write** (or **Maintain**).

## Required status checks (how to set them)

GitHub only allows selecting “Required status checks” after a check has run at least once.

Workflow expectation:
- A CI workflow runs on `pull_request` and defines checks like:
  - `pre-commit`
  - `tests (pytest)`

After the workflow runs:
- Settings → Branches → Branch protection rule → enable “Require status checks”
- Select the checks to require.

## Release workflow

Publishing is handled via GitHub Actions (tags). See:
- [PUBLISHING.md](./docs/PUBLISHING.md)

## Operational tips

- Prefer merging via squash merge for a clean history.
- If a PR is blocked by missing checks, verify the CI workflow triggers on `pull_request`.
- If you accidentally lock the branch, disable “Lock branch” in branch protection immediately.
