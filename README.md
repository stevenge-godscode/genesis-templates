# Genesis Admin Prompt Templates

Templates for the Genesis Admin Prompt Marketplace live under the `packs/`
directory. Each pack represents one publishable template (e.g., "GraphRAG
Default Query Prompts") and contains:

```
<channel>/<slug>/
├── metadata.json      # describes locale/tags/modules
├── <module>.prompt    # raw prompt text per module
└── ...
```

## Adding / Updating a Pack

1. Create or edit `packs/<channel>/<slug>/metadata.json`.
2. Update the referenced `.prompt` files with the latest content.
3. Commit and push the changes to this repository.
4. In Genesis Admin → 管理员 → 提示词模板 → 系统来源，添加 metadata 的 Raw URL
   (例如 `https://raw.githubusercontent.com/<org>/<repo>/<branch>/packs/query/graphrag-default-en/metadata.json`).
5. 点击“同步”即可让 Prompt Marketplace 自动拉取 metadata 和对应的 `.prompt` 文件。

> 不再需要打包单独的 JSON；每个 metadata 直接对应一个模板记录。

## metadata.json Reference

```json
{
  "id": "graphrag-index-default-v1",
  "name": "GraphRAG Default Index Prompts",
  "channel": "index",
  "locale": "en-US",
  "scenario": "indexing",
  "version": "2025.11",
  "description": "English defaults for GraphRAG 2.7 indexing flows.",
  "tags": {
    "source": "graphrag",
    "release": "2.7.0",
    "industry": "general",
    "language": "en"
  },
  "modules": [
    {
      "key": "extract_graph",
      "label": "Entity Extraction Prompt",
      "description": "Detect entities and relationships.",
      "language": "en",
      "audience": "index_worker",
      "style": "analytical",
      "file": "extract_graph.prompt"
    }
  ]
}
```

- `channel`: `index` 或 `query`。
- `modules[*].file`: metadata 所在目录下的 prompt 文件路径。
- 通过 `tags`、`modules[*].language/style/audience` 等字段标注用途，方便 UI
  展示和筛选。
