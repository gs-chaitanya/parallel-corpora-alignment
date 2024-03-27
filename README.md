# parallel-corpora-alignment

## Installation
Make sure you have installed the required apertium language packs for the source and target languages.
In this case, install apertium-eng and apertium-spa

Next, install eflomal. The steps are given below
1) Navigate to the current folder in you terminal 

    ``` cd \path\to\repostiory ```

2) clone the eflomal repository 

    ``` git clone https://github.com/robertostling/eflomal.git ```

3) cd into the repository and intall eflomal using the following command

    ```python -m pip install . ```

You are now ready to go

## Usage 
The script assumes the following files : 

1) ```<source-lang-filename>.txt``` - a file containing one sentence per line in the source language. In this case, it is called ```eng.txt```

2) ```<target-lang-filename>.txt``` - a file containing one sentence per line in the target language

### To use the script, run this in the terminal

```python alignment-script.py apertium-<source-lang>/ <source-lang-file>.txt apertium-<target-lang>/ <target-lang-filename>.txt```

### To run it as it is, use

``` python alignment-script.py apertium-eng/ eng.txt apertium-spa/ spa.txt ```