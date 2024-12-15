import argparse
import os
import yaml

from src.data.DataPreparation import DataPreparation
from src.model.ModelTraining import Train
from src.model.Model import Model_init
from src.model.ModelValidation import ModelValidation
from src.test.ModelTesting import ModelTesting

import tensorflow as tf
import dvc

def main():

    parser = argparse.ArgumentParser(description="")
    

    with open("config.yaml") as f:
        config=yaml.safe_load(f)
        print(config)
        
    num_classes,class_names,training_set,test_set=DataPreparation()
    
    model=Model_init(num_classes)
    
    hist=Train(model,training_set,test_set,)
    
    ModelValidation(hist,model,test_set,training_set)
        
    ModelTesting(model,class_names)
    
    model.save(os.getcwd()+"/models/model.h5")

if __name__ == "__main__":
    main()