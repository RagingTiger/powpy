## About
`Python 3`-based `Proof of Work` CLI tool for `Crypto Mining`. It currently uses
`SHA-256` and is heavily based on the
[bitcoin wiki: Proof of Work](https://en.bitcoin.it/wiki/Proof_of_work)
documentation.

## Usage
Currently only an `example` subcommand is implemented (see
[source](https://github.com/RagingTiger/powpy/blob/21ae75123e363706cc0582777d03a0d6b54d38ed/src/pow.py#L7-L52)
)

## Environment Setup
Here we will discuss several ways for setting up a `Python 3` environment.

### VirtualEnv
The source code is written in `Python 3`, please bare that in mind:
```
$ git clone https://github.com/RagingTiger/powpy
$ cd powpy
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r src/requirements.txt
$ python src/pow.py example
```

### Docker
My personal choice is just to build or run the docker image.

#### Docker Run
The [`tigerj/powpy`](https://hub.docker.com/r/tigerj/powpy)image is
`multi-arch` for `arm`, `arm64`, and `amd64`:
```
$ docker run --rm -it tigerj/powpy
```
+ **Note**: This will simply run the `example` subcommand.

#### Docker Build
```
$ git clone https://github.com/RagingTiger/powpy
$ cd powpy
$ docker build -t powpy .
```
