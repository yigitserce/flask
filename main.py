from flask import Flask, render_template, request

app = Flask(__name__)

headings = ("Ad", "Soyad", "TC", "İl", "İlçe", "Mahalle", "Telefon Numarası")
data = []

@app.route('/loadData', methods=['POST'])
def load_data():
    data.clear()
    args = request.json
    for i in args:
        data.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
    return 200


@app.route('/')
def main():
    return render_template("table.html", headings=headings, data=data)


if __name__ == '__main__':
    app.debug = True
    app.run()
