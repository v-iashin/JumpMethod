# JumpsMethod
*UPD: 19 Feb 2017*

## Motivation
This repository contains an attempt to replicate some of the results that were achieved in

    `Sugar, C. A., & James, G. M. (2003). Finding the number of clusters in a dataset: An information-theoretic approach. Journal of the American Statistical Association, 98(463), 750–763. JOUR.`
[link](http://www-bcf.usc.edu/~gareth/research/ratedist.pdf)

In particular, it is attempted to replicate the results that are illustrated in Figure 4.

Another reason why this repository was created is that the implementation of the Jump Method algorithm on Python cannot be found easily on the internet (I have not found any).

## Files
In the repository, one may find an article itself with the illustration of the results that is needed to replicate (`article` folder).

Also, this repository contains a Python class `jumpmethod.py` which in turn contains two functions: `Distortions` and `Jumps` that calculates vectors of distortions and jumps for a given number of clusters to check.

Finally, there is also a JupyterNotebook `Simulations (Figure 4).ipynb` which was created for illustrative explanations why the replication can be achieved.

## TODO:
1. Add the Transformed distortion curves to class (easy: this is just a cumulate of Jumps).
2. Add to the README the discription of the algorithm.
3. Replicate the Iris results (SJ, p. 12).
4. Replicate the bootstrap results (SJ, pp. 13--15).
