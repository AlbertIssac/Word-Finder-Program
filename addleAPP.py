from flask import Flask, request, render_template, jsonify, session, redirect, url_for
import os

app = Flask(__name__)
# Set a secret key for the session to work
app.secret_key = os.urandom(24)  # You can use a random key or set your own string key

# Load the word list from the file
with open('words.txt', 'r') as file:
    words = [line.strip() for line in file.readlines()]

# Function to search for words based on inclusion criteria
def search_word(word_list, criteria):
    result = []
    
    for word in word_list:
        word = word.strip()
        if len(word) != 5:  # Ensure the word is exactly 5 characters long
            continue
        match = True
        
        for position, letter in criteria.items():
            if letter != '':  # Ignore positions with ' ' (any letter allowed)
                if word[position - 1].upper() != letter.upper():
                    match = False
                    break
        
        if match:
            result.append(word)
    
    return result

# Function to search for words excluding certain letters at specific positions
def search_word_excluding(word_list, exclude_letters):
    result = []
    
    for word in word_list:
        word = word.strip()
        if len(word) != 5:  # Ensure the word is exactly 5 characters long
           continue

        exclude = False
        
        for letter in exclude_letters:
            if letter in word.upper():  # If the letter is found in the word, exclude it
                exclude = True
                break
        
        if not exclude:
            result.append(word)
    
    return result

# Function to search for words with certain letters present anywhere in the word
def search_word_with_present_letters(word_list, present_letters):
    result = []
    
    for word in word_list:
        word = word.strip()
        if len(word) != 5:  # Ensure the word is exactly 5 characters long
            continue
        contains_all = all(letter.upper() in word.upper() for letter in present_letters)
        
        if contains_all:
            result.append(word)
    
    return result

@app.route('/', methods=['GET', 'POST'])
def search():
    
    # Initialize session variable if it's not already initialized
    if 'filtered_words' not in session:
        session['filtered_words'] = words  # Default to all words if no previous session


    # If the user has made a search request (POST method)
    if request.method == 'POST':
        # Retrieve the user input for each letter position from the form data
        letter1 = request.form.get('letter1', '').strip()
        letter2 = request.form.get('letter2', '').strip()
        letter3 = request.form.get('letter3', '').strip()
        letter4 = request.form.get('letter4', '').strip()
        letter5 = request.form.get('letter5', '').strip()
        
        # Treat empty fields as '-'
        letter1 = '' if not letter1 else letter1
        letter2 = '' if not letter2 else letter2
        letter3 = '' if not letter3 else letter3
        letter4 = '' if not letter4 else letter4
        letter5 = '' if not letter5 else letter5

        # Store the input in a dictionary for search criteria
        inclusion_criteria = {1: letter1, 2: letter2, 3: letter3, 4: letter4, 5: letter5}

        # Perform the first search based on inclusion criteria
        included_words = search_word(session['filtered_words'], inclusion_criteria)
        
        # Get the input for letters that should be excluded anywhere in the word
        exclude_letters = request.form.get('exclude_letters', '').strip().upper()
        if exclude_letters:
            exclude_letters = [char for char in exclude_letters]  # Split into individual letters
        
        # Perform the second search based on exclusion criteria
        filtered_words = search_word_excluding(included_words, exclude_letters)
        
        # Get the input for letters that should be present anywhere in the word
        present_letters = request.form.get('present_letters', '').strip().upper()
        if present_letters:
            present_letters = [char for char in present_letters]  # Split into individual letters
           
            # Filter the words further based on the presence of certain letters
            filtered_words = search_word_with_present_letters(filtered_words, present_letters)
        
        
        # Update session with the filtered words
        session['filtered_words'] = filtered_words
        
        # Return the result in JSON format (for easy reading in browser)
        return render_template('index.html', 
                        letter1=letter1, 
                        letter2=letter2, 
                        letter3=letter3, 
                        letter4=letter4, 
                        letter5=letter5, words=filtered_words, search=True)

    return render_template('index.html', search=False)

# Reset route to clear search results and start a new search
@app.route('/reset', methods=['GET'])
def reset():
    # Clear the session and reset the filtered words list
    session.pop('filtered_words', None)
    return redirect(url_for('search'))  # Redirect back to the main search page

if __name__ == '__main__':
    app.run(debug=True)