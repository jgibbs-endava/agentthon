---
name: google_documents_skill
description: Retrieve authoritative Google Developer documentation using the Developer Knowledge MCP server or the Developer Knowledge REST API (v1alpha). Use this whenever users ask about Google APIs, SDKs, Cloud, Firebase, Android, Maps, or official implementation details.
---

# Google Developer Documentation Skill  
(Developer Knowledge MCP + REST v1alpha)

This skill enables reliable retrieval of **official Google documentation** using:

1. **Developer Knowledge MCP server** (preferred when MCP is supported)
2. **Developer Knowledge REST API (v1alpha)** (fallback or direct HTTP usage)

Always prefer MCP when available. Use REST if:
- MCP is unavailable
- You need reproducible curl commands
- The user wants raw HTTP examples

---

# SECTION 1 — CLI REQUIREMENTS (Most Common Failure Point)

## Required: Updated Google Cloud CLI

Check version:

```bash
gcloud --version
```

Verify MCP commands exist:

```bash
gcloud beta services mcp --help
```

ONLY If the `mcp` command group does not appear:
- Re-run `gcloud components update`
- Reinstall beta component
- Restart your shell

- Update to latest:

```bash
gcloud components update
```

- Install beta components (required for MCP commands):

```bash
gcloud components install beta
```

There is no single fixed minimum version published, but **you must have a current gcloud install with the beta component installed**.

---

# SECTION 2 — PROJECT SETUP

## 1) Enable the Developer Knowledge API

```bash
gcloud services enable developerknowledge.googleapis.com --project=PROJECT_ID
```

## 2) Create an API key

```bash
gcloud services api-keys create \
  --project=PROJECT_ID \
  --display-name="Developer Knowledge Key"
```

Restrict the key to:
- API: `developerknowledge.googleapis.com`

## 3) Enable the MCP server

```bash
gcloud beta services mcp enable developerknowledge.googleapis.com --project=PROJECT_ID
```

---

# SECTION 3 — MCP SERVER USAGE (Preferred Method)

## MCP Endpoint

```
https://developerknowledge.googleapis.com/mcp
```

## Required Header

```
X-Goog-Api-Key: YOUR_API_KEY
```

## Available MCP Tools

- `search_documents`
- `get_document`
- `batch_get_documents`

## Recommended MCP Workflow

1. Call `search_documents` with a precise query.
2. Inspect results for relevant `parent` identifiers.
3. Call `get_document` (or `batch_get_documents`) using those parents.
4. Extract:
   - Setup instructions
   - Authentication details
   - Code samples
   - Configuration steps
5. Summarize clearly for the user.

---

# SECTION 4 — REST API (v1alpha) REFERENCE

Base URL:

```
https://developerknowledge.googleapis.com
```

API Version:

```
v1alpha
```

Authentication options:
- Header: `X-goog-api-key: YOUR_API_KEY`
- OR query parameter: `?key=YOUR_API_KEY`

---

# METHOD 1 — Search Document Chunks

Endpoint:

```
GET /v1alpha/documents:searchDocumentChunks
```

Full example:

```bash
curl -H "X-goog-api-key: YOUR_API_KEY" \
"https://developerknowledge.googleapis.com/v1alpha/documents:searchDocumentChunks?query=Cloud%20Run%20deploy%20container%20Python"
```

Purpose:
- Returns relevant documentation snippets
- Provides `parent` document references
- Use first to discover relevant documents

Use this when:
- The question is broad
- You don’t know the exact document name

---

# METHOD 2 — Get Single Document

Endpoint:

```
GET /v1alpha/{name=documents/**}
```

Example:

```bash
curl -H "X-goog-api-key: YOUR_API_KEY" \
"https://developerknowledge.googleapis.com/v1alpha/documents/cloud-run/deploying-containers"
```

Purpose:
- Retrieves full Markdown documentation
- Includes code samples and structured content

Use after identifying the document via search.

---

# METHOD 3 — Batch Get Documents

Endpoint:

```
GET /v1alpha/documents:batchGet
```

Example:

```bash
curl -H "X-goog-api-key: YOUR_API_KEY" \
"https://developerknowledge.googleapis.com/v1alpha/documents:batchGet?names=documents/doc1&names=documents/doc2"
```

Purpose:
- Fetch multiple documents in one call
- Useful for comparison or multi-part answers

---

# RECOMMENDED WORKFLOW (REST)

1. Construct precise query including:
   - Product name
   - Language
   - Specific task

2. Call:
   ```
   documents:searchDocumentChunks
   ```

3. Identify relevant `parent` documents.

4. Retrieve full content via:
   - `documents.get`
   - OR `documents.batchGet`

5. Extract:
   - Setup steps
   - Authentication flow
   - Required IAM roles
   - CLI commands
   - SDK initialization
   - Code examples

6. Provide accurate answer grounded in retrieved content.

---

# QUERY WRITING GUIDELINES

Good queries:
- "Cloud Run deploy container Python"
- "Firestore add document Node.js example"
- "Vertex AI embeddings REST example"
- "Google OAuth2 service account authentication"
- "Cloud Storage signed URL Go"

Avoid vague queries:
- "Google login"
- "Storage help"
- "API example"

Always include:
- Product
- Language (if relevant)
- Specific action

---

# WHEN TO USE THIS SKILL

Use for:
- Google Cloud
- Firebase
- Maps Platform
- Android
- Google APIs
- Authentication / IAM
- Deployment guides
- Official limits / quotas
- SDK usage
- REST reference

Do NOT use for:
- General programming questions
- Non-Google services
- Pure conceptual explanations

Always prioritize retrieved official documentation over model memory.
