# OpenCode Agent 🤖

Autonomous AI coding agent powered by OpenCode + OpenRouter free models.

## How To Use

Comment `/oc [your task]` in any issue and OpenCode will handle it automatically.

## Required Secrets

Go to Settings → Secrets and variables → Actions → New repository secret

| Secret Name | Value |
|-------------|-------|
| `PAT_TOKEN` | Your GitHub Personal Access Token |
| `PRIVATE_REPO_NAME` | Your private repo (username/reponame) |
| `OPENROUTER_API_KEY` | Your OpenRouter API key |
| `HF_TOKEN` | HuggingFace token (optional) |
| `GROQ_API_KEY` | Groq API key (optional) |
| `CEREBRAS_API_KEY` | Cerebras API key (optional) |
| `VENICE_API_KEY` | Venice AI key (optional) |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token (optional) |
| `TELEGRAM_CHAT_ID` | Your Telegram chat ID (optional) |

## AI Models Used (All Free)

- NVIDIA Nemotron Ultra 550B
- MiniMax M3
- DeepSeek R1
- Nous Hermes 405B
- GLM 5.2
- Llama 3.3 70B

## Cost

**$0 forever** — all free models
