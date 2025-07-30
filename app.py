import streamlit as st
import pandas as pd
import joblib

# Set page config
st.set_page_config(page_title="Restaurant App", layout="wide")

# Main navigation
st.title("🍽️ Restaurant Analysis App")
st.markdown("### Choose what you want to do:")

# Create navigation tabs
tab1, tab2 = st.tabs(["🔍 Restaurant Recommendations", "⭐ Rating Prediction"])

with tab1:
    st.header("Restaurant Recommendation System")
    st.markdown("### Choose your preference to find the best restaurants!")

    # Sample pre-computed data for each option
    cheap_restaurants = [
        {"name": "Brahmin's Coffee Bar", "average_cost": 100, "locality": "Basavanagudi", "rest_type": "Quick Bites", "cuisines": "South Indian", "rate": 4.8},
        {"name": "Taaza Thindi", "average_cost": 100, "locality": "Banashankari", "rest_type": "Quick Bites", "cuisines": "South Indian", "rate": 4.7},
        {"name": "CTR", "average_cost": 150, "locality": "Malleshwaram", "rest_type": "Quick Bites", "cuisines": "South Indian", "rate": 4.7},
        {"name": "Chikkanna Tiffin Room", "average_cost": 150, "locality": "Brigade Road", "rest_type": "Quick Bites", "cuisines": "South Indian", "rate": 4.5},
        {"name": "Veena Stores", "average_cost": 150, "locality": "Malleshwaram", "rest_type": "Quick Bites", "cuisines": "South Indian", "rate": 4.5},
        {"name": "Opus Food Stories", "average_cost": 1500, "locality": "Bellandur", "rest_type": "Bar, Casual Dining", "cuisines": "Goan, Asian, North Indian, European, Continental", "rate": 4.7},
        {"name": "Chianti", "average_cost": 1500, "locality": "Brigade Road", "rest_type": "Casual Dining", "cuisines": "Italian", "rate": 4.5},
        {"name": "Sarjapur Social", "average_cost": 1500, "locality": "Bellandur", "rest_type": "Bar, Casual Dining", "cuisines": "American, North Indian, Chinese, Finger Food", "rate": 4.6},
        {"name": "Toast & Tonic", "average_cost": 1500, "locality": "Brigade Road", "rest_type": "Casual Dining", "cuisines": "European, Asian", "rate": 4.6},
        {"name": "Communiti", "average_cost": 1500, "locality": "Brigade Road", "rest_type": "Microbrewery, Casual Dining", "cuisines": "Continental, BBQ, Salad", "rate": 4.7}
    ]

    expensive_restaurants = [
        {"name": "Rim Naam - The Oberoi", "average_cost": 3000, "locality": "Brigade Road", "rest_type": "Fine Dining", "cuisines": "Thai", "rate": 4.6, "votes": 979},
        {"name": "Karavalli - The Gateway Hotel", "average_cost": 3500, "locality": "Brigade Road", "rest_type": "Fine Dining", "cuisines": "Mangalorean, Konkan, Seafood, Kerala", "rate": 4.5, "votes": 674},
        {"name": "Alba - JW Marriott Bengaluru", "average_cost": 4000, "locality": "Brigade Road", "rest_type": "Fine Dining", "cuisines": "Italian", "rate": 4.5, "votes": 583}
    ]

    # Create two columns for buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Pocket-Friendly Plates"):
            st.subheader("Recommended Cheap Restaurants")
            for restaurant in cheap_restaurants:
                st.write(f"**Name:** {restaurant['name']}")
                st.write(f"**Average Cost:** ₹{restaurant['average_cost']}")
                st.write(f"**Locality:** {restaurant['locality']}")
                st.write(f"**Restaurant Type:** {restaurant['rest_type']}")
                st.write(f"**Cuisines:** {restaurant['cuisines']}")
                st.write(f"**Rating:** ⭐ {restaurant['rate']}")
                st.write("---")

    with col2:
        if st.button("Top-Tier Tastes"):
            st.subheader("Recommended Expensive Restaurants")
            for restaurant in expensive_restaurants:
                st.write(f"**Name:** {restaurant['name']}")
                st.write(f"**Average Cost:** ₹{restaurant['average_cost']}")
                st.write(f"**Locality:** {restaurant['locality']}")
                st.write(f"**Restaurant Type:** {restaurant['rest_type']}")
                st.write(f"**Cuisines:** {restaurant['cuisines']}")
                st.write(f"**Rating:** ⭐ {restaurant['rate']}")
                st.write(f"**Votes:** {restaurant['votes']}")
                st.write("---")

with tab2:
    st.header("Restaurant Rating Prediction")
    st.markdown("### Predict restaurant rating based on features")

    try:
        # Load the trained model and mappings
        ETree = joblib.load('extra_trees_model.pkl')
        mappings = joblib.load('mappings.pkl')

        st.write("Provide details below to predict the restaurant's rating:")

        # Collect user inputs
        user_input = {}

        # Create columns for better layout
        col1, col2 = st.columns(2)

        with col1:
            # Dropdowns for categorical variables that need encoding
            for column in ["online_order", "book_table", "location"]:
                if column in mappings:
                    options = mappings[column].set_index("Encoded")["Original"].to_dict()
                    selected_value = st.selectbox(f"{column.replace('_', ' ').title()}:", options.keys(), format_func=lambda x: options[x])
                    user_input[column] = selected_value

        with col2:
            for column in ["rest_type", "cuisines"]:
                if column in mappings:
                    options = mappings[column].set_index("Encoded")["Original"].to_dict()
                    selected_value = st.selectbox(f"{column.replace('_', ' ').title()}:", options.keys(), format_func=lambda x: options[x])
                    user_input[column] = selected_value

        # Add menu_item with default value since it was removed from mappings but model expects it
        user_input["menu_item"] = 0  # Default encoded value

        # Numeric inputs
        col3, col4 = st.columns(2)
        with col3:
            user_input["votes"] = st.number_input("Votes:", min_value=0, step=1, help="Number of votes received by the restaurant")
        with col4:
            user_input["cost"] = st.number_input("Cost (in ₹):", min_value=0.0, step=0.01, help="Approximate cost for two people")

        # Prediction button
        if st.button("Predict Rating", type="primary"):
            try:
                # Create DataFrame with correct feature order as expected by the model
                # Model expects: ['online_order', 'book_table', 'votes', 'location', 'rest_type', 'cuisines', 'cost', 'menu_item']
                ordered_data = {
                    'online_order': user_input['online_order'],
                    'book_table': user_input['book_table'],
                    'votes': user_input['votes'],
                    'location': user_input['location'],
                    'rest_type': user_input['rest_type'],
                    'cuisines': user_input['cuisines'],
                    'cost': user_input['cost'],
                    'menu_item': user_input['menu_item']
                }

                input_data = pd.DataFrame([ordered_data])

                # Make prediction
                prediction = ETree.predict(input_data)

                # Display result
                st.success("Prediction Complete!")
                st.subheader("Predicted Rating:")
                st.write(f"⭐ **{round(prediction[0], 2)}/5.0**")
                st.balloons()

            except Exception as e:
                st.error(f"Error making prediction: {str(e)}")
                st.write("Please check that all fields are filled correctly.")

    except FileNotFoundError:
        st.error("Model files not found! Please make sure 'extra_trees_model.pkl' and 'mappings.pkl' are in the same directory.")
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")

# Add footer
st.markdown("---")
st.markdown("*Built with Streamlit and Machine Learning*")
