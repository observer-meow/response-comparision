import json

def compare_filtered_answers(openai, gemini):
    differences = []

    # Filter openai to include only 'multiple-choice' and 'checkbox' types
    filtered_openai = [item for item in openai if item['type'] in ['multiple-choice', 'checkbox']]

    for obj1, obj2 in zip(filtered_openai, gemini):
        # Compare the 'answer' fields
        if obj1['answer'] != obj2['answer']:
            # If different, add the 'question' and both 'answers' to the result list
            differences.append({
                "question": obj1['question'],
                "openai_answer": obj1['answer'],
                "gemini_answer": obj2['answer']
            })

    return differences

# Read the sets from the files
with open('openai.txt', 'r') as file:
    openai = json.load(file)

with open('gemini.txt', 'r') as file:
    gemini = json.load(file)

# Run the comparison
differences = compare_filtered_answers(openai, gemini)

# Write the differences to a text file
with open('differences.txt', 'w') as output_file:
    for diff in differences:
        output_file.write(f"Question: {diff['question']}\n")
        output_file.write(f"OpenAI Answer: {diff['openai_answer']}\n")
        output_file.write(f"Gemini Answer: {diff['gemini_answer']}\n\n")
