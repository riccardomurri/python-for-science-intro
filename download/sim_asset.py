#! /usr/bin/env python

## -----------------------------------------------------------------------------
# Generate sample paths for assets assuming geometric Brownian motion.
#
# Inputs: S0 - stock price today (e.g., 50)
#       : mu - expected return (e.g., 0.04)
#       : sig - volatility (e.g., 0.1)
#       : dt - size of time steps (e.g., 0.273)
#       : etime - days to expiry (e.g., 1000)
#       : nsims - number of simulation paths to generate
#
# Output:
#   - "results.csv" dump of a matrix where each column
#     represents a simulated asset price path.
#   - "results.pdf" line plot of all simulated price path
#
# Notes: This code focuses on details of the implementation of the
#        Monte-Carlo algorithm.
#        It does not contain any programatic essentials such as error
#        checking.
#        It does not allow for optional/default input arguments.
#        It is not optimized for memory efficiency nor speed.
#
# Original MATLAB code by Phil Goddard (phil@goddardconsulting.ca), Date: Q2, 2006
# Adapted to NumPy by Riccardo Murri <riccardo.murri@gmail.com>, 2017-06-08
#
## -----------------------------------------------------------------------------

import numpy as np


def asset_paths(S0, mu, sigma, dt, steps, nsims):
    # calculate the drift
    nu = mu - sigma*sigma/2

    ## Generate potential paths:


    # generate random matrix with `steps` rows and `nsims` columns
    rnd = np.random.randn(steps, nsims)

    # compute paths
    X = np.exp(nu*dt + sigma*np.sqrt(dt)*rnd)
    Y = np.cumprod(X, axis=0)

    # all paths start at (relative) price 1
    top = np.ones([1, nsims]) # 1 x nsims matrix of 1's
    relpaths = np.concatenate((top, Y), axis=0)

    # multiply by initial price S0 to get the final result
    return (S0 * relpaths)


## -----------------------------------------------------------------------------
## Commands to run simulation
## -----------------------------------------------------------------------------

if __name__ == '__main__':
    import sys

    ## get arguments from command line
    S0 = int(sys.argv[1])       # Price of underlying today
    mu = float(sys.argv[2])     # expected return
    sig = float(sys.argv[3])    # expected volatility
    dt  = float(sys.argv[4])    # time steps
    etime = int(sys.argv[5])  # days to expiry
    nsims = int(sys.argv[6])  # Number of simulated paths

    ## Generate potential future asset paths
    S = asset_paths(S0, mu, sig, dt, etime, nsims)

    ## write out results
    from csv import writer
    with open("results.csv", 'w') as stream:
        output = writer(stream)
        n_rows, n_cols = S.shape
        for j in range(n_cols):
            col = S[:, j]
            output.writerow(col)
