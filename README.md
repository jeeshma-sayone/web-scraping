# web-scraping

# ============================================
# Implementing Web Scraping in Python with BeautifulSoup
# ============================================


# Step 1: Installing the required third-party libraries

        pip install requests
        pip install html5lib
        pip install bs4

# Step 2: Accessing the HTML content from webpage 
        import requests
        URL = "your url"
        r = requests.get(URL)
        print(r.content)

# Step 3: Parsing the HTML content 
        soup = BeautifulSoup(r.content, 'html5lib')
        print(soup.prettify())

        We create a BeautifulSoup object by passing two arguments:
        
        1) r.content : It is the raw HTML content.
        2) html5lib : Specifying the HTML parser we want to use.

        soup.prettify() is printed, it gives the visual representation of the parse tree created from the raw HTML content.


# Step 4: Searching and navigating through the parse tree

    todo
