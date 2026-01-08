# Fibonacci Web Server
Simple Fibonacci web server.

## Interview
Please see [INTERVIEW.md](INTERVIEW.md) for instructions.


!! Candidate usage notes added to [README.md](./python/README.md).

This design uses Python, Github actions, and helm. 

The Python project packages and builds with Poetry. This was a design choice based off of ergonomics and experience with Poetry, however, could easily be swapped for uv, pipenv, or another dependency manager. 

Tests are written in pytest. 

For building and deploying many of the operations are baked into the Makefile. 