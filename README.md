# Prompt Postman - AI Email Generator

**Prompt Postman** is an intelligent email drafting and sending application that uses AI (Llama 3.2) to generate professional emails based on your natural language requests.

## Features

- **AI-Powered Email Generation**: Uses Llama 3.2 3B model to draft emails in your personal style
- **Terminal-Based Editor**: Edit generated emails directly in the terminal with multiple editing options
- **Auto-Download Model**: Automatically fetches the model from Hugging Face on first run
- **Smart Recipient Detection**: Automatically detects and maps nicknames to email addresses
- **Professional UI**: Clean terminal interface with loading animations
- **SMTP Integration**: Direct email sending via Gmail SMTP
- **Interactive Loop**: Continuously generate and send emails without restarting
- **Easy Configuration**: Centralized `.env` file for all settings

## Requirements

- Python 3.8+
- 4GB+ RAM (for running Llama 3.2 model)
- 2GB+ Storage (for downloaded model)
- Internet connection (for model auto-download and SMTP)
- Gmail account with app-specific password

## Installation

### 1. Clone or Download the Project

```bash
cd promptpostman/PromptPostman
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Model Setup (Auto-Download)

The application automatically downloads the model from Hugging Face on first run if it's not already present. The download may take a few minutes depending on your internet speed.

**Note**: To use a custom model:

1. Upload your model to a Hugging Face repository
2. Update these values in `main.py`:
   ```python
   HF_REPO_ID = "your-username/your-repo-name"
   MODEL_FILENAME = "your-model-file.gguf"
   ```

## Configuration

### 1. Configure Model (Optional)

By default, the app uses:

- **Repository**: `hitrohitro/llama-3.2-3b-email-assistant`
- **Model File**: `llama-3.2-3b-instruct.Q4_K_M.gguf`

To use a different model, edit the top of `main.py`:

```python
HF_REPO_ID = "your-username/your-repo-name"
MODEL_FILENAME = "your-model.gguf"
```

The model will be automatically downloaded from Hugging Face on first run.

### 2. Set Up `.env` File

Copy the template below and update with your details:

```env
# Gmail SMTP Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
YOUR_NAME=Your Name

# Nickname to Email Mapping
NICKNAME_DAVID=david.smith@company.com
NICKNAME_JOHN=john.doe@company.com
NICKNAME_SARAH=sarah.johnson@company.com
```

### 3. Gmail App Password Setup

1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Click **Security** in the left menu
3. Enable **2-Step Verification** (if not already enabled)
4. Scroll down to **App passwords**
5. Select **Mail** and **Windows Computer**
6. Copy the generated 16-character password
7. Paste it in `.env` as `SENDER_PASSWORD` (without quotes)

### 4. Add Nicknames

In the `.env` file, add as many nickname mappings as needed:

```env
NICKNAME_ALICE=alice@company.com
NICKNAME_BOB=bob@company.com
NICKNAME_CHARLIE=charlie@company.com
```

## Usage

### Running the Application

```bash
python main.py
```

### Workflow

1. **Application starts** - Model loads and displays welcome header
2. **Enter request** - Type your email request naturally:
   - "Draft an email to David about the quarterly review"
   - "Email John asking for feedback on the proposal"
3. **Review draft** - AI generates and displays the email
4. **Edit (Optional)** - Choose to edit the email:
   - Type `y` or `yes` to enter terminal editor
   - Choose one of three options:
     - **Option 1**: Replace entire email (paste new content, type `END` to finish)
     - **Option 2**: Edit specific line(s) (select line numbers and update)
     - **Option 3**: Keep original draft
   - The edited email will be displayed
   - Type `n` or `no` to skip editing and keep original draft
5. **Confirm recipient** - If nickname detected, confirm sending:
   - Type `y` or `yes` to send to detected recipient
   - Type `n` or `no` to specify a different email
6. **Enter email** - Provide recipient email address if needed
7. **Email sent** - Confirmation message displays
8. **Continue or quit**:
   - Press `q` to exit application
   - Press any other key to draft another email

### Example Session

```
======================================================================
                 PROMPT POSTMAN - AI EMAIL GENERATOR
