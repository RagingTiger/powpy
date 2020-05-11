# python's standard hashing library
import hashlib

# class for proof of work
class POW:

  def example(self):
    # string representing base transaction hash
    trx = "Hello, world!"

    # integer representing the number that will be incremented
    nonce = 0

    # number that our  hash of trx+nonce must be smaller than
    target = 2**240

    # get pow
    while True:
      # append nonce to end of transaction hash (e.g. Hello World)
      mtrx = '{}{}'.format(trx, nonce)

      # get SHA-256 hash of modified transaction hash in hexadecimal
      new_hash = hashlib.sha256(mtrx.encode('utf-8')).hexdigest()

      # convert new hexadecimal hash to integer
      int_hash = int(new_hash, 16)

      # check if new hash value is lower than target value
      if  int_hash < target:
        # show that a nonce has been found that yields the desired hash
        print('    New POW found => nonce {}'.format(nonce))

        # show the concatenated trx+nonce and hash
        print('{} => {}'.format(mtrx, new_hash))

        # show the integer value of the new concatenate trx+nonce hash
        print('Hash Value: {}'.format(int_hash))

        # show the integer value of the target
        print('Target:     {}'.format(target))

        # leave the loop
        break

      # else keep looking for that magic nonce babay!!!! waste those cycles!!!
      else:
        # show the concatenated trx+nonce and hash
        print('{} => {}'.format(mtrx, new_hash))

        # increase nonce by adding one to it and then start from loop top
        nonce += 1


# executable section
if __name__ == '__main__':
    # get fire lib for CLI work
    import fire

    # open fire full blast
    fire.Fire(POW)
