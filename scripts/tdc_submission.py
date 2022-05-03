# TDC Submission
# Ayush Noori

for seed in [1, 2, 3, 4, 5]:
    
    benchmark = group.get('Martins_BBB') 
    
    # all benchmark names in a benchmark group are stored in group.dataset_names
    predictions = {}
    name = benchmark['name']
    train_val, test = benchmark['train_val'], benchmark['test']
    train, valid = group.get_train_valid_split(benchmark = name, split_type = 'default', seed = seed)
    
        # --------------------------------------------- # 
        #  Train your model using train, valid, test    #
        #  Save test prediction in y_pred_test variable #
        # --------------------------------------------- #
        
    predictions[name] = y_pred_test
    predictions_list.append(predictions)

results = group.evaluate_many(predictions_list)
# {'caco2_wang': [6.328, 0.101]}