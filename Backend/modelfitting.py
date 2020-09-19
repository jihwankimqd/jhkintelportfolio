# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

## EDA
# Objective of this section is to find insights in the preprocessed data.

def modelfitting():
    import pandas as pd

    df = pd.read_csv('processed_data.csv')
    df.head()


    # corr_matrix = df.corr()
    # corr_matrix

    # The label's (Close) correlation with other features is of interest. Features which show exceptionally low correlation to the label should be dropped. For example-> Change, Org_Volume, XR_Pct_Change have very low correlation and should be dropped.


    # from pandas.plotting import scatter_matrix
    # import matplotlib.pyplot as plt

    attributes = ['Close','Volume','Foreign_Count','DJI_Close','IR','XR']

    # Uncomment to view the plot. Plot takes up a lot of memory and time when viewed on Github and hence was commented out.

    # pd.plotting.scatter_matrix(df[attributes],figsize=(12,8),alpha=0.1)
    # plt.show()


    ### The scatter plot reveals a lot about the relationship between the features and label. Amongst the plots, there seems to be a strong postivie linear correlation between Foreign_Count, DJI_Close and Close, whilst a strong negative correlation between XR and Close. For Volume, it is less obvious, but there exists a negative linear trend with Close. As for IR, there exists specific regions of IR values shown as a group points in a '|' shape, and there seems to be linearity between increasing IR and higher Close prices.


    drop_cols = ['XR_Pct_Change']
    df.drop(drop_cols,axis=1,inplace=True)
    # df.head()


    ### There are no categorical variables to encode and transformation pipelines are not needed because the data was preprocessed in the data_preprocessing step. In hindsight, the usage of pipelines may provide cleaner code with very scalability, but at this point, for this specific project, using it would be redundant and a waste of resources.


    ## Feature Scaling
    ### Standarization vs Normalization?
    ### Standarization is much less prone to outliers, but in this specific case, some variable changes such as closing price or volume may have sudden extreme changes following a series of events (such as an earnings report/significant news). Therefore, these extremes may be regarded as outliers in standaization, and this is not desired. Extremes must be included in the data to allow a better prediction of the stock price movement. Therefore, normalization should be used for feature scaling.

    # Copy the df for testing purposes
    df_test = df
    df_test = df_test.set_index(['Date'])
    df_test['USD_Bar'] = pd.to_numeric(df_test['USD_Bar'], errors='coerce')
    # df_test['USD_Bar'].dtype
    # df_test.info()
    # df_test.head()


    from sklearn import preprocessing

    # Min-Max Standardized df_norm
    x = df_test.values 
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df_norm = pd.DataFrame(x_scaled)
    # Date,Open,High,Low,Close,Volume,DJI_Close,IR,USD_Bar,XR,XR_Pct_Change
    df_norm.columns = ['Open', 'High', 'Low', 'Close', 'Volume',
        'DJI_Close', 'IR', 'USD_Bar', 'XR']

    # df_norm.head()


    # Check for null values and fill using forward fill.

    df_norm.isnull().any()
    df_norm = df_norm.fillna(method='ffill')

    # same for df_test (non-normalized dataset)
    df_test = df_test.fillna(method='ffill')


    ## Selecting and Training a model


    # Split the data into training and testing datasets

    from sklearn.model_selection import train_test_split

    features = df_test.drop("Close", axis=1) # drop labels for training set
    labels = df_test["Close"].copy()

    X_train, X_test, y_train, y_test = train_test_split(features, labels,test_size=0.1 ,random_state=41)

    # X_train.shape


    # Linear Regression

    # from sklearn.linear_model import LinearRegression

    # lin_reg = LinearRegression()
    # lin_reg.fit(X_train, y_train)


    # print("Predictions:", lin_reg.predict(X_test))


    # from sklearn.metrics import mean_squared_error
    # import numpy as np

    # stock_predictions = lin_reg.predict(X_test)
    # lin_mse = mean_squared_error(y_test, stock_predictions)
    # lin_rmse = np.sqrt(lin_mse)
    # lin_rmse


    # 14830 KRW is roughly in the 10% range of the stock price. It's not bad, but maybe other models can fit better.


    # from sklearn.metrics import mean_absolute_error

    # lin_mae = mean_absolute_error(y_test, stock_predictions)
    # lin_mae


    # To choose which metric to test the error (although it depends on the loss function), RMSE or MAE were considered, but RMSE gives more weight to points further away from mean, and should be reference in this particular stock scenario.


    # Decision Tree Regressor

    # from sklearn.tree import DecisionTreeRegressor

    # tree_reg = DecisionTreeRegressor(random_state=41)
    # tree_reg.fit(X_train, y_train)


    # stock_predictions = tree_reg.predict(X_test)
    # tree_mse = mean_squared_error(y_test, stock_predictions)
    # tree_rmse = np.sqrt(tree_mse)
    # tree_rmse


    # The RMSE is much lower, which may either indicate overfitting or a better model.


    # Test using cross validation

    # from sklearn.model_selection import cross_val_score

    # scores = cross_val_score(tree_reg, X_train, y_train, scoring="neg_mean_squared_error", cv=10)
    # tree_rmse_scores = np.sqrt(-scores)


    # def display_scores(scores):
    #     print("Scores:", scores)
    #     print("Mean:", scores.mean())
    #     print("Standard deviation:", scores.std())

    # # Decision Tree RMSE Scores
    # display_scores(tree_rmse_scores)


    # lin_scores = cross_val_score(lin_reg, X_train, y_train, scoring="neg_mean_squared_error", cv=10)
    # lin_rmse_scores = np.sqrt(-lin_scores)

    # # Linear Regression RMSE Scores
    # display_scores(lin_rmse_scores)


    # The Decision Tree Regressor seems to be a more promising model, but there are more models to try.


    # Random Forest Regressor

    from sklearn.ensemble import RandomForestRegressor

    forest_reg = RandomForestRegressor(n_estimators=100, random_state=41)
    # forest_reg.fit(X_train, y_train)


    # stock_predictions = forest_reg.predict(X_test)
    # forest_mse = mean_squared_error(y_test, stock_predictions)
    # forest_rmse = np.sqrt(forest_mse)
    # forest_rmse


    # forest_scores = cross_val_score(forest_reg, X_train, y_train, scoring="neg_mean_squared_error", cv=10)
    # forest_rmse_scores = np.sqrt(-forest_scores)
    # display_scores(forest_rmse_scores)



    # Random forest regressor is the best until now. The score on training and validation sets are very similar and hence there should be no overfitting. If the score on the training set is much lower than that of the validation set, the data may be overfit, but in this case, it seems that the data is not overfitting (and no underfitting).


    # Now that we know the Random Forest Regressor has the lowest RMSE, lets fine-tune the parameters to get an even lower RMSE.

    from sklearn.model_selection import GridSearchCV

    param_grid = [
        {'bootstrap': [False], 'n_estimators': [5,10,100], 'max_features': [3,5,7]},
    ]

    forest_reg = RandomForestRegressor(random_state=41)

    grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                            scoring='neg_mean_squared_error',
                            return_train_score=True)

    grid_search.fit(X_train, y_train)

    grid_search.best_params_


    grid_search.best_estimator_


    final_model = grid_search.best_estimator_
    final_predictions = final_model.predict(X_test)
    # final_mse = mean_squared_error(y_test, final_predictions)
    # final_rmse = np.sqrt(final_mse)


    # print("Final RMSE:",final_rmse)


    # After using the GridSearchCV to search for the best parameters and using those parameters, the final RMSE is the lowest amongst all methods tried.
    return ([X_test,final_predictions])

