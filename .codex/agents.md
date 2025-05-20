# Codex Agent Instructions

These instructions are for Python or TypeScript projects. The agent should run tests and linters whenever source code changes.

## When to Run Tests and Linters
- Run `flake8` and `pytest` if any `.py` files change.
- Run `npm run lint` and `npm test` if any `.ts` or `.js` files change.
- Skip tests and linters when commits only modify comments or documentation files (e.g., `.md`, `.rst`, or comments in code).

## Python Conventions
- Format Python code with `black`.
- Use `snake_case` for variables and functions.

## TypeScript Conventions
- Format TypeScript code with `prettier` using the repo's config.
- Use `camelCase` for variables and functions.

## Memory and Project Planning
- Keep a running history of context and instructions in `memory.md` at the repo root.
- Track each task and its status in `project-plan.md` using a table or list with TODO/DOING/DONE states.
- Update these files whenever the agent gains new context or completes an action.

## Pull Request Summary
- Summarize the main changes and reference files with markdown code blocks.
- Mention test results and linters in the PR description.
