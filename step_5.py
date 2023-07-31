from flask import Flask, render_template, request

app = Flask(__name__)

def get_films_from_file():
    with open ('film_ratings.txt', 'r') as file:
        split_lines = [line.split(',') for line in file.read().splitlines()]

    return split_lines

@app.route('/films/table')
def get_films():
    films = []

    stars_filter = request.args and request.args['stars']

    split_lines = get_films_from_file()    

    films = [{'film_name': film_name, 'stars': stars}
            for [film_name, stars] in split_lines
            if not stars_filter or stars == stars_filter]
             
    
    return render_template('film_table.html', films=films)

@app.route('/films/submit', methods=['GET'])
def get_form():
    return render_template("file_submit.html", message=None)

@app.route('/films/submit', methods=['POST'])
def add_film():

    title = request.form['film-name']
    stars = request.form['stars']

    with open('film_ratings.txt', 'a') as file:
        file.write(f'{title},{stars}\n')
        #file.write(f"{request.form['film-name']},{request.form['stars']}\n")

    return render_template('file_submit.html', message={"content": "Successfully added film"})

if __name__ == '__main__':
    app.run()