======================================================================

Loading model |

Model ready. Starting email generation...

----------------------------------------------------------------------
Enter your email request: Draft an email to David about the meeting
----------------------------------------------------------------------

Processing request...
Drafting email...

======================================================================
DRAFT EMAIL
======================================================================
Hi David,

I hope this email finds you well. I wanted to reach out to discuss
our upcoming meeting on the marketing strategy. Are you available
next Tuesday at 2 PM?

Best regards,
Rohit
======================================================================

Would you like to edit this email? (y/n): y

----------------------------------------------------------------------
TERMINAL EMAIL EDITOR
----------------------------------------------------------------------

Current email:

 1. Hi David,
 2.
 3. I hope this email finds you well. I wanted to reach out to discuss
 4. our upcoming meeting on the marketing strategy. Are you available
 5. next Tuesday at 2 PM?
 6.
 7. Best regards,
 8. Rohit

----------------------------------------------------------------------
Options:
  1. Replace entire email
  2. Edit specific line(s)
  3. Keep current email
----------------------------------------------------------------------

Select option (1/2/3): 2
Enter line number(s) to edit (e.g., '1' or '1,3,5'): 3,4

Current line 3: I hope this email finds you well. I wanted to reach out to discuss
Enter new content: I hope this email finds you well. I wanted to discuss

Current line 4: our upcoming meeting on the marketing strategy. Are you available
Enter new content: our upcoming meeting on the marketing strategy. Would you be available

======================================================================
EDITED EMAIL
======================================================================
Hi David,

I hope this email finds you well. I wanted to discuss
our upcoming meeting on the marketing strategy. Would you be available
next Tuesday at 2 PM?

Best regards,
Rohit
======================================================================

Recipient detected: David (david.smith@company.com)
Send to this recipient? (y/n): y

Sending email...
Transmitting -

======================================================================
SUCCESS: Email sent successfully!
Recipient: david.smith@company.com
======================================================================

Continue with another email? Press 'q' to quit or any other key to continue: q

Thank you for using Prompt Postman. Goodbye!
```

## Troubleshooting

### Error: "Username and Password not accepted"

**Solution:**

- Ensure you're using an **app-specific password**, not your regular Gmail password
- Verify 2-Step Verification is enabled
- Check the password in `.env` has no extra spaces or quotes

### Error: "Model loading fails"

**Solution:**

- Verify your internet connection (model downloads from Hugging Face)
- Ensure `HF_REPO_ID` and `MODEL_FILENAME` in `main.py` are correct
- Check you have at least 4GB free storage for the model
- Try running on a machine with better specs if download times out

### Error: "SMTP connection failed"

**Solution:**

- Check your internet connection
- Verify `SMTP_SERVER` and `SMTP_PORT` in `.env`
- Ensure Gmail account has SMTP enabled

### Nickname not detected

**Solution:**

- Ensure nickname format in `.env` is correct: `NICKNAME_<NAME>=<EMAIL>`
- The nickname search is case-insensitive
- Make sure the nickname appears in your instruction

## File Structure

```
PromptPostman/
├── main.py                          # Main application
├── requirements.txt                 # Python dependencies
├── .env                            # Configuration file (not in git)
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
└── llama-3.2-3b-instruct.Q4_K_M.gguf  # AI model (auto-downloaded from Hugging Face)
```

## Security Notes

- ⚠️ **Never commit `.env` to version control** - It contains sensitive credentials
- ⚠️ **Use app-specific passwords** - Never use your main Gmail password
- ⚠️ **Keep credentials private** - Don't share your `.env` file

## Contributing

Feel free to fork and contribute improvements!

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Support

For issues or questions, please check the Troubleshooting section or open an issue on the repository.

---

**Prompt Postman** - Making email generation smarter, one draft at a time.
