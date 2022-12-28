def generate_meta_tags():
  # Initialize an empty list to store the meta tags
  meta_tags = []

  # Loop 50 times to generate 50 meta tags
  for i in range(1):
    # Prompt the user to enter the title
    title = input("Enter the title for the website: ")

    # Prompt the user to enter the description
    description = input("Enter a description for the website: ")

    # Prompt the user to enter the keywords
    keywords = input("Enter a list of keywords for the website (separated by commas): ")

    # Prompt the user to enter the author
    author = input("Enter the author of the website: ")

    # Prompt the user to enter the copyright information
    copyright = input("Enter the copyright information for the website: ")

    # Prompt the user to enter the viewport size
    viewport = input("Enter the viewport size for the website (e.g. width=device-width, initial-scale=1.0): ")

    # Create the title meta tag
    title_tag = f'<title>{title}</title>'

    # Create the description meta tag
    description_tag = f'<meta name="description" content="{description}">'

    # Create the keywords meta tag
    keywords_tag = f'<meta name="keywords" content="{keywords}">'

    # Create the author meta tag
    author_tag = f'<meta name="author" content="{author}">'

    # Create the copyright meta tag
    copyright_tag = f'<meta name="copyright" content="{copyright}">'

    # Create the viewport meta tag
    viewport_tag = f'<meta name="viewport" content="{viewport}">'

    # Add all of the meta tags to the list
    meta_tags.append(title_tag + description_tag + keywords_tag + author_tag + copyright_tag + viewport_tag)

  # Return the list of meta tags
  return meta_tags

# Test the function
meta_tags = generate_meta_tags()
print(meta_tags)
