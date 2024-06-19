import streamlit as st
from PIL import Image
from helpers import * 



# Import this file in app.py
def meal_plan_page():
  st.title("Meal Plan Generator")

  # uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

  # if uploaded_file is not None:
  #     # Display the uploaded image
  #     image = Image.open(uploaded_file)
  #     st.image(image, caption='Uploaded Image', use_column_width=True)
      
  #     image.save('temp_upload/img.png')

  #     # Identify ingredients
  #     with st.spinner('Identifying ingredients...'):
  #         ingredients = identify_ingredients('temp_upload/img.png')

  #     st.subheader("Identified Ingredients")
  #     st.write(ingredients)

    # Generate meal plan
  ingredients = st.text_input("Enter ingredients (comma separated)")
  preferences = st.text_input("Preferences", placeholder="I need a full day meal plan for a body builder who's prioritizing proteins")

  # Add a button to submit the request (can be linked to actual meal plan generation logic)
  if st.button("Generate Meal Plan"):
    with st.spinner("Generating Meal Plan..."):  # Show spinner while processing
      meal_plan = generate_recipe(ingredients, preferences)  # Replace with your function call

      st.subheader("Meal Options")

    # Display meal plan after generation
    if meal_plan:
      for i, meal in enumerate(meal_plan['meals']):
         with st.expander(meal['meal']):
            output_text = ' \n'.join(str(v) for v in meal['ingredients']) + '\n\n' + '\n'.join( str(v) for v in meal['recipe'])
            st.write(
               output_text
            )
        

    else:
      st.error("An error occurred while generating the meal plan.")


  st.write("Don't forget to leave a feedback ❤️")


if __name__ == '__main__':
  meal_plan_page()