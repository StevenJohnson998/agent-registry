# RFC 001: Micro-Agent Manifest Schema (Draft)

## Status
Draft / Request for Comments

## Context
Every agent must provide a manifest to be indexed by the registry. This manifest must be machine-readable (for the registry) and semantically rich (for the vector search).

## Proposed Structure (JSON)
{
  "manifest_version": "1.0.0",
  "agent_id": "urn:uuid:550e8400-e29b-41d4-a716-446655440000",
  "name": "FinanceGuard-Analyzer",
  
  "publisher": {
    "name": "Alpha Corp",
    "website": "[https://alpha-corp.ai](https://alpha-corp.ai)",
    "contact": "support-agents@alpha-corp.ai"
  },

  "verification": {
    "status": "verified",
    "method": "manual_review",
    "verified_at": "2026-02-05T10:00:00Z",
    "verified_by": "AgentRegistry_Core_Team",
    "claims": {
      "mcp_compliance": true,
      "identity_verified": true
    }
  },

  "interfaces": {
    "mcp": {
      "endpoint": "[https://agents.example.com/finance/mcp](https://agents.example.com/finance/mcp)",
      "version": "2024-11-05",
      "transport": "sse",
      "auth_type": "oauth2"
    }
  },

  "capabilities": {
    "description": "Analyzes portfolio concentration risk and cross-sector exposure using real-time market data.",
    "tags": ["finance", "risk", "equity"]
  }
}
