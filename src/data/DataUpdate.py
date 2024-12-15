import subprocess
import yaml
def update_dataDVC (data_ver ):
  subprocess.run([ "dvc", "add", "data/augmented_dataset"])
  subprocess.run([ "git", "add", "data/augmented_dataset.dvc" ])
  subprocess.run([ "git", "commit" , "-m", "new dataset version"+str(data_ver) ])
  tag = "v." + str(data_ver )
  subprocess.run([ "git", "tag", "-a", tag, "-m", "Dataset version" ])
  subprocess.run([ "git", "push"])
  subprocess.run([ "dvc", "push"])
  
if __name__ == "__main__" :
  with open("config.yaml") as f:
    params=yaml.safe_load(f)
  data_ver = params[ 'data_version' ]
  update_dataDVC(data_ver)