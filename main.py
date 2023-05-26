import streamlit as st
import requests
import io
from PIL import Image

# Define the API endpoint URL
API_ENDPOINT = 'http://157.230.238.180/predict'

# Define Streamlit app
def main():
    st.title("Receipt OCR API Demo")

    # Create a file uploader widget
    uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpeg', 'jpg'])

    # Display the uploaded image
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        # st.image(image, caption='Uploaded Image', use_column_width=True)

    # Create a button to send the image to the API
    if st.button('Send Image'):
        if uploaded_file is None:
            st.warning('Please upload an image file first.')
        else:
            # Prepare the image data for the API request
            img_data = io.BytesIO()
            image.save(img_data, format='PNG')
            img_data.seek(0)

            # Send the image to the API using the curl command
            files = {'file': ('invoice.png', img_data, 'image/png')}
            headers = {'accept': 'application/json'}
            response = requests.post(API_ENDPOINT, files=files, headers=headers)

            # Display the API response
            st.subheader('API Response')
            st.json(response.json())

# Run the Streamlit app
if __name__ == '__main__':
    main()
