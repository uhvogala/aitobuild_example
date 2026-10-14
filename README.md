# aitobuild Example

Minimal Python target for supervised aitobuild delivery trials.

Run tests with Python 3.14+ and pytest installed:

```sh
python -B -m pytest -p no:cacheprovider -q
```

Trial implementation runs use disposable checkouts. Publishing a trial result
requires a separate approval.

## Using `square`

`square` from `src/demo_app/math_ops.py` is documented by the signature
`square(value: int) -> int`, which returns the square of an integer value.

```python
from demo_app.math_ops import square
print(square(3))  # 9
print(square(-3))  # 9
print(square(0))  # 0
```