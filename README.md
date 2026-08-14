# AgentProof Demo

This repository is a small Python project used to exercise AgentProof against a real external repository. The scenarios are intentionally simple so a pull request can demonstrate both a genuine fix and integrity violations.

## Verification workflow

The workflow runs the published v0.2.0rc2 Action from the AgentProof repository. The original AP001/AP002 receipts were also exercised against immutable v0.2.0rc1 before the metadata correction:

```yaml
uses: GenRamzi/AgentProof@v0.2.0rc2
with:
  test-command: python -m pytest -q
  policy-preset: strict
  auto-proof: true
```

After stable release, the reference should be updated to `GenRamzi/AgentProof@v0.2.0` or a full commit SHA.

## Planned PR scenarios

| Scenario | Expected result |
|---|---|
| Genuine calculator fix | `BASE FAIL → HEAD PASS`, `PROVEN` |
| Delete a regression test | `BLOCKED AP001` |
| Add a skip marker | `BLOCKED AP002` |
| Narrow CI discovery | `BLOCKED AP102/AP103` |
| Fake regression test | `INCONCLUSIVE AP201` |

The scenarios are documented here before opening PRs so the external test target remains auditable and does not contain hidden behavior. No secrets are required by the workflow.
