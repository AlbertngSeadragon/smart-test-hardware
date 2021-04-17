from flask_cors import cross_origin
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/getchartdata", methods=['GET', 'POST'])
@cross_origin()
def submit():
    if request.method == 'POST':
        #json_data = request.json
        request_data = request.json

        return {
            "Linechartyearshowmonth": [
                [
                    210
                ],
                [
                    79
                ],
                [
                    170
                ],
                [
                    130
                ],
                [
                    242
                ],
                [
                    201
                ],
                [
                    200
                ],
                [
                    159
                ],
                [
                    236
                ],
                [
                    30
                ],
                [
                    264
                ],
                [
                    348
                ]
            ],
            "Year": [
                [
                    "Peter     ",
                    22
                ],
                [
                    "Rex         ",
                    12
                ],
                [
                    "Sam        ",
                    83
                ],
                [
                    "Laurence           ",
                    17
                ],
                [
                    "Winnie       ",
                    51
                ],
                [
                    "Cindy           ",
                    260
                ]
            ],
            "Month": [
                [
                    "Cantoneses       ",
                    1513
                ],
                [
                    "Music Festival      ",
                    104
                ],
                [
                    "CSCI3100 Software Engineering  ",
                    208
                ]
            ],
            "typeofitem": [
                [
                    "Success",
                    166
                ],
                [
                    "Failure      ",
                    265
                ],
            ]
        }
    return 'Cant Retrieve'


if __name__ == '__main__':
    app.debug = True
    app.run()
