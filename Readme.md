# Lab Assignment - 3
### Execution Format: `python3 bplus.py input.txt`
- `bplus.py`: Python file with the implementation of B+ Tree with the given constraints. 
- the order of B+ tree is `3` which is assumed to be the number of child pointers a node can hold and this value is hard coded in the code.
- `input.txt`: Text file containing the queries to be applied on the implemented B+ tree. 
- Each query in the input file is supposed to be separated by `new line` in the text file and the name of the text file is supposed to be given as the input argument while executing the code. 
- `output.txt`: Text file conatining the output of the queries listed in the input file. All the ouputs are separated by new line in the output file. 
- the input file is supposed to be in the same directory in which the `bplus.py` is residing, and the output file is also created at the same location.

### Implementation Details: 
- With the order being 3, a node in the given B+ tree is supposed to be holding 2 keys. 
- `INSERT X`: for insert function, at first we traverse the tree starting from the root node to the leaf node on the last level on which the key `X` is supposed to be inserted. If in case the key is already present in the tree we just increament the count of that key, else we append the key in the node. After inserting, we check if the number of keys in the node is exceeding the maximum keys it can hold. If yes, we split the leaf node according to the rules of B+ tree.
- `FIND X`: we follow the same procedure as in the insert function, by traversing the tree from root to the appropriate leaf node. After that we traverse through the keys of the leaf node in order to check if the queried key is present or not and based on that we return the result.
- `COUNT X`: for the count function we call the `FIND` function to know if the key is present in the tree or not. If the result of the find `FIND` function is `No`, the returned value is `0`, else we traverse to the leaf node containing `X` and return the count value of it.
- `RANGE X Y`: for the range function we first find the leaf node containing `X` or the rightmost leaf node containing keys < `X`. We then start traversing through all the leaf nodes with the help of pointers pointing to the next leaf node and we return the count of number of values between `X` and `Y`.
  
