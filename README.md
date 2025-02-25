# Grainger Take Home Assignment

This repository contains a solution for Grainger take-home interview assignment.

## Project Structure

- `data.py` - processes and generates the dataset according to assignment specification.
- `main.py` - Processes the dataset and generates desired output.
- `prompt_store.py` - Stores the prompt used in the workflow.


## How to Run

Follow these steps to run the project in the correct order:

### 1. Clone the Repository
```bash
git clone https://github.com/gosandhya/grainger-applied-ai-interview.git
cd grainger-applied-ai-interview
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
Ensure you have the required dependencies installed:
```bash
pip install -r requirements.txt  # If a requirements file exists
```

### 4. Set Up API Key
This project requires an Anthropic API key. Set it as an environment variable before running the scripts:
```bash
export ANTHROPIC_API_KEY=your_api_key_here  # On Windows use `set ANTHROPIC_API_KEY=your_api_key_here`
```

### 5. Generate the Dataset
Run the `data.py` script to create the dataset:
```bash
python data.py
```

### 6. Run the Main Processing Script
Use `main.py` to process the dataset and generate output:
```bash
python main.py
```

### 7. Utilize the Prompt Store
The `prompt_store.py` contains stored prompts used in the project. 

## Notes
- Ensure you have Python installed (preferably 3.10 or later).
- If any additional dependencies are required, add them to `requirements.txt`.


