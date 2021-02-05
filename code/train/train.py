import nbformat
import oscmd
from pprint import pprint as pp
from nbconvert.preprocessors import ExecutePreprocessor

def main():
   o1, o2, o3 = oscmd.osCmdRun(["jupyter", "kernelspec", "list"])
   pp(o2.decode("utf-8"))
   o1, o2, o3 = oscmd.osCmdRun(["pwd"])
   pp(o2.decode("utf-8"))
   o1, o2, o3 = oscmd.osCmdRun(["ls", "-latr"])
   pp(o2.decode("utf-8"))
   o1, o2, o3 = oscmd.osCmdRun(["echo", "$PATH"])
   pp(o2.decode("utf-8"))
   o1, o2, o3 = oscmd.osCmdRun(["id"])
   pp(o2.decode("utf-8"))
   o1,o2,o3 = oscmd.osCmdRun(["find","/","-name","kernel.json","-print"])
   pp(o2.decode("utf-8"))
   o1,o2,o3 = oscmd.osCmdRun(["python","--version"])
   pp(o2.decode("utf-8"))
   o1,o2,o3 = oscmd.osCmdRun(["python","-m","pip","list"])
   pp(o2.decode("utf-8"))

   with open("01.run-experiment.ipynb","r") as fp:
      nb = nbformat.read(fp, as_version=4)
   ep = ExecutePreprocessor(timeout=600, kernel_name="python3"
   ep.preprocess(nb, {"metadata": {"path":"./"}})

if __name__ == "__main__":
   main()
