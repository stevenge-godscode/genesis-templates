# Prompt Marketplace Templates

该目录收录可直接托管到 GitHub（或任何静态文件服务器）供 Prompt Marketplace 拉取的模板文件。

## 文件结构

| 文件 | 说明 |
| --- | --- |
| `prompt-market-defaults.json` | GraphRAG 官方默认的索引 / 查询提示词模板，包含全量模块（索引：`extract_graph`、`community_reports`、`summarize_descriptions`；查询：`global_map`、`global_reduce`、`local_map`、`local_answer`、`answer`）。 |

## 使用方式

1. 将 `prompt-market-defaults.json` 提交到公开仓库（例如 `https://github.com/<org>/<repo>/templates/prompt-market-defaults.json`）。
2. 记录该文件的 Raw URL（GitHub 可使用 `https://raw.githubusercontent.com/<org>/<repo>/<branch>/templates/prompt-market-defaults.json`）。
3. 在管理员后台「提示词模板」页面添加新的系统来源，URL 填写上述 Raw 链接，保存后点击「同步」即可把该文件内的模板写入市场缓存。
4. 项目成员即可在「提示词市场」中浏览并克隆这些模板。

> 模板格式：顶层对象包含 `items` 数组，每个元素描述一个模板条目，可同时包含 `index_prompts` 与 `query_prompts` 字段（后端会按字段自动识别支持的频道）。
