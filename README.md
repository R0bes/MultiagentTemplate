# MultiagentTemplate

This repository provides a starting point for building Codex-powered multi-agent projects. It is meant to be forked and customized for your own application. The template helps you coordinate multiple agents that work in parallel on a shared codebase.

## Getting Started

1. **Fork** this repository.
2. Fill in `project-intent.md` with a short description of your project, the desired architecture, and the main modules you need.
3. Start the initial agent using the instructions in `agents/InitAgent.md`. This agent focuses on planning the architecture, scaffolding the repository, and creating task files for additional agents. It will always include a final **Cleanup** task and may delegate extra planning agents if the project scope is large.
4. Agents collaborate by following the tasks defined in `agents.md` and contribute code in the appropriate folders under `src/`.

## Repository Layout

- `agents/` – Individual agent instruction files.
- `src/core/` – Core framework code shared across modules.
- `src/modules/` – Project-specific modules.
- `src/utils/` – Utility functions used across the codebase.
- `tests/` – Unit and integration tests.
- `templates/` – Optional project templates.
- `scripts/` – Helper scripts such as environment setup.

## Usage

After you have filled out `project-intent.md`, run the setup script:

```bash
bash scripts/start.sh
```

This installs dependencies and prints instructions for launching your first agent.

Agents coordinate tasks using `agents.md`. Each agent writes to a dedicated instruction file under `agents/` and commits code only within its assigned module.

## Contributing

See `CONTRIBUTING.md` for guidelines on how agents should contribute to this project.


