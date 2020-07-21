Based on https://github.com/po5i/flask-mini-tests.git

## Setup

Create and activate the virtual environment

```bash
virtualenv venv
source venv/bin/activate
```

Run the server

```bash
python app.py
```

Run the tests

```bash
python -m pytest
```

The server will be up on [http://localhost:5000](http://localhost:5000).

## Requirements

Python >= 3.6

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## false pylint import errors & pytest test discovery failures
Add to PYTHONPATH the current folder.
### win
set PYTHONPATH=C:\path_to_project\
### mac & LIN
export PYTHONPATH='/path_to_project/'
