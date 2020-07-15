"""Modules for building and running indicators.

Technical indicators are used to see past trends and anticipate future moves.
See [Using Technical Indicators to Develop Trading Strategies](https://www.investopedia.com/articles/trading/11/indicators-and-strategies-explained.asp).

## Indicator factory

The indicator factory class `vectorbt.indicators.factory.IndicatorFactory` offers a convenient way to create
technical indicators of any complexity. By providing it with information such as calculation functions and
the names of your inputs, parameters, and outputs, it will create a stand-alone indicator class
capable of running the indicator for an arbitrary combination of your inputs and parameters. It also
creates methods for signal generation and supports common pandas and parameter indexing operations.

```python-repl
>>> import pandas as pd
>>> import vectorbt as vbt

>>> # Create indicator class
>>> MyInd = vbt.IndicatorFactory(
...     ts_names=['ts'],
...     param_names=['param1', 'param2'],
...     output_names=['output']
... ).from_apply_func(
...     lambda ts, param1, param2: ts * param1 + ts * param2
... )

>>> # Create indicator instance
>>> myind = MyInd.from_params(pd.Series([1, 2, 3]), [1, 2], [3, 4], param_product=True)
>>> print(myind.output)
custom_param1       1       2
custom_param2   3   4   3   4
0               4   5   5   6
1               8  10  10  12
2              12  15  15  18
>>> print(myind[(1, 3)].output)
0     4
1     8
2    12
Name: (1, 3), dtype: int64
```

## Basic

`vectorbt.basic` provides a collection of basic technical trading indicators, such as Bollinger Bands,
all built with `vectorbt.indicators.factory.IndicatorFactory`.

You can access all the indicators either by `vbt.*` or `vbt.indicators.*`.

```python-repl
>>> # vectorbt.indicators.basic.MA
>>> vbt.MA.from_params(pd.Series([1, 2, 3]), [2, 3]).ma
ma_window     2     3
ma_ewm    False False
0           NaN   NaN
1           1.5   NaN
2           2.5   2.0
```

## Numba-compiled functions

`vectorbt.indicators.nb` provides an arsenal of Numba-compiled functions that are used by indicator
classes. These only accept NumPy arrays and other Numba-compatible types.
"""

from vectorbt.indicators import factory, basic, nb

from vectorbt.indicators.factory import IndicatorFactory
from vectorbt.indicators.basic import (
    MA,
    MSTD,
    BollingerBands,
    RSI,
    Stochastic,
    MACD,
    ATR,
    OBV
)