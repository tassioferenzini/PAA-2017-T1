# PAA 2017-1

The purpose of this project is to solve the list of problem 1.


### How to run

```
./trabalho <instance_path> <question>
```

where:
* Question **1** is the 
* Question **2a** is the fractional knapsack problem - O(nlogn)
* Question **3** is the 


**Example**
```
./trabalho path 2a
```


### Instance Format

**Input format to Question 2**

The input file should be in the following format:

```
NbItems
<< And then for each item >>
Index Profit Weight
KnapsackSize
```

**Output format to Question 2**

The output file should be in the following format:

```
NbItemsUsed TotalWeight TotalProfit
<< And then for each item placed in the knapsack >>
ItemIndex FractionOfItem
```

**Some remarks**
** The second field "FractionOfItem" belongs between [0,1].



