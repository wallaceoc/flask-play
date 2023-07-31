from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

def get_films_from_file():
    with open ("film_ratings.txt", 'r') as f:
        lines = f.read().splitlines()
    return lines

def get_films_from_file_split():
    with open ("film_ratings.txt", 'r') as file:
        split_lines = [line.split(',') for line in file.read().splitlines()]

    return split_lines

@app.route('/films/list')
def get_films():
    list = get_films_from_file()
    return render_template('film_list.html', films=list)

@app.route('/films/list_two')
def get_films2():
    return app.send_static_file("filmlist.html")

@app.route('/films/table')
def get_table():
    print("test1")
    films = []

    split_lines = get_films_from_file_split()
 
    films = [{'film_name': film_name, 'stars': stars}
             for [film_name, stars] in split_lines]
    
    return render_template('film_table.html', films=films)


#if __name__ == '__main__':
#    app.run()