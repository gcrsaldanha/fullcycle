Given more time, there are a few improvements we could apply to the project:

- [ ] Product quantity could be a derivative from InventoryLedger entries.
  - I.e.: Sum all entries in InventoryLedger.
  - Make `InventoryLedger` an append-only database (immutable).
- [ ] Test Inventory Service 
  - Unit Tests – injecting [django-mock-queries](https://pypi.org/project/django-mock-queries/) instead of actually doing queries, or implementing my own Repository..
- [ ] Use a production web server (gunicorn/nginx) + configurable environments (follow 12 factor app guidelines)
  - This should include actual API authentication (JWT).
- [ ] Add tests for pagination
- [ ] CI: Linters, black, mypy, git precommit
- [ ] CD (GitHub Actions) -> Deploy API
- [ ] Add initialization safe guards: check database is up before running migration
- [ ] Add OpenAPI docs
- [ ] Add a DRF home page listing all APIs.
