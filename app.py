from json import dumps

from flask import Flask

app = Flask(__name__)


@app.route('/test', defaults={'file_name': 'file1.txt', 'start_line': 0, 'end_line': None}, methods=['GET'])
@app.route('/test/<path:file_name>', defaults={'start_line': 0, 'end_line': None}, methods=['GET'])
@app.route('/test/<int:start_line>/<int:end_line>', defaults={'file_name': 'file1.txt'}, methods=['GET'])
@app.route('/test/<path:file_name>/<int:start_line>/<int:end_line>', methods=['GET'])
def red_file(file_name, start_line, end_line):

    number_of_lines_read = 0
    lines = list()
    try:
        with open(file_name) as f:
            for line in f:
                if start_line <= number_of_lines_read:
                    if not end_line or number_of_lines_read <= end_line:
                        lines.append(line.split(':')[1].strip())
                number_of_lines_read += 1
    except FileNotFoundError:
        return dumps({'message': "The file don't exist"})
    json_data = {
        'file_name': file_name,
        'number_of_lines_read': number_of_lines_read,
        'lines': lines,
    }

    return dumps(json_data)


if __name__ == '__main__':
    app.run()
