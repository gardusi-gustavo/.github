# Tasks

| Task | Schedule | Target |
| --- | --- | --- |
| `tasks/lottery` | daily | `database-lottery` |
| `tasks/news` | hourly | `database-news` |
| `tasks/stocks` | market close | `database-stocks` |

Each task runs with only its target database token. Cross-domain access is not
allowed.
