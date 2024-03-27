import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

crop_data = pd.read_csv('Crop_recommendation.csv')

crop_data.drop([8,9],axis=0)
unnamed_columns_index = [8, 9]
crop_data = crop_data.iloc[:, ~crop_data.columns.isin(crop_data.columns[unnamed_columns_index])]
#crop_data = pd.get_dummies(crop_data)
def compare_similarities(cropDf,cropData):
    try:
        # Calculate cosine similarity
        similarity_matrix = cosine_similarity(cropData,cropDf)
        # Get the similarity level for each row
        similarity_levels = pd.Series(similarity_matrix.flatten(), index=crop_data['label'])
        
        # Sort the results by similarity level
        sorted_results = similarity_levels.sort_values(ascending=False)
        top_3 = sorted_results[:3]
        # Convert to percentage
        similarity_percentage = (top_3 * 100).round(2).astype(str) + '%'
        print(f"Similarity Percentage:", similarity_percentage)
        return similarity_percentage

    except Exception as e:
        print("Error in compare_symptoms_percentage:", e)
        return str(e)




def preparation(input_data):

        df = pd.DataFrame({
            'Nitrogen': [input_data['Nitrogen']],
            'phosphorus': [input_data['phosphorus']],
            'potassium': [input_data['potassium']],
            'temperature': [input_data['temperature']],
            'humidity': [input_data['humidity']],
            'ph': [input_data['ph']],
            'rainfall':[input_data['rainfall']]
        })
        features=crop_data.drop(labels=['label'],axis=1)
        recommended_crops =compare_similarities(df, features)
        index_values = recommended_crops.index.tolist()  # Convert index to a list
        series_values = recommended_crops.values.tolist()  # Convert values to a list

        print("Index values:", index_values)
        print("Series values:", series_values)
        return index_values




