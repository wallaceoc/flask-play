from flask import Flask, render_template, request

app = Flask(__name__)

def get_films_from_file_split():
    with open ("film_ratings.txt", 'r') as file:
        split_lines = [line.split(',') for line in file.read().splitlines()]

    return split_lines

@app.route('/films/table')
def get_films():
    films = []

    stars_filter = request.args and request.args['stars']

    split_lines = get_films_from_file_split()    

    films = [{'film_name': film_name, 'stars': stars}
            for [film_name, stars] in split_lines
            if not stars_filter or stars == stars_filter]
             
    
    return render_template('film_table.html', films=films)