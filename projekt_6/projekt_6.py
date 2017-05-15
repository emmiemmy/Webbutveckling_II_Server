from flask import Flask, render_template, request, flash, redirect, jsonify
from form import ArticleForm
import json, os
from slugify import slugify

app = Flask(__name__)
# Enable CSRF secret key
app.config.from_object('config')


# App is a wikipedia where users can write, edit and read articles

# Startpage
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


# Retrive all data as JSON
@app.route('/api/articles')
def get_articles_json():
    # Open existing file content and store it in variable
    with open("/Users/emmashakespeare/Documents/HT-2016/Web-Server/projekt_6/database.json", 'r') as f:
        data = json.load(f)
    return jsonify({'articles': data})



# Retrieve all data in HTML rendered document
# All articles are presented in lists
@app.route('/articles')
def get_articles_html():
    # Open eisitng file content and store it in variable
    with open("/Users/emmashakespeare/Documents/HT-2016/Web-Server/projekt_6/database.json", 'r') as f:
        data = json.load(f)
        print(data)
    return render_template('articles.html',
                           title='Articles',
                           articles=data)


# Retrive specific article as JSON
@app.route('/api/articles/<name>')
def get_article_json(name):
    # Find article object with matching name
    article = find_article(name)

    # Return a json formatted object
    return jsonify({'article': article})


# Retrieve specified article in HTML rendered document
@app.route('/articles/<name>')
def get_article(name):
    # Call function to retrieve specified article
    article = find_article(name)

    return render_template('article.html',
                           title='Article',
                           article=article)


# Function to retrieve article specified by name
def find_article(name):
    # Open eisitng file content and store it in variable
    with open("/Users/emmashakespeare/Documents/HT-2016/Web-Server/projekt_6/database.json", 'r') as f:
        articles = json.load(f)

    # Slugify title for search
    name_slugified = slugify(name).lower()

    print("Looking for: " + name_slugified)
    # Search for specified article title, slugify title in database for exact match
    article = [article for article in articles if slugify(article['title']).lower() == name_slugified]

    # if title was not found
    if len(article) == 0:
        return "Titel not found"

    return article


# Create new article
@app.route('/new', methods=['GET', 'POST'])
def create_article():
    # create instance of form
    form = ArticleForm()

    #To make sure all required fields are filled
    if form.validate_on_submit():
        flash('Article with title: %s, content: %s' % (form.title.data, form.text.data))

        title = form.title.data

        #Create new object
        new_article = {
            'title': title,
            'text': form.text.data,
            'created_at': form.publ_date.raw_data
        }

        #If article already exists
        if find_article(title):
            delete(title)

        # save article to file
        save_article(new_article)

        #If form is to be submitted
        return render_template('/index.html',
                               art_title=form.title.data,
                               text=form.text.data,
                               created_at=form.publ_date.data,
                               message="Your article has been updated!")
    # If GET requests form
    return render_template('form_article.html',
                           title="Create new article",
                           form=form,
                           action='/new'
                           )


# Edit specified article
@app.route('/edit/<name>', methods=['POST', 'GET'])
def edit(name):
    print("EDIT route" + name)
    # find article by name
    article = find_article(name)

    # create instance of form with prefilled fields
    form = ArticleForm()
    form.title.data = article[0]['title']
    form.text.data = article[0]['text']


    return render_template('form_article.html',
                           article=article,
                           form=form,
                           action='/new'
                           )


#Delete article with specified title
@app.route('/articles/delete/<name>')
def delete(name):
    path = "/Users/emmashakespeare/Documents/HT-2016/Web-Server/projekt_6/database.json"

    # Open existing file content and store it in variable
    with open(path, 'r') as f:
        data = json.load(f)

        #Slugify data for accurate search
        slugged_name = slugify(name).lower()

    # Find element with matching name
    for i in range(len(data)):
        #Slugify title on file for accurate search
        # If found, delete object
        if slugify(data[i]['title']).lower() == slugged_name:
            print("Found: " + data[i]['title'])
            data.pop(i)

    # Save new edited data
    with open(path, 'w')as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return render_template('index.html', message="Article: " + name + " has been deleted.")


# Save article in json file
def save_article(new_article):
    print(new_article)

    # Beacause I cannot get the relative path to work...
    path = "/Users/emmashakespeare/Documents/HT-2016/Web-Server/projekt_6/database.json"
    # If there isn't a file already, create one
    if not (os.path.isfile(path)):
        print("Creating file...")
        with open(path, 'w')as f:
            json.dump([], f)  # Wrap

    # Open existing file content and store it in variable
    with open(path, 'r') as f:
        data = json.load(f)

    data.append(new_article)

    with open(path, 'w')as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return len(data)


# View handles 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', title='Page Not Found')


if __name__ == '__main__':
    app.run(debug=True)
