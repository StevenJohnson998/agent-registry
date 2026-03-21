> ⏸️ **PROJECT STATUS: ON HOLD**  
> This project is paused while the maintainer focuses on other priorities.  
> The architecture and design docs remain available for review and feedback.  
> Contributions are welcome but may not be reviewed immediately.
> 
# AgentLedger

> **The Trust & Privacy Layer for the Agentic Ecosystem.**

[![License](https://img.shields.io/badge/License-AGPL_3.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Status](https://img.shields.io/badge/Status-Alpha-orange.svg)](#project-status)
[![ADHP](https://img.shields.io/badge/ADHP-v0.1_Draft-purple.svg)](docs/ADHP-SPEC.md)

## The Problem

AI agents are multiplying. An orchestrator handling a financial analysis task might have 50 agents to choose from — but no good way to decide:

- **Which agent is the best for this specific task?** Not a generic rating — proven quality at *this* capability.
- **What will it do with my data?** Will it train on it? Store it? Forward it to a third party?
- **Is it compliant with the regulations I care about?** GDPR, HIPAA, POPIA, CCPA — can I filter by that?
- **Who's behind this agent?** Is there a verified, accountable organization operating it?
- **What's the most cost-effective option** at the trust level I need?
- **If it delegates to another agent, will the privacy and compliance chain hold?**

Today, registries catalog agents. None of them answer these questions. **AgentLedger** is an open-source trust layer that does. We don't replace [MCP](https://modelcontextprotocol.io/) or [A2A](https://a2a-protocol.org/) — we complement them. MCP connects agents to tools. A2A lets agents talk to each other. **We help agents decide *who* to trust.**

---

## What We're Building

### 1. Agent Data Handling Policy (ADHP)

A standardized way for agents to declare what happens to your data — and for orchestrators to filter agents based on those declarations.

Five levels, from `open` (no guarantees) to `zero-trace` (streaming only, no storage, no logs, no delegation):

| Level | Training | Persistence | Logging | Delegation | Third-Party Sharing |
|-------|----------|-------------|---------|------------|---------------------|
| **open** | Yes | Unlimited | Full | Unrestricted | Allowed |
| **standard** | No | Session | Metadata only | Same level+ | With consent |
| **sensitive** | No | Request only | Metadata only | Declared only | Anonymized only |
| **strict** | No | Request only | None | Same level+ | Not allowed |
| **zero-trace** | No | None | None | None | Not allowed |

**Key innovation: Delegation Cascading.** When Agent A delegates to Agent B, the data handling level must be maintained or strengthened — never weakened. The registry validates the entire chain.

**Privacy legislation compliance tags.** Agents declare which regulations they comply with — `GDPR`, `HIPAA`, `CCPA`, `POPIA`, `PIPEDA`, `LGPD`, and others. Orchestrators filter by regulation: *"find me an agent compliant with GDPR and HIPAA that handles data at strict level."*

📄 [Full ADHP Specification](docs/ADHP-SPEC.md)

### 2. Operator Verification (KYC)

Trust requires accountability. We verify the organizations behind agents through tiered verification:

| Tier | What's Verified | Badge |
|------|----------------|-------|
| Unverified | Nothing — self-registered | — |
| Email-verified | Valid email confirmed | ✉️ |
| Identity-verified | Legal identity confirmed via documents | ✅ |
| Audited | Identity + technical ADHP compliance audit | 🛡️ |

Orchestrators can combine filters: *"find me an agent with ADHP ≥ sensitive AND verification ≥ identity-verified."*

📄 [Full KYC Specification](docs/KYC-SPEC.md)

### 3. Per-Capability Trust Scoring

A flat rating is useless. An agent might be excellent at financial analysis but poor at creative writing. Our registry stores **contextual trust maps** — quality and confidence scores per capability.

```
GET /agents?capability=financial-analysis&min_quality=4.0&adhp_level=strict&jurisdiction=EU&compliance=GDPR
```

---

## How It Fits In the Ecosystem

We're not competing with existing projects — we're filling a gap that none of them address:

```
┌─────────────────────────────────────────────────────┐
│                   Agentic Ecosystem                  │
│                                                      │
│  MCP Registry ─── catalogs servers/tools             │
│  A2A Protocol ─── agents discover & talk to agents   │
│  Kong/Solo.io ─── enterprise gateway & governance    │
│                                                      │
│  AgentLedger ───── WHO DO I TRUST? ◄── you are here │
│    ├── ADHP: what happens to my data?                │
│    ├── Compliance: GDPR, HIPAA, CCPA, POPIA...      │
│    ├── KYC: who's behind this agent?                 │
│    ├── Trust scores: is it good at THIS task?        │
│    └── Delegation chains: will trust hold?           │
└─────────────────────────────────────────────────────┘
```

We plan to **federate with the official MCP Registry** — pulling server metadata and adding our trust layer on top. We support both MCP and A2A protocols. We're compatible with AAIF standards.

---

## Project Status

**Alpha MVP** — working registry with REST API, PostgreSQL storage, API key auth, rate limiting, search with filtering, web dashboard, and Docker deployment. 47 tests, 84% coverage.

| Component | Status |
|-----------|--------|
| REST API (FastAPI) | ✅ Working |
| Agent CRUD + search | ✅ Working |
| ADHP fields + filtering | ✅ Working |
| API key auth (writes) | ✅ Working |
| Rate limiting (Redis) | ✅ Working |
| Web dashboard | ✅ Working |
| Docker deployment | ✅ Working |
| ADHP Specification | 📄 v0.1 Draft |
| KYC Specification | 📄 v0.1 Draft |
| Operator system | 🔨 Next |
| Public deployment | 🔨 Next |

See the [Roadmap](docs/ROADMAP.md) for what's coming.

---

## Quick Start

```bash
# Clone
git clone https://github.com/StevenJohnson998/AgentLedger.git
cd AgentLedger

# Start (requires Docker)
./batch/run-dev.sh

# API available at http://localhost:8000
# Dashboard at http://localhost:8000/dashboard
# Docs at http://localhost:8000/docs

# Run tests
./batch/run-tests.sh

# Seed example agents
./batch/seed-db.sh
```

### Register an Agent

```bash
curl -X POST http://localhost:8000/agents \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "FinanceAnalyzer Pro",
    "description": "Financial document analysis with strict privacy",
    "capabilities": ["financial-analysis", "document-parsing"],
    "endpoint": "https://api.finanalyzer.example.com",
    "protocol": "REST",
    "data_handling": {
      "level": "strict",
      "training_opt_out": true,
      "max_retention": "request",
      "content_logging": false,
      "delegation_policy": "same_or_higher",
      "jurisdiction": ["DE", "FR"],
      "compliance": ["GDPR"],
      "third_party_sharing": { "enabled": false }
    }
  }'
```

### Find Agents by Trust Requirements

```bash
# Find strict+ agents in the EU, GDPR-compliant, that don't share data
curl "http://localhost:8000/agents?min_data_handling_level=strict&jurisdiction=EU&compliance=GDPR&third_party_sharing=false"
```

---

## Repository Structure

```
AgentLedger/
├── docs/                    # Specifications
│   ├── ADHP-SPEC.md         # Agent Data Handling Policy specification
│   ├── KYC-SPEC.md          # Operator verification specification
│   └── ROADMAP.md           # Project roadmap
├── dev/                     # Application source code
│   ├── app/                 # FastAPI application
│   │   ├── api/             # API routes
│   │   ├── core/            # Config, auth, rate limiting
│   │   ├── models/          # SQLAlchemy models
│   │   └── schemas/         # Pydantic schemas
│   ├── tests/               # Test suite
│   ├── alembic/             # Database migrations
│   ├── static/              # Web dashboard
│   └── docker-compose.dev.yml
├── batch/                   # Operational scripts
│   ├── run-dev.sh
│   ├── stop-dev.sh
│   ├── run-tests.sh
│   ├── seed-db.sh
│   └── ...
└── notes/                   # Internal project notes
```

---

## Contributing

We're especially looking for feedback on:

- **ADHP Specification** — Are the five levels right? What data handling concerns are we missing?
- **Ecosystem integration** — How should we best work with MCP and A2A?
- **Real-world testing** — Do you operate agents? We'd love to register them and test our assumptions.

### How to Contribute

1. Read the [ADHP Spec](docs/ADHP-SPEC.md) and [KYC Spec](docs/KYC-SPEC.md)
2. Open an Issue or Discussion with your feedback
3. Submit PRs for code or spec improvements

All contributions are welcome, from spec feedback to code to documentation.

---

## License

Apache 2.0 — see [LICENSE](LICENSE).

---

## Links

- [ADHP Specification](docs/ADHP-SPEC.md)
- [KYC Specification](docs/KYC-SPEC.md)
- [Roadmap](docs/ROADMAP.md)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [A2A Protocol](https://a2a-protocol.org/)
- [AAIF](https://aaif.io/)
