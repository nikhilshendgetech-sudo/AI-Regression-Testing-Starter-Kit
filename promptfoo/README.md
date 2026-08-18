# Promptfoo Demo

This folder demonstrates how the free dataset can be connected to an LLM evaluation tool.

## Important
- The example uses a provider configuration that may require your own API credentials.
- Do not commit API keys.
- Adjust the provider/model to your environment before running.

## Typical commands
```bash
npm install -g promptfoo
promptfoo eval -c promptfooconfig.yaml
promptfoo view
```

The YAML is intentionally small for the free MVP. The paid version can expand this
into a larger test library, CSV-driven generation, richer assertions, and CI workflows.
