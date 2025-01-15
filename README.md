# Restaurant Information Generation Using LangChain

This project demonstrates the use of LangChain and Large Language Models (LLMs) to generate creative and relevant information for Indian restaurants, including fancy names and appropriate menus based on user inputs. The implementation is done using Python, with Hugging Face Transformers and OpenAI API as core tools. A Streamlit app is also included for a user-friendly interface.

## Features
- Generate creative and relevant restaurant names based on a provided theme or concept.
- Generate appropriate menus tailored to the restaurant's theme.
- Leverages LangChain for managing and integrating LLM responses.
- Supports multiple LLMs, including OpenAI's API and Hugging Face models.
- Interactive **Streamlit** app for easy user interaction.

---

## Tools and Libraries Used
1. **LangChain**:
   - Framework for building applications powered by language models.
   - Used for managing LLM calls and chaining responses effectively.

2. **OpenAI API**:
   - Provides access to OpenAI’s GPT models for generating names and menu ideas.

3. **Hugging Face Transformers**:
   - Supports alternative free LLMs (e.g., GPT-J, GPT-Neo).

4. **Streamlit**:
   - Used to create a user-friendly web-based interface for the project.

5. **Python**:
   - Core programming language for scripting and implementation.

---

## Project Structure
- `main.py`:
  - Entry point for the application.
  - Handles user interaction and triggers name and menu generation using LLMs.

- `langchain_helper.py`:
  - Contains utility functions and logic for interacting with LangChain and the chosen LLMs.

- `LangChain_Notebook.ipynb`:
  - Jupyter Notebook demonstrating the project’s functionality interactively.

- `app.py`:
  - Streamlit application for running the project through a web interface.

---

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or later
- pip (Python package manager)

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/restaurant-info-generator.git
   cd restaurant-info-generator
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**:
   - **OpenAI**:
     Add your OpenAI API key to the environment:
     ```bash
     export OPENAI_API_KEY="your_openai_api_key"
     ```

   - **Hugging Face** (optional):
     Add your Hugging Face token to the environment:
     ```bash
     export HUGGINGFACE_TOKEN="your_huggingface_token"
     ```

---

## How to Run

1. **Run the Main Script**:
   ```bash
   python main.py
   ```
   - Enter the theme or concept for your restaurant when prompted.
   - The system will generate and display a fancy restaurant name and an appropriate menu.

2. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```
   - Open the displayed URL in your browser to interact with the web interface.

3. **Interactive Jupyter Notebook**:
   - Open `LangChain_Notebook.ipynb` in Jupyter.
   - Follow the step-by-step instructions to see the project in action.

---

## Example Output
Prompt:
```plaintext
I want to open a restaurant for Indian food. Suggest a fancy name and an appropriate menu for this.
```
Output:
```plaintext
Name: "Spice Symphony"
Menu:
1. Butter Chicken with Garlic Naan
2. Paneer Tikka Masala
3. Lamb Rogan Josh
4. Mango Lassi
5. Gulab Jamun
```

---

## Screenshots
### 1. Terminal Output
*Insert a screenshot of the terminal running the `main.py` script and generating a restaurant name and menu.*

### 2. Streamlit App
*Insert a screenshot of the Streamlit app showcasing the generation process.*

### 3. Notebook Output
*Insert a screenshot of the Jupyter Notebook demonstrating the process.*

---

## Future Improvements
- Support for additional languages and themes.
- Add more advanced features to the Streamlit app.
- Integrate additional LLMs for more creative options.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- **OpenAI** for their GPT models.
- **Hugging Face** for their freely available language models.
- **LangChain** for providing an easy way to manage LLM workflows.
- **Streamlit** for enabling quick and interactive web app development.

Feel free to raise an issue or contribute to this repository!

