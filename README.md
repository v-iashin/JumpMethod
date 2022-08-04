# The Implementation of the Jump Clustering Algorithm on Python

## Motivation
This repository contains an attempt to replicate some of the results that were
achieved in

[Sugar, C. A., & James, G. M. (2003). Finding the number of clusters in a
dataset: An information-theoretic approach. Journal of the American
Statistical Association, 98(463), 750–763. JOUR.](http://faculty.marshall.usc.edu/gareth-james/Research/ratedist.pdf)

In particular, it is attempted to replicate the results that are illustrated
in Figure 4.

Another reason why this repository was created is that the implementation of
the Jump Method algorithm on Python cannot be found easily on the internet (I
have not found any).

## Files
Also, this repository contains a Python class `jumpmethod.py` which in turn
contains two functions: `distortions` and `jumps` that calculate vectors of
distortions and jumps for a given number of clusters to check.

To use this:
```python
jm = JumpsMethod(data)
jm.distortions()
jm.jumps()
number_cluster = jm.number_clusters()
```

Finally, there is also a JupyterNotebook `Simulations (Figure 4).ipynb` which
was created for illustrative explanations why and how the replication can be
achieved.

## TODO:
1. Add the Transformed distortion curves to the class (easy: this is just a
   cumulate of Jumps).
2. Add the description of the algorithm to the README.
3. Replicate the Iris results (SJ, p. 12).
4. Replicate the bootstrap results (SJ, pp. 13--15).
5. Performance check (may be improvements).
