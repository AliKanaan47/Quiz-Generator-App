# Import necessary libraries
import os
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import streamlit as st
import random

# Function to initialize session state
def init_session_state():
    # Check if 'quiz_generated' and 'user_answers' are in session state, initialize if not
    if 'quiz_generated' not in st.session_state:
        st.session_state.quiz_generated = False
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []

# Function to create the prompt template for the quiz
def create_the_quiz_prompt_template():
    """Create the prompt template for the quiz app."""
    
    template = """
    You are an expert quiz maker for technical fields. Let's think step by step and
    create a quiz with {num_questions} questions about the following concept/content: {quiz_context}.

    The format of the quiz should look like this:
     Multiple Choice:
     Questions:
        <Question1>: 
            
            a. Answer 1\n
            
            b. Answer 2\n
            
            c. Answer 3\n
            
            d. Answer 4\n
        <Question2>: 
            
            a. Answer 1\n
            
            b. Answer 2\n
            
            c. Answer 3\n
            
            d. Answer 4\n
        ....
     Answers:
        <Answer1>: <a|b|c|d>

        <Answer2>: <a|b|c|d>
        ....
        Example:
         Questions:
         1. What is the time complexity of a binary search tree?
            
            a. O(n)\n
            
            b. O(log n)\n
            
            c. O(n^2)\n
            
            d. O(1)\n
         Answers: 
            
            1. b
    """
    # Create a prompt template using langchain library
    prompt = PromptTemplate.from_template(template)
    prompt.format(num_questions=3, quiz_context="Autonomous Cars")
    
    return prompt

# Function to create the quiz chain
def create_quiz_chain(prompt_template,llm):
    """Creates the chain for the quiz app."""
    return LLMChain(llm=llm, prompt=prompt_template)

# Function to split questions and answers from the quiz response
def split_questions_answers(quiz_response):
    """Function that splits the questions and answers from the quiz response."""
    questions = quiz_response.split("Answers:")[0]
    answers = quiz_response.split("Answers:")[1]
    return questions, answers

# Main function
def main():
    init_session_state()  # Initialize session state
    st.title("Quiz Generator App")
    st.write("This app generates a quiz based on a given topic")
    prompt_template = create_the_quiz_prompt_template()
    llm = ChatOpenAI(openai_api_key="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")
    chain = create_quiz_chain(prompt_template, llm)
    context = st.text_area("Please specify the topic you want")
    num_questions = st.number_input("Please specify the number of questions ", min_value=1, max_value=10, value=3)
    
    if st.button("GENERATE"):
        quiz_response = chain.run(num_questions=num_questions, quiz_context=context)
        st.write("Quiz Generated!")        
        questions, answers = split_questions_answers(quiz_response)
        st.session_state.answers = answers
        st.session_state.questions = questions
        st.write(questions)
        st.session_state.quiz_generated = True  # Set the flag to True when the quiz is generated
    
    # Show the "Submit Quiz" button only if the quiz has been generated
    if st.session_state.quiz_generated and st.button('SUBMIT'):
        st.markdown(st.session_state.questions)
        st.write("----")
        st.markdown(st.session_state.answers)

# Entry point for the script
if __name__ == "__main__":
    main()