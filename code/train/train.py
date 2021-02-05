import nbformat
import oscmd
from pprint import pprint as pp
from nbconvert.preprocessors import ExecutePreprocessor

def main():
   pp(dir(oscmd))
   o1, o2, o3 = oscmd.osRunCmd(["jupyter", "kernelspec", "list"])
   pp(o2.decode("utf-8"))
   o1, o2, o3 = oscmd.osRunCmd(["pwd"])
   pp(o2.decode("utf-8"))
   o1, o2, o3 = oscmd.osRunCmd(["ls", "-latr"])
   pp(o2.decode("utf-8"))
   o1, o2, o3 = oscmd.osRunCmd(["echo", "$PATH"])
   pp(o2.decode("utf-8"))
   o1, o2, o3 = oscmd.osRunCmd(["id"])
   pp(o2.decode("utf-8"))
   o1,o2,o3 = oscmd.osRunCmd(["find","/","-name","kernel.json","-print"])
   pp(o2.decode("utf-8"))

   with open("01.run-experiment.ipynb","r") as fp:
      nb = nbformat.read(fp, as_version=4)
   ep = ExecutePreprocessor(timeout=600, kernel_name="Python 3.7 - AzureML")
   ep.preprocess(nb, {"metadata": {"path":"notebooks/"}})

if __name__ == "__main__":
   main()
