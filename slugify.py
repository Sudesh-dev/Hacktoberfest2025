import re  # Import the regex module to perform pattern matching and text replacement

def slugify(text: str) -> str:
    # Convert all characters to lowercase
    text = text.lower()
    
    # Replace spaces and underscores with hyphens
    text = re.sub(r'[\s_]+', '-', text)
    
    # Remove all characters except lowercase letters, digits, and hyphens
    text = re.sub(r'[^a-z0-9\-]', '', text)
    
    # Replace multiple consecutive hyphens with a single hyphen
    text = re.sub(r'-{2,}', '-', text)
    
    # Remove leading and trailing hyphens
    text = text.strip('-')
    
    # Return the cleaned, URL-safe slug
    return text

if __name__ == "__main__":
    # Ask the user to enter a string
    user_input = input("Enter a string to convert into a slug: ")
    
    # Call the slugify function and store the result
    slug = slugify(user_input)
    
    # Display the generated slug
    print("Generated slug:", slug)
