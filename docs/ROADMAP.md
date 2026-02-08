# Agent Registry — Roadmap

> Last updated: February 2026

## Vision

Build the trust and privacy layer for the agentic ecosystem — where orchestrators discover and evaluate agents based on **data handling transparency**, **operator accountability**, and **per-capability trust**.

We complement [MCP](https://modelcontextprotocol.io/) and [A2A](https://a2a-protocol.org/) by answering: **who should I trust with my data?**

---

## Phase 1 — Trust Foundation (Current)

Core registry with ADHP, operator verification, and per-capability scoring.

### Completed ✅

| Feature | Description |
|---------|-------------|
| REST API (FastAPI) | Register, search, update, delete agents |
| PostgreSQL + JSONB | Persistent storage with flexible fields for future extension |
| ADHP fields | Agents declare data handling level (open → zero-trace) with full property set |
| ADHP search filters | Filter agents by minimum level, jurisdiction, third-party sharing policy |
| API key authentication | Write operations require API key, reads are public |
| Rate limiting (Redis) | Abuse prevention with graceful fallback |
| Keyword search | Search by name, description, capabilities |
| Web dashboard | Browse and search agents |
| Docker deployment | Containerized with Docker Compose on shared network |
| Unit tests | 47 tests, 84% coverage (pytest) |
| OpenAPI documentation | Auto-generated Swagger/ReDoc |
| Seed data | Example agents for demo |
| Database migrations | Alembic with versioned schema changes |
| Batch scripts | run-dev, stop-dev, run-tests, seed-db, status, view-logs |
| ADHP Specification v0.1 | [Full spec](ADHP-SPEC.md) — 5 levels, delegation cascading, third-party sharing matrix |
| KYC Specification v0.1 | [Full spec](KYC-SPEC.md) — 4 tiers, GDPR-compliant, operator data model |

### In Progress 🔨

| Feature | Description |
|---------|-------------|
| Operator system | `operators` table linked to agents, verification tiers |
| Admin CLI | Scripts for verification management, GDPR export/deletion |
| Per-capability scoring | Quality/confidence scores per capability (contextual trust maps) |
| Privacy compliance tags | Agents declare regulatory compliance: GDPR, HIPAA, CCPA, POPIA, etc. |
| Agent status | Active/suspended/deprecated status with admin control |
| Public deployment | Domain + HTTPS via Caddy |
| Actionable demo | Orchestrator simulation choosing agents based on ADHP requirements |

### Planned 📋

| Feature | Description |
|---------|-------------|
| Admin dashboard | Web UI for KYC review queue, operator management, audit log |
| Privacy policy page | Dashboard page covering GDPR rights for operators |
| MCP compatibility | Ensure agent schema is compatible with MCP server metadata |
| A2A Agent Card alignment | Ensure agent schema maps cleanly to A2A Agent Cards |
| Health checks & monitoring | Uptime monitoring, alerting |

---

## Phase 2 — Ecosystem Integration

Native protocol support, federation, and enhanced discovery.

| Feature | Description |
|---------|-------------|
| Federation with MCP Registry | Pull server metadata from official MCP registry, add trust layer |
| A2A protocol support | Support A2A Agent Cards for agent discovery |
| Semantic search | Embedding-based matching of orchestrator intent to agent capabilities |
| OpenAPI auto-registration | Paste an OpenAPI spec URL, auto-register as an agent |
| Usage observability | Track which agents are queried, how often, by whom |
| Delegation chain validation | Verify that sub-agents maintain required ADHP levels |
| Webhook notifications | Notify subscribers when matching agents are registered |
| KYC document management | Encrypted upload, admin review workflow, retention enforcement |
| GDPR automation | Data export, deletion endpoints, retention enforcement |

---

## Phase 3 — Verified Trust at Scale

Move from self-declaration to independently verified trust.

| Feature | Description |
|---------|-------------|
| Verified badge system | Organizations pay for KYC + ADHP compliance verification |
| Automated ADHP auditing | Auditor agents test registered agents with tracking markers |
| Reputation scoring | Aggregated trust scores based on usage, audits, and peer feedback |
| Blast radius tracking | Map agent dependency chains for risk assessment |
| Re-verification workflow | Expiry notifications, renewal process |
| Third-party KYC integration | Provider integration for scalable identity verification |

---

## ADHP as Standalone Standard

In parallel with the registry development, we are developing ADHP (Agent Data Handling Policy) as a **standalone open specification** that can be adopted independently:

- Publish as a separate repository with Apache 2.0 license
- Propose as an MCP Extension via the SEP process
- Seek adoption across the agentic ecosystem
- Engage with AAIF community

The registry is the reference implementation, but ADHP is designed to work with any registry or discovery system.

---

## Infrastructure

| Item | Status |
|------|--------|
| VPS (Hetzner CAX21 ARM64) | ✅ Running — Ubuntu 24.04, secured |
| Docker + shared services | ✅ Running — Caddy, PostgreSQL 16, Redis 7 |
| GitHub repo | ✅ Active — branch protection, secret scanning |
| CI/CD pipeline | 📋 Planned |
| Automated backups | 📋 Planned |
| Domain + HTTPS | 📋 Planned |
| Monitoring & alerting | 📋 Planned |
