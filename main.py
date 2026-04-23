from llama_cpp import Llama

# 1. Load the model (Update the filename if yours is slightly different)
print("Loading model...")
llm = Llama(
    model_path="./llama-3.2-3b-instruct.Q4_K_M.gguf",
    chat_format="llama-3", # This tells it to expect system/user/assistant roles
    n_ctx=2048,            # Context window (how much text it can remember)
    verbose=False          # Hides the messy loading text
)

# 2. Define your instruction
user_instruction = "Draft an email to David to check if he reviewed the marketing deck."

# 3. Call the model using the exact roles from your training data
print("Drafting email...\n" + "-"*30)
response = llm.create_chat_completion(
    messages = [
        {
            "role": "system", 
            "content": "You are an AI assistant that drafts emails in my personal, concise, and friendly corporate style."
        },
        {
            "role": "user", 
            "content": user_instruction
        }
    ],
    temperature=0.3, # Keep it low (0.1 to 0.3) so it stays strict to your style
)

# 4. Print the final email
print(response["choices"][0]["message"]["content"])