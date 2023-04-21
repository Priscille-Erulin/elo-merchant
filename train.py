from sklearn.model_selection import train_test_split
import lightgbm as lgb

# input: dataframe with features
# output: loyalty score

# first_active_month,card_id,feature_1,feature_2,feature_3,target
def train(df_train):
    X_train, X_test, y_train, y_test = train_test_split(df_train, test_size=0.33)
    tr_lgb(X_train, X_test)

def tr_lgb():
    # fix wheel problems with lightgbm
    # add kfold function
    return 0
    



# dataframe