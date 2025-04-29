# pytestzoo

![coverage badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/rbturnbull/8dcb24262e0971e8a9cd6336a0c628c4/raw/coverage-badge.json)](https://pytestzoo.github.io/rbturnbull/coverage/)

A demo repository to demonstrate testing in Python using `pytest` and `coverage`.

## Sayings of the wise

- If you don't test your code, your users will
- Untested code is broken code — you just don't know it yet.
- If someone breaks your code and it was untested, then you broke your code.
- Testing is the engineering version of 'measure twice, cut once.’
- Tests are the safety net that lets you move fast without breaking things
- You can write tests now, or you can debug later — with interest
- If it isn't tested, it shouldn't be in main.

## Install the dependencies

```bash
poetry install
```
or 
```bash
pip install -e .
```

## Run the tests

```bash
pytest
```

## Run the tests with coverage

```bash
coverage run -m pytest
```

See the coverage report by:

```bash
coverage report
```

View this in HTML format:

```bash
coverage html
```

Then open the `htmlcov/index.html` file in your browser.

## Credits

[Robert Turnbull](https://robturnbull.com) Melbourne Data Analytics Platform (MDAP)

