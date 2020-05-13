## About
`Python 3`-based `Proof of Work` CLI tool for `Crypto Mining`.

## Usage
Currently only an `example` subcommand is implemented (see
[source](https://github.com/RagingTiger/powpy/blob/21ae75123e363706cc0582777d03a0d6b54d38ed/src/pow.py#L7-L52)
). The purpose of this subcommand is `educational` and is heavily based on the
[bitcoin wiki: Proof of Work](https://en.bitcoin.it/wiki/Proof_of_work) documentation. When executed it runs a `crypto mining simulation` using `SHA-256` with the following output:
```
$ python pow.py example
Hello, world!0 => 1312af178c253f84028d480a6adc1e25e81caa44c749ec81976192e2ec934c64
Hello, world!1 => e9afc424b79e4f6ab42d99c81156d3a17228d6e1eef4139be78e948a9332a7d8
Hello, world!2 => ae37343a357a8297591625e7134cbea22f5928be8ca2a32aa475cf05fd4266b7
Hello, world!3 => 098edd39515007adf089d1a8df453b5add12dde302549f4af79c5f3371cbbcc2
Hello, world!4 => a86de1d026a9e783b98a7d609d6037b13791e71acbb996bb5f971c05f9cdbe3d
Hello, world!5 => c81000834046e31559f9519f281257ca267ff9aa1409c97e201e96ec0b6ad99f
Hello, world!6 => d6bab161aa0d2dc55ab90b3414db2e332460744a796f408070cfb57f7e242ea9
Hello, world!7 => 02af402de37a5f2c0a2aee17eec1924c64536ba3411e065d177d70cee6ff30bc
Hello, world!8 => 86dfdfc2ff09863b3e25ed92971e37f21ff9838c0455e5b3c67daf66882e6f2f
Hello, world!9 => 9a81709a7290da8d5515cdd87afec495bd5558a0fa886682951fe127b14fe5a9
Hello, world!10 => 14e0873e3d96d95e2da26fa8c0d247e797258639c8828ec41d958b20f0225d8e
.
.
.
Hello, world!4240 => 9bf52acd113993fd569d6a4ef2916f5d88fd7cfd93f12aa79587b895a06f8671
Hello, world!4241 => c1916540254a1b47bef14f57ee48e5dfc8bf6c354b5da1724e98fe14a7a08b0c
Hello, world!4242 => bd1f27a8e576f85a75a6b77945c6c5e724d3b6bea7a1093accfe6a905b02ef66
Hello, world!4243 => 2be850f587ae69172cc6b588cee3623b6709359ab226354469a7bfc154a10f33
Hello, world!4244 => 62b100d51d8b5f04c2be7a89e9e7babf49350567cffe8f00f326a625084557c4
Hello, world!4245 => 848deec0d6123c0ed10aad31bf32e9467158db8b0d1df88e03aeeda79f291f31
Hello, world!4246 => 8e46c058ec660406a1f90e323f352512fb17327ccc64847710ae3430ac8fc4a9
Hello, world!4247 => 97f387b4d3f4cb88d2f8a28c719148500d54c87f3d506268d340dd45b3549191
Hello, world!4248 => 6e110d98b388e77e9c6f042ac6b497cec46660deef75a55ebc7cfdf65cc0b965
Hello, world!4249 => c004190b822f1669cac8dc37e761cb73652e7832fb814565702245cf26ebb9e6
    New POW found => nonce 4250
Hello, world!4250 => 0000c3af42fc31103f1fdc0151fa747ff87349a4714df7cc52ea464e12dcd4e9
Hash Value: 1350565582647790482127632554504241516291697500941742491868079705537959145
Target:     1766847064778384329583297500742918515827483896875618958121606201292619776
```
We see that the `while` loop found in the function def for `example` (see
[source](https://github.com/RagingTiger/powpy/blob/21ae75123e363706cc0582777d03a0d6b54d38ed/src/pow.py#L7-L52)),
will simply loop forever, incrementing `nonce` until a hash of the concatenation
of the `trx` (the transaction hash, in this case the string `Hello, world!`)
and the `nonce` yields a `hash` with a value less than the `target`.

In the case of this `example`, the target is set to `2^240` which has an integer
value of
`1766847064778384329583297500742918515827483896875618958121606201292619776`.
When the `nonce` value equals `4250`, is combined with the `trx` value of
`Hello, world!` (i.e. `Hello, world!4250`), and is hashed, we finally get that
magic hash `0000c3af42fc31103f1fdc0151fa747ff87349a4714df7cc52ea464e12dcd4e9`
that has a value of
`1350565582647790482127632554504241516291697500941742491868079705537959145`.

Simply by inspection we can see that this `new hash value` is less than the
`target`. Our `Proof of Work` is complete.

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

#### Run
The [`tigerj/powpy`](https://hub.docker.com/r/tigerj/powpy)image is
`multi-arch` for `arm`, `arm64`, and `amd64`:
```
$ docker run --rm -it tigerj/powpy
```
+ **Note**: This will simply run the `example` subcommand by default.

#### Build
```
$ git clone https://github.com/RagingTiger/powpy
$ cd powpy
$ docker build -t powpy .
```
