# OpenCode Agent 🤖

Autonomous AI coding agent powered by OpenCode + OpenRouter free models.

## How To Use

Comment `/oc [your task]` in any issue:

```
/oc implement Step 23 DEX encryption
/oc fix build error in gradle
/oc implement anti-tamper in Step 46
/oc push all changes to main branch
```

## Setup Required Secrets

Go to Settings → Secrets → Actions and add:

| Secret | Value |
|--------|-------|
| `GITHUB_PRIVATE_TOKEN` | Your GitHub Personal Access Token |
| `PRIVATE_REPO_NAME` | `username/nova-no-vpn-main` |
| `OPENROUTER_API_KEY` | Your OpenRouter API key |
| `HF_TOKEN` | HuggingFace token (optional) |
| `GROQ_API_KEY` | Groq API key (optional) |
| `CEREBRAS_API_KEY` | Cerebras API key (optional) |
| `VENICE_API_KEY` | Venice AI key (optional) |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token (optional) |
| `TELEGRAM_CHAT_ID` | Your Telegram chat ID (optional) |

## AI Models Used (All Free)

### Priority 1 — Chat/Info/Results
- MiniMax M3 (1.05M context)
- NVIDIA Nemotron Ultra 550B (1M context)
- GLM 5.2 (256K context)

### Priority 2 — Code/Scripts/Tools (Uncensored)
- Venice Uncensored (Dolphin Mistral 24B)
- Nous Hermes 3 405B
- DeepSeek R1 671B

## Fallback Chain
OpenRouter → HuggingFace → Groq → Cerebras → Pollinations

## Cost
**$0 forever** — all free models
