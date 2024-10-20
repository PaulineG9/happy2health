# Import helpline data from helplines.py
from helplines import helpline_list

def chatbot_response(user_input):
    """
    Generate a response based on user input and match it to available helplines or provide helpful suggestions.
    """
    # Normalize user input (remove extra spaces, convert to lowercase)
    user_input = user_input.strip().lower()

    # Define keywords to match with helpline categories
    resource_keywords = {
        "counseling": "Free Online Counselling",
        "talk": "Someone to Talk To",
        "indigenous": "Aboriginal & Torres Strait Islander Resources",
        "lgbti": "LGBTI Support",
        "eating disorder": "Eating Disorder Resources",
        "mood disorder": "Mood Disorder Resources",
        "faith": "Faith-Based Support",
        "post-natal": "Post-Natal Support",
        "suicide": "Suicide Prevention"
    }

    # Attempt to find a matching helpline category based on user input
    for keyword, category in resource_keywords.items():
        if keyword in user_input:
            # Use .get() to avoid KeyErrors if category is not found
            response = helpline_list.get(category)
            if response:
                return f"Connecting you to {response} now. Please stay safe."

    # Default response if no matching keyword is found
    return (
        "I'm here to help! Please specify the type of support you need:\n"
        "- Counseling\n"
        "- Someone to Talk To\n"
        "- Indigenous Resources\n"
        "- LGBTI Support\n"
        "- Eating Disorder Support\n"
        "- Mood Disorder Support\n"
        "- Faith-Based Support\n"
        "- Post-Natal Support\n"
        "- Suicide Prevention"
    )

# Example usage to test the chatbot function
if __name__ == "__main__":
    # Simulate user input for testing
    test_input = input("Type your message: ")
    print(chatbot_response(test_input))
