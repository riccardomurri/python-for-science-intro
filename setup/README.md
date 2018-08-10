This directory describes how a Jupyter notebook server for running the
course is usually set up, and collects the relevant scripts and
configuration snippets.  It is anyway possible to run the course on
almost any Jupyter notebook server -- you do not need to use this
exact set up.

1. Create a Jupyter notebook server using [ElastiCluster][1] with the
   `jupyterhub.conf` configuration file found in this directory::

        elasticluster -c jupyterhub.conf start --no-setup ju16

2. Use the Ansible playbook `setup.yml` (in this directory) to create
   user accounts and deploy additional scripts (note there is a space
   between `--` and `setup.yml`):

        elasticluster -c jupyterhub.conf setup -- setup.yml

   **Note:** Cleartext passwords are hard-coded in `setup.yml` and
   `accounts.tex`; the two must match!

3. Edit the LaTeX file `accounts.tex` (fill in the actual IP address
   and/or hostname of the Jupyterhub server) and use the PDF file to
   print out credential sheets to hand out to course participants.

   **Note:** Cleartext passwords are hard-coded in `setup.yml` and
   `accounts.tex`; the two must match!


<!-- References -->
[1]: http://elasticluster.readthedocs.io/en/latest/install.html#quickstart
