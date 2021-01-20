# The-RSA-Cryptosystem
The RSA Public Key Cryptosystem


This cryptosystem is one the initial system. It remains most employed cryptosystem even today. The system was invented by three scholars Ron Rivest, Adi Shamir, and Len Adleman and hence, it is termed as RSA cryptosystem.

We will see two aspects of the RSA cryptosystem, firstly generation of key pair and secondly encryption-decryption algorithms.

Generation of RSA Key Pair
Each person or a party who desires to participate in communication using encryption needs to generate a pair of keys, namely public key and private key. The process followed in the generation of keys is described below −

Generate the RSA modulus (n)

Select two large primes, p and q.

Calculate n=p*q. For strong unbreakable encryption, let n be a large number, typically a minimum of 512 bits.

Find Derived Number (e)

Number e must be greater than 1 and less than (p − 1)(q − 1).

There must be no common factor for e and (p − 1)(q − 1) except for 1. In other words two numbers e and (p – 1)(q – 1) are coprime.

Form the public key

The pair of numbers (n, e) form the RSA public key and is made public.

Interestingly, though n is part of the public key, difficulty in factorizing a large prime number ensures that attacker cannot find in finite time the two primes (p & q) used to obtain n. This is strength of RSA.

Generate the private key

Private Key d is calculated from p, q, and e. For given n and e, there is unique number d.

Number d is the inverse of e modulo (p - 1)(q – 1). This means that d is the number less than (p - 1)(q - 1) such that when multiplied by e, it is equal to 1 modulo (p - 1)(q - 1).

This relationship is written mathematically as follows

![](https://latex.codecogs.com/svg.latex?ed%20%3D%201%20mod%20%28p-1%29%28q-1%29)

Example
An example of generating RSA Key pair is given below. (For ease of understanding, the primes p & q taken here are small values. Practically, these values are very high).

Let two primes be p = 7 and q = 13. Thus, modulus n = pq = 7 x 13 = 91.

Select e = 5, which is a valid choice since there is no number that is common factor of 5 and (p − 1)(q − 1) = 6 × 12 = 72, except for 1.

The pair of numbers (n, e) = (91, 5) forms the public key and can be made available to anyone whom we wish to be able to send us encrypted messages.

Input p = 7, q = 13, and e = 5 to the Extended Euclidean Algorithm. The output will be d = 29.

Check that the d calculated is correct by computing

![](https://latex.codecogs.com/svg.latex?de%20%3D%2029%5Ctimes%205%3D145%3D1%20mod%20%2872%29)

