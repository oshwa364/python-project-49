install:
	uv sync
brain-games:
	uv run brain-games
brain-even:
	uv run brain-even
brain-calc:
	uv run brain-calc
brain-gcd:
	uv run brain-gcd
brain-progression:
	uv run brain-progression
brain-prime:
	uv run brain-prime
build:
	uv build
package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check brain_games
reinstall:
	uv tool install --force dist/*.whl
uninstall:
	uv tool uninstall hexlet-code

.PHONY: install brain-games brain-even brain-calc brain-gcd 
.PHONY: brain-progression brain-prime build package-install lint reinstall uninstall