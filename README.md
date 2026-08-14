# AgentProof Demo

This repository is a small Python project used to exercise AgentProof against a real external repository. The scenarios are intentionally simple so a pull request can demonstrate both a genuine fix and integrity violations.

## Verification workflow

The workflow runs the development-channel Action from the AgentProof repository until the first release candidate exists:

```yaml
uses: GenRamzi/AgentProof@main
with:
  test-command: python -m pytest -q
  policy-preset: strict
  auto-proof: true
```

After `v0.2.0rc1` is published, the reference should be changed to `GenRamzi/AgentProof@v0.2.0rc1`. After stable release it should be pinned to `GenRamzi/AgentProof@v0.2.0`.

## Planned PR scenarios

| Scenario | Expected result |
|---|---|
| Genuine calculator fix | `BASE FAIL → HEAD PASS`, `PROVEN` |
| Delete a regression test | `BLOCKED AP001` |
| Add a skip marker | `BLOCKED AP002` |
| Narrow CI discovery | `BLOCKED AP102/AP103` |
| Fake regression test | `INCONCLUSIVE AP201` |

The scenarios are documented here before opening PRs so the external test target remains auditable and does not contain hidden behavior. No secrets are required by the workflow.
