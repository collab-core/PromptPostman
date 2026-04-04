# 🚀 PromptPostman

# 🧠 How it Works
1. **User Input:** Accepts messy, natural human language.
2. **SLM Parser:** A fine-tuned 3B parameter model processes the intent and aggressively formats it into a strict JSON tool call.
3. **Execution Layer:** A Python wrapper catches the JSON and triggers the hardcoded email function (via standard SMTP/API).

# 🛠️ Tech Stack
* **Model:** [e.g., Llama-3.2-3B-Instruct or Qwen-2.5-3B]
* **Fine-Tuning:** LoRA adapters via Unsloth (trained on Google Colab)
* **Execution:** Python (json, smtplib)

# 🤝 Collaboration
* The dataset generation and model training notebook are tracked in this repository.
* The model weights are hosted separately on Hugging Face.
