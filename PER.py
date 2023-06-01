# Example code using Surprise library for matrix factorization
from surprise import accuracy
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

# Load the data from your dataset
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)

# Split the data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.2)

# Train the model using SVD algorithm
model = SVD()
model.fit(trainset)
# Make predictions on the testing set
predictions = model.test(testset)

# Calculate accuracy metrics
accuracy.rmse(predictions)
accuracy.mae(predictions)
