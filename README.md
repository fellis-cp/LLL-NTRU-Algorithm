
Python implementation of the LLL (Lenstra-Lenstra-Lovász) lattice reduction algorithm. The LLL algorithm is used in lattice-based cryptography and mathematics for lattice reduction.
## Authors

- [fellis-cp](https://github.com/fellis-cp)
- [nisaaa7](https://github.com/nisaaa7)


## Usage

before using it you need to add some dependecies

```bash
  pip install scipy
```

```bash
  pip install numpy
```

and run using

```bash
 python main.py
```


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.




## Usage/Examples

```python
#your input 
mat = [[1, 0, 0, 0, 0, 1, 20, 0, 0, 20],[0, 1, 0, 0, 0, 20, 1, 20, 0, 0],[0, 0, 1, 0, 0, 0, 20, 1, 20, 0],[0, 0, 0, 1, 0, 0, 0, 20, 1, 20],[0, 0, 0, 0, 1, 20, 0, 0, 20, 1],[0, 0, 0, 0, 0, 41, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 41, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 41, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 41, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 41]]

print("contoh : ")
mat1 = create_matrix(mat)

print("mat1 : ")
print_mat(mat1)
print("mat1 is lll?", islll(mat1))

print("reduce mat : ")
mat1pass = lll_reduction(mat1)
print_mat(mat1pass)
print("mat1 is lll?", islll(mat1pass))

stop = timeit.default_timer()
print("time : ",stop - start)

