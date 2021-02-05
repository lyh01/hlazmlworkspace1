import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def main():
   with open("01.run-experiment.ipynb","r") as fp:
      nb = nbformat.read(fp, as_version=4)
   ep = ExecutePreprocessor(timeout=600, kernel_name="Python 3.7 - AzureML")
   ep.preprocess(nb, {"metadata": {"path":"notebooks/"}})
if __name__ == "__main__":
   main()
