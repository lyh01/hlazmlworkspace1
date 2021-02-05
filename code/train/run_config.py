import logging
from azureml.core import Workspace, Experiment, ScriptRunConfig
def main(workspace):
    """
      input: workspace
      output: ScriptRunConfig
      
      For more information see: https://github.com/Azure/aml-run 

    """
    logging.info(f"run_config")
    return ScriptRunConfig(
         source_directory=".", script="train.py", compute_target="amlcompute3"
         )
