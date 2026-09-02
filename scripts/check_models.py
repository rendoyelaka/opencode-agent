import requests
import os
import json
from datetime import datetime

def get_openrouter_free_models(api_key):
    """Get all free models from OpenRouter"""
    try:
        response = requests.get(
            "https://openrouter.ai/api/v1/models",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30
        )
        models = response.json().get("data", [])

        # Filter free models
        free_models = []
        for m in models:
            pricing = m.get("pricing", {})
            prompt_price = str(pricing.get("prompt", "1"))
            completion_price = str(pricing.get("completion", "1"))

            if prompt_price == "0" and completion_price == "0":
                free_models.append({
                    "id": m.get("id"),
                    "name": m.get("name"),
                    "context": m.get("context_length", 0),
                    "platform": "OpenRouter"
                })

        # Sort by context length (biggest first)
        free_models.sort(key=lambda x: x["context"], reverse=True)
        return free_models

    except Exception as e:
        print(f"OpenRouter error: {e}")
        return []

def get_huggingface_free_models(hf_token):
    """Get free models from HuggingFace"""
    try:
        response = requests.get(
            "https://router.huggingface.co/v1/models",
            headers={"Authorization": f"Bearer {hf_token}"},
            timeout=30
        )
        data = response.json()
        models = data.get("data", [])

        hf_models = []
        for m in models:
            hf_models.append({
                "id": m.get("id"),
                "name": m.get("id"),
                "context": 128000,
                "platform": "HuggingFace"
            })

        return hf_models[:10]  # Top 10

    except Exception as e:
        print(f"HuggingFace error: {e}")
        return []

def send_telegram_notification(bot_token, chat_id, message):
    """Send notification to Telegram"""
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        response = requests.post(url, json={
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }, timeout=30)
        return response.status_code == 200
    except Exception as e:
        print(f"Telegram error: {e}")
        return False

def main():
    api_key = os.getenv("OPENROUTER_API_KEY", "")
    hf_token = os.getenv("HF_TOKEN", "")
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "")

    print("Checking free models...")

    # Get models
    or_models = get_openrouter_free_models(api_key) if api_key else []
    hf_models = get_huggingface_free_models(hf_token) if hf_token else []

    # Build report
    date = datetime.now().strftime("%Y-%m-%d")
    report = f"""
🤖 *Daily Free Model Update*
📅 {date}

*OpenRouter Free Models: {len(or_models)}*
"""

    # Top 5 OpenRouter models
    for i, m in enumerate(or_models[:5], 1):
        ctx = f"{m['context']//1000}K" if m['context'] else "?"
        report += f"{i}. {m['name']} — {ctx} context\n"

    report += f"\n*HuggingFace Free Models: {len(hf_models)}*\n"

    # Top 5 HF models
    for i, m in enumerate(hf_models[:5], 1):
        report += f"{i}. {m['name']}\n"

    report += "\n✅ Pipeline auto-updated!"

    print(report)

    # Save to file
    with open("free_models.json", "w") as f:
        json.dump({
            "date": date,
            "openrouter": or_models,
            "huggingface": hf_models
        }, f, indent=2)

    # Send Telegram notification
    if bot_token and chat_id:
        send_telegram_notification(bot_token, chat_id, report)
        print("Telegram notification sent!")
    else:
        print("No Telegram config — skipping notification")

if __name__ == "__main__":
    main()
