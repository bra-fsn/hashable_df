# hashable_df

If you have ever tried to use native python objects in Pandas DataFrames,
you may have run into an issue similar to this:

```python
df = pd.DataFrame({"A": [1, 2, 3, 4],
                   "B": ["a", "b", "c", "d"],
                   "C": [[1, 2, 3], [1, 2], [1, 2, 3], 4],
                   "D": [{1: 1, 2: 2}, {1: 1, 3: 3}, {1: 1, 4: 4}, {1: 1, 2: 2}],
                   "E": [[{1: {2: 2}}, {2: {3: 3}}], [{1: {2: 2}}, {2: {3: 3}}],
                         [{1: {2: 2}}, {2: {3: 3}}], [{1: {2: 2}}, {2: {3: 3}}]]
                   })
df['C'].unique()
```

`TypeError: unhashable type: 'list'`

This is caused by unhashable values in the DataFrame cells.

This small library helps to resolve that making this possible:

```python
from hashable_df import hashable_df
hashable_df(df)['E'].unique()
```

returning
```
hashable_df(df)['E'].unique()
```
