import collections
import numpy as np
from autohash import AutoHash


def hashable_df(df):
    return df.apply(np.vectorize(
                    lambda value: value if isinstance(value, collections.abc.Hashable)
                                        else AutoHash(value)))


__version__ = '0.0.2'
