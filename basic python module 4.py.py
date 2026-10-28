# Step 1: Preloaded Feedbacks (Given Data)
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        '  Very GOOD Service!!!',
        'poor support,   not happy   ',
        'GREAT experience! will come again.',
        'okay   okay...',
        '  not   BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# Step 2: Add More Feedbacks
try:
    num_new_feedbacks = int(input("How many more feedbacks do you want to add? "))
except ValueError:
    print("Invalid input. Proceeding with 0 new feedbacks.")
    num_new_feedbacks = 0

for i in range(num_new_feedbacks):
    name = input("Enter Name: ")
    feedback_text = input("Enter Written Feedback: ")
    
    # Ensure valid rating
    while True:
        try:
            rating = int(input("Enter Rating (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid integer for the rating.")
            
    # Automatically increment S_No
    next_s_no = feedback_data['S_No'][-1] + 1 if feedback_data['S_No'] else 1
    
    # Append all new data
    feedback_data['S_No'].append(next_s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback_text)
    feedback_data['Rating'].append(rating)

# Step 3: Text Cleaning
cleaned_feedbacks = []
for text in feedback_data['Feedback']:
    # Remove punctuation (. , ! ?)
    for punctuation in ['.', ',', '!', '?']:
        text = text.replace(punctuation, '')
    
    # Convert to lowercase
    text = text.lower()
    
    # Split handles multiple spaces, leading/trailing spaces, and join puts a single space
    clean_text = ' '.join(text.split())
    cleaned_feedbacks.append(clean_text)

feedback_data['Feedback'] = cleaned_feedbacks

# Step 4: Word Count Insights
def count_word_in_feedbacks(word):
    count = 0
    search_word = word.lower()
    for text in feedback_data['Feedback']:
        # Split into words to match exact words rather than substrings
        if search_word in text.split():
            count += 1
    return count

print("\n--- Word Count Insights ---")
print(f"Number of feedbacks containing 'good': {count_word_in_feedbacks('good')}")
print(f"Number of feedbacks containing 'poor': {count_word_in_feedbacks('poor')}")
print(f"Number of feedbacks containing 'excellent': {count_word_in_feedbacks('excellent')}")

# Step 5: Final Summary & Insights
print("\n--- Final Cleaned Feedback Data ---")
print(feedback_data)

# Print the average rating
average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print(f"\nAverage Rating: {average_rating:.2f}")

# Find and display the feedback with the longest comment (in terms of word count)
longest_comment = ""
max_words = 0
for text in feedback_data['Feedback']:
    word_count = len(text.split())
    if word_count > max_words:
        max_words = word_count
        longest_comment = text

print(f"\nFeedback with longest comment ({max_words} words): '{longest_comment}'")

# Print the list of unique words used across all feedbacks
unique_words = set()
for text in feedback_data['Feedback']:
    unique_words.update(text.split())

print(f"\nList of unique words ({len(unique_words)} words):")
print(list(unique_words))

# (Optional) Sort feedbacks by rating (highest to lowest) using zip() and sorted()
print("\n--- Feedbacks Sorted by Rating (Highest to Lowest) ---")
zipped_data = zip(feedback_data['Rating'], feedback_data['S_No'], feedback_data['Name'], feedback_data['Feedback'])

# Sort based on the first item in the zipped tuple (Rating), reversed for highest to lowest
sorted_feedbacks = sorted(zipped_data, key=lambda x: x[0], reverse=True)

for rating, s_no, name, feedback in sorted_feedbacks:
    print(f"Rating: {rating} | S_No: {s_no:02d} | Name: {name:<7} | Feedback: {feedback}")