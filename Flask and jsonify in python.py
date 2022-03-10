from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'helloo world!'
@app.route('armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n > 0):
        digit = n % 10
        sum = digit ** order
        n = n//10
    if sum == copy_n:
        print(f"{copy_n} is an armstrong number")
        result = {
            "number": copy_n,
            "armstrong": True,
            "server IP": "122.234.213.53",
            "other numbers": [1, 23, 43, 5, 3]

        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            "number": copy_n,
            "armstrong": False,
            "server IP": "122.234.213.53",
            "other numbers": [1, 23, 43, 5, 3]

        }

    return jsonify(result)


if __name__ == "__main__":

    app.run(debug=True)