import yaml
def Train(model,training_set,test_set):
    
    with open("config.yaml") as f:
        config=yaml.safe_load(f)
        print(config)
    
    batch_size,optimizer,epochs,=config["batch_size"],config["optimizer"],config["epochs"]
        
    model.compile(optimizer = optimizer, loss = 'categorical_crossentropy', metrics = ['accuracy'])
    history= model.fit(training_set,
                            epochs = epochs,batch_size=batch_size,
                            validation_data = test_set)
    # list all data in history
    print(history.history.keys())
    return history

if __name__ == "__main__" :
  
  with open("dvc.yaml") as f:
    params=yaml.safe_load(f)
    
  model = Train(params)