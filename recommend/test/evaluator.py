import pprint

def evaluate(test_users_data, recommendation):
    #precision: tp/(tp+fp)
    #recall : tp/(tp+fn);
    tp = 0
    all_real = 0
    all_predict = 0
    #pprint.pprint(recommendation)
    for user, real_movies in test_users_data.items():
        predict = set(recommendation[user])
        tp += len( real_movies & predict )
        all_real += len(real_movies)
        all_predict += len(predict)
    tp = tp*1.0
    precision = tp/all_predict
    recall = tp/all_real
    return (precision, recall)