"""Make DataFrame cells hashable."""
import collections
from autohash import AutoHash


def f(value):
    """Make value hashable."""
    if isinstance(value, collections.abc.Hashable):
        return value
    else:
        return AutoHash(value)


def hashable_df(df):
    """Return a DataFrame with hashable cell values."""
    return df.applymap(f)


def hashable_series(ser):
    """Return a Series with hashable values."""
    return ser.map(f)


__version__ = '0.0.6'
