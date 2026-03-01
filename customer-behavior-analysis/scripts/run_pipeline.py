import pandas as pd
from src.customer_behavior.data_processing import load_data, clean_data, preprocess_data
from src.customer_behavior.features import create_features, select_features
from src.customer_behavior.models import CustomerBehaviorModel
from src.customer_behavior.visualize import plot_customer_segments, plot_feature_importance

def run_pipeline():
    # Load the data
    raw_data = load_data('data/raw/customer_behavior_data.csv')
    
    # Clean the data
    cleaned_data = clean_data(raw_data)
    
    # Preprocess the data
    processed_data = preprocess_data(cleaned_data)
    
    # Create features
    features = create_features(processed_data)
    
    # Select features
    selected_features = select_features(features)
    
    # Initialize and fit the model
    model = CustomerBehaviorModel()
    model.fit(selected_features)
    
    # Make predictions
    predictions = model.predict(selected_features)
    
    # Evaluate the model
    evaluation_results = model.evaluate(predictions)
    
    # Visualize customer segments
    plot_customer_segments(processed_data)
    
    # Visualize feature importance
    plot_feature_importance(model)

if __name__ == "__main__":
    run_pipeline()