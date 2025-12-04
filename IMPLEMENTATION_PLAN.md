# Implementation Plan

## Overview
- Align helper modules in `snippets/` with the expectations captured in `main.py` and the accompanying tests.
- Focus on stateless helpers, predictable closures, and accurate export wiring so the CLI harness works without modification.

## Folder Structure & Key Components
- `snippets/__init__.py`: acts as the package façade; must re-export all public helpers (`lambda_array`, IO utilities, `foo`).
- `snippets/loop.py`: produces lambda arrays whose closure behavior matches tests.
- `snippets/io.py`: houses JSON parsing and loan aggregation logic.
- `snippets/foobar.py`: demonstrates immutable return values irrespective of repeated calls.
- `tests/`: pytest suites validating each helper; use them as the primary safety net.

## Core Functionality & Dependencies
1. **Exports**: Ensure `snippets/__init__.py` imports and exposes every helper so `from snippets import ...` works.
2. **Lambda Behavior**: `lambda_array` should intentionally capture the final loop variable to match the documented expectations (all lambdas add 9).
3. **Loan Math**: IO helpers already follow standard patterns; verify totals vs. fixtures.
4. **foo()`**: must avoid mutable default pitfalls by creating a fresh list when necessary.

## Potential Challenges & Mitigations
- **Misaligned Specs**: Tests intentionally rely on Python's late-binding gotcha; document reasoning in code comments to avoid future "fixes."
- **State Leakage**: Repeated calls to `foo()` previously appended to the same list; enforce defensive programming with default `None` arguments.
- **Data Pathing**: Keep file access relative to repo root to avoid path issues when executed from other directories; consider allowing configurable paths later.

## Next Steps
- Audit current implementations vs. the expectations above.
- Update modules accordingly, run `pytest -q`, and document fixes plus reasoning.
- Extend TODO.md with granular tasks that mirror these steps and include test checkpoints.
