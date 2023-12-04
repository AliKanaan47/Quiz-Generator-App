# Quiz-Generator-App

This is a simple Quiz Generator App built using Python and Streamlit. The app leverages the Langchain library to interact with a language model (in this case, ChatGPT from OpenAI) and generate a quiz based on user-specified parameters.

How to Run the App
Before running the app, ensure you have the necessary libraries installed. You can install them using the following command:
```
pip install os langchain streamlit
```


Make sure to replace openai_api_key with your valid OpenAI GPT-3 API key.

To run the app, execute the script:
```
streamlit run your_script_name.py
```

App Workflow


Initialization: The app starts by importing required libraries and initializing the session state.

Prompt Template: The create_the_quiz_prompt_template function defines the template for generating a quiz using the Langchain library. Users can specify the number of questions and the quiz context.

Quiz Chain Creation: The create_quiz_chain function creates a language model chain for generating the quiz based on the specified prompt template.

User Input: Users provide the topic and the number of questions they want in the quiz using Streamlit's user interface.

Quiz Generation: When the "GENERATE" button is clicked, the app generates a quiz based on the user input. The generated quiz is displayed, and the session state is updated.

Submit Quiz: After the quiz is generated, the "SUBMIT" button becomes visible. Clicking this button displays the questions and answers generated during the quiz creation process.

Additional Notes
This app assumes you have an OpenAI GPT-3 API key for the Chat model.

Customize the OpenAI API key, and other parameters as needed.

The app uses Streamlit for the user interface, making it easy to deploy and interact with.

Feel free to modify the code to suit your needs or extend its functionality.

Enjoy using the Quiz Generator App!
