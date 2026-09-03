#!/usr/bin/env python3
"""
Model switcher for OpenCode via Telegram
Updates OpenCode config with selected model
"""

import json
import os
import sys

MODELS = {
    "MODEL1": {
        "id": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free",
        "name": "Nemotron Ultra 550B",
        "use": "Best reasoning + chat"
    },
    "MODEL2": {
        "id": "openrouter/deepseek/deepseek-r1:free",
        "name": "DeepSeek R1",
        "use": "Best coding"
    },
    "MODEL3": {
        "id": "openrouter/cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
        "name": "Venice Uncensored",
        "use": "No restrictions"
    },
    "MODEL4": {
        "id": "openrouter/z-ai/glm-5.2:free",
        "name": "GLM 5.2",
        "use": "Fast responses"
    },
    "MODEL5": {
        "id": "openrouter/minimax/minimax-m3:free",
        "name": "MiniMax M3",
        "use": "Long context 1M"
    },
    "MODEL6": {
        "id": "openrouter/nousresearch/hermes-3-llama-3.1-405b:free",
        "name": "Nous Hermes 405B",
        "use": "Uncensored large"
    },
    "MODEL7": {
        "id": "openrouter/meta-llama/llama-3.3-70b-instruct:free",
        "name": "Llama 3.3 70B",
        "use": "General purpose"
    },
}

def switch_model(model_key):
    config_path = os.path.expanduser("~/.config/opencode/config.json")
    api_key = os.environ.get("OPENROUTER_API_KEY", "")

    if model_key not in MODELS:
        print(f"Unknown model: {model_key}")
        print("Available models:", list(MODELS.keys()))
        return False

    model = MODELS[model_key]
    config = {
        "providers": {
            "openrouter": {
                "apiKey": api_key,
                "baseURL": "https://openrouter.ai/api/v1"
            }
        },
        "model": model["id"],
        "autoapprove": True
    }

    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    print(f"Switched to: {model['name']}")
    print(f"Model ID: {model['id']}")
    print(f"Best for: {model['use']}")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        switch_model(sys.argv[1].upper())
    else:
        print("Usage: python3 switch_model.py MODEL1")
        print("\nAvailable models:")
        for key, m in MODELS.items():
            print(f"  {key}: {m['name']} - {m['use']}")
