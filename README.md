# Decision Stump
A practice of decision stump.

## How to run

Start the program
```
python ArtificialData.py
python MultiDimension.py
```

## Versions

There are 2 versions, one with artificial data and one for mutidimensional data

### ArtificialData.py

The data is artificial generated as the following:
```
(a) Generate x by a uniform distribution in [−1, 1].
(b) Generate y by f(x) = ˜s(x) + noise where ˜s(x) = sign(x) and the noise flips the result with
20% probability
```

then run the decision stump algorithm on it, <br/>
and output the avg E_in and E_out.<br/>
E_out is calculated with: <br/>
0.5 + 0.3s*(|&#952;|-1)<br/>

### MultiDimension.py

The data is multidimension.<br/>
Run decision stump on each dimension and return the "best of the best".<br/>
Output &#952;, s, error rate, and best dimension<br/>
Then use the trained decision stump to predict the test data.<br/>
Output the error rate of the prediction.<br/>

## Built With

* Python 3.6.0 :: Anaconda custom (64-bit)

## Authors

* **SaKaTetsu** - *Initial work* - [SaKaTetsu](https://github.com/SaKaTetsu)