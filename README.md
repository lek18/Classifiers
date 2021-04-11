## Running the code:
Code Structure:
```buildoutcfg
|---src     # source code
|---main.py # main entry point of code
```

#Running the code:
0. Works best in pycharm as pycharm adds python path to code.
1. Python >=3.9 and pip install required requirements.txt
2. python main.py "path to data set"


##Running code from docker
1. Install docker in your system
2. Run `docker run -v ${PWD}:/data lek1992/churn-docker101:v0.0.1`
3. Feature importance values will be saved in $PWD
