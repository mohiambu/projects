import pandas as pd
import numpy as np

### Data Loading and Exploration:
# in this code we load data as we read in as csv file 

path = "C://Users//M7MDA//Downloads//u.data"
Tit = ['userId', 'movieId', 'rating', 'timestamp']
data = pd.read_csv(path, sep='\t', names=Tit, header=None)

### Data Preprocessing
# in this code we convert the data into a matrix and covert Nan values into 0's 
# also we drop timestamp column because we don't need it 

data = data.drop(columns='timestamp')
matrix = data.pivot(index='userId', columns='movieId', values='rating').fillna(0) 
# print(matrix)


#Data Split
# this code keeps 20% of the users, take its data and hide 20% of it's ratings and keep the rest for training

TestUser = data['userId'].drop_duplicates().sample(frac=0.2, random_state=31)  ## 20% of users 
Test_User_data = data[data['userId'].isin(TestUser)]
test_data = Test_User_data.sample(frac=0.2, random_state=31)
train_data = data.drop(test_data.index)

# print(len(train_data))
# print(len(test_data))



### User-Based Collaborative filtering
# this code calculate user similarities using cosine similarity, 
#then predicts movie ratings for test users based on their most similar users ratings.

matrix = train_data.pivot(index='userId', columns='movieId', values='rating').fillna(0)
def cosine_similarity(matrix):
    users_n = matrix.shape[0]
    sim = np.zeros((users_n, users_n))
    for i in range(users_n):
        for j in range(users_n):
            if i == j:
                sim[i, j] = 1
            else:
                user_1 = matrix[i]
                user_2 = matrix[j]
                prod = np.dot(user_1, user_2)
                ni = np.linalg.norm(user_1)
                nj = np.linalg.norm(user_2)
                if ni == 0 or nj == 0:
                    sim[i, j] = 0 
                else:
                    sim[i, j] = prod/ (ni * nj)
    return sim

tmatrix = matrix.to_numpy()
cos_matrix = cosine_similarity(tmatrix)
df = pd.DataFrame(cos_matrix, index=matrix.index, columns=matrix.index)



def predict(test_data,k=5):
    predicts = []
    for z,row in test_data.iterrows():
        user_id, movie_id = row['userId'], row['movieId']
        
        if user_id in df.index and movie_id in matrix.columns:
            su = df[user_id].sort_values(ascending=False).iloc[1:k+1]
            w_sum, s_sum = 0, 0
            for sim_user,similarity in su.items():
                rating = matrix.at[sim_user, movie_id]
                if rating > 0:
                    w_sum += similarity * rating
                    s_sum += similarity
            if s_sum > 0:
                predicts.append(w_sum / s_sum)
            else:
                predicts.append(np.nan)
        else:
            predicts.append(np.nan)
    return predicts


test_data['predicted_rating'] = predict(test_data)

print(test_data[['userId', 'movieId', 'rating', 'predicted_rating']].head())

#V. Evaluation:
#This code compares the actual ratings and predicted ratings 
#to measure how close the predictions are which mentions the average
# error (MSE) and its square root (RMSE)

def rmse(initial, predicted):
    c = 0
    for i,j in zip(initial,predicted):
        c += (i-j)**2
        mse = c/len(initial)

    return f"mean squared error :{mse}" ,f"root mean squared error :{mse** 0.5}"




dataneeded = test_data.dropna(subset=['predicted_rating'])
initialratings = dataneeded['rating'].tolist()
predictedratings = dataneeded['predicted_rating'].tolist()

rmse = rmse(initialratings, predictedratings)

print(rmse)



# Results and Analysis:
# performance:
# we got root mean squared error: 1.13 which means predictions are usually about 1.13 points different from the actual ratings
# which means the model accuracy is performing very good (almost accurate))

#strengths:
#easy to understand and implement 
# works good with small data sets.


#limitations 
# can be slow when datasets are large 
# we need a lot of ratings to find similar users.