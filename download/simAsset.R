#!/usr/bin/Rscript

## -----------------------------------------------------------------------------
# Generate sample paths for assets assuming geometric Brownian motion.
#
# Inputs: CSV file with the following columns:
#   S0 - stock price today (e.g., 50)
#   mu - expected return (e.g., 0.04)
#   sigma - volatility (e.g., 0.1)
#   dt - size of time steps (e.g., 0.273)
#   nsteps - number of time steps to simulate
#   nsims - number of simulation paths to generate
#
# Output:
#   - "resultN.csv" dump of a matrix where each column
#     represents a simulated asset price path.
#   - "resultN.pdf" line plot of all simulated price path
#
# Notes: This code focuses on details of the implementation of the
#        Monte-Carlo algorithm.
#        It does not contain any programatic essentials such as error
#        checking.
#        It does not allow for optional/default input arguments.
#        It is not optimized for memory efficiency nor speed.
#
# Original MATLAB code by Phil Goddard (phil@goddardconsulting.ca), Date: Q2, 2006
# Adapted to R by Riccardo Murri <riccardo.murri@gmail.com>, 2016-11-16
#
## -----------------------------------------------------------------------------


assetPaths <- function(S0, mu, sigma, dt, steps, nsims) {

  ## calculate the drift
  nu <- mu - sigma*sigma/2;

  ## Generate potential paths:

  # all paths start at (relative) price 1
  top <- rep(1, nsims);  # vector of 1's

  # generate random matrix with `steps` rows and `nsims` columns
  # (`apply(matrix, 1, fn)` => apply `fn` to each row of matrix;
  # `apply(matrix, 2, fn)` => apply `fn` to each column of matrix)
  rnd <- t(apply(matrix(c(NA), steps, nsims), 1, function(x) { rnorm(nsims); }));

  # compute paths
  X <- exp(nu*dt + sigma*sqrt(dt)*rnd);
  Y <- apply(X, 2, cumprod);  # column-wise cumulative product
  relpaths <- rbind(top, Y);

  # multiply by initial price S0 to get the final result
  S0 * relpaths;
}


plotPaths <- function(S, filename) {
  pdf(filename, 13, 10);
  
  data <- t(S)
  nsims <- dim(data)[1]
  nsteps <- dim(data)[2]

  # get the range for the x and y axis
  xrange <- c(1, nsteps)
  yrange <- range(data)

  # set up the plot
  plot(xrange, yrange, type="n",
     xlab="Time to expiry (days)",
     ylab="Asset Value (US$)" )
  colors <- rainbow(nsims)
  linetype <- c(1:nsims)
  plotchar <- seq(18,18+nsims,1)

  # add lines
  for (i in 1:nsims) {
    lines(1:nsteps, data[i,], type="b", lwd=1.5,
      lty=linetype[i], col=colors[i], pch=plotchar[i])
  }

  # add a title and subtitle
  title("Asset Pricing", "simulated pricing")

  # add a legend
  legend(xrange[1], yrange[2], 1:nsims, cex=0.8, col=colors,
    pch=plotchar, lty=linetype, title="Simulation path");
}


## -----------------------------------------------------------------------------
## Commands to run simulation
## -----------------------------------------------------------------------------

## get arguments from command line
args <- commandArgs(TRUE)
infile <- args[1];

inputs <- read.csv(infile, header=FALSE, col.names=c('S0', 'mu', 'sigma', 'dt', 'nsteps', 'nsims'));

for (i in 1:dim(inputs)[1]) {
    dat <- inputs[i,];

    ## Generate potential future asset paths
    S <- assetPaths(dat$S0, dat$mu, dat$sigma, dat$dt, dat$nsteps, dat$nsims);

    ## write out results
    write.table(t(S), paste("result", i, ".csv", sep=''), row.names=FALSE, col.names=FALSE, sep=",");
    plotPaths(S, paste("result", i, ".pdf", sep=''));
}
