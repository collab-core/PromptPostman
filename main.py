from llama_cpp import Llama
import os
import sys
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration from .env
your_name = os.getenv("YOUR_NAME", "Your Name")
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT", 587))
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")

# Parse nickname mappings from .env
nicknames = {}
for key, value in os.environ.items():
    if key.startswith("NICKNAME_"):
        nickname = key.replace("NICKNAME_", "").lower()
        nicknames[nickname] = value

# Utility Functions
def clear_screen():
    """Clear terminal screen (works on Windows, Mac, and Linux)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print application header"""
    print("\n" + "=" * 70)
    print(" " * 15 + "PROMPT POSTMAN - AI EMAIL GENERATOR")
    print("=" * 70 + "\n")

def loading_animation(duration=2, text="Loading"):
    """Display professional loading animation"""
    frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    frame_idx = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{text} {frames[frame_idx % len(frames)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        frame_idx += 1
    sys.stdout.write("\r" + " " * (len(text) + 3) + "\r")
    sys.stdout.flush()

def confirm_input(prompt):
    """Get yes/no confirmation from user (case insensitive)"""
    while True:
        response = input(prompt + " (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'")

def get_nickname_from_instruction(instruction):
    """Extract nickname from user instruction if present"""
    instruction_lower = instruction.lower()
    for nickname in nicknames.keys():
        if nickname in instruction_lower:
            return nickname
    return None

def ask_to_continue():
    """Ask user if they want to continue or quit"""
    while True:
        response = input("Continue with another email? Press 'q' to quit or any other key to continue: ").strip().lower()
        if response == 'q':
            return False
        else:
            return True

# Load the model once at startup
print("Initializing application...")
loading_animation(duration=2, text="Loading model")
llm = Llama(
    model_path="./llama-3.2-3b-instruct.Q4_K_M.gguf",
    chat_format="llama-3",
    n_ctx=2048,
    verbose=False
)

# Main application loop
app_running = True
while app_running:
    # Clear screen and print header
    clear_screen()
    print_header()
    print("Model ready. Starting email generation...\n")

    # 1. Get user instruction as input
    print("-" * 70)
    user_instruction = input("Enter your email request: ").strip()
    print("-" * 70 + "\n")

    # 2. Draft the email
    print("Processing request...")
    loading_animation(duration=2, text="Drafting email")
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
        temperature=0.3,
    )
    print("Email draft completed.\n")

    # 3. Process the response
    response_text = response["choices"][0]["message"]["content"]
    response_text = response_text.replace("[Your Name]", your_name)

    # 4. Display the draft
    print("=" * 70)
    print("DRAFT EMAIL")
    print("=" * 70)
    print(response_text)
    print("=" * 70 + "\n")

    # 5. Determine recipient email
    receiver_email = None

    # Check if instruction contains a nickname
    detected_nickname = get_nickname_from_instruction(user_instruction)

    if detected_nickname:
        mapped_email = nicknames[detected_nickname]
        print(f"Recipient detected: {detected_nickname.capitalize()} ({mapped_email})")
        
        if confirm_input("Send to this recipient?"):
            receiver_email = mapped_email
        else:
            # User wants to specify different email
            receiver_email = input("\nEnter recipient email address: ").strip()
    else:
        # No nickname detected, ask for email
        receiver_email = input("Enter recipient email address: ").strip()

    print()

    # 6. Send email via SMTP
    try:
        print("Sending email...")
        loading_animation(duration=2, text="Transmitting")
        
        # Create message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Email Draft"
        
        message.attach(MIMEText(response_text, "plain"))
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        server.quit()
        
        print("\n" + "=" * 70)
        print("SUCCESS: Email sent successfully!")
        print(f"Recipient: {receiver_email}")
        print("=" * 70 + "\n")
        
        # Ask if user wants to continue
        if not ask_to_continue():
            clear_screen()
            print("\nThank you for using Prompt Postman. Goodbye!\n")
            app_running = False
        
    except Exception as e:
        print("\n" + "=" * 70)
        print(f"ERROR: Failed to send email")
        print(f"Details: {e}")
        print("=" * 70 + "\n")
        
        # Ask if user wants to try again
        if not ask_to_continue():
            clear_screen()
            print("\nThank you for using Prompt Postman. Goodbye!\n")
            app_running = False