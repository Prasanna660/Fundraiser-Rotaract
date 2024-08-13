import streamlit as st
from streamlit_option_menu import option_menu
import time

# Set up the page configuration
st.set_page_config(page_title="Rotaract Club Fundraiser", page_icon=":rotating_light:", layout="centered")

# Custom CSS to expand and style the navigation bar
st.markdown("""
    <style>
    /* Increase padding and spacing */
    .css-1b2oii4 {
        padding: 10px 20px; /* Top/bottom padding, Left/right padding */
    }
    .nav-bar .nav-item .nav-link {
        padding: 0 20px !important; /* Left/right padding */
        font-size: 18px !important; /* Font size */
    }
    .nav-bar {
        display: flex;
        justify-content: center; /* Center the navigation items */
        background-color: #f5f5f5; /* Background color */
        padding: 10px 0;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# Top Navigation Bar with increased spacing
selected = option_menu(
    None, 
    ["Home", "Donate via QR Code", "Donate via Bank Transfer", "Impact", "Contact Us", "Social Media"], 
    icons=["house", "qrcode", "bank", "graph-up", "envelope", "share-fill"], 
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal"
)

# Placeholder values for donations
total_donations_target = 5000  # Target value
todays_donations_target = 250  # Target value

# Function to animate the counting
def animate_count(label, target_value):
    placeholder = st.empty()
    current_value = 0
    increment = target_value // 100  # Adjust the speed of counting here
    while current_value < target_value:
        current_value += increment
        if current_value > target_value:
            current_value = target_value
        placeholder.metric(label=label, value=f"${current_value:,}")
        time.sleep(0.01)

# Home Page
if selected == "Home":
    st.markdown("<div class='title'>Rotaract Club Fundraiser</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>Making a Difference Together</div>", unsafe_allow_html=True)
    st.write("Join us in our mission to support various causes and bring positive change to the community.")
    
    # Display Total Donations and Today's Donations with animation
    st.write("### Donation Statistics")
    col1, col2 = st.columns(2)
    with col1:
        animate_count("Total Donations", total_donations_target)
    with col2:
        animate_count("Today's Donations", todays_donations_target)
    
    # Reason for This Funding
    st.write("### Reason for This Funding")
    st.write(
        """
        The funds raised through this campaign will be used to support underprivileged students by providing scholarships, 
        improving local community healthcare facilities, and organizing environmental sustainability initiatives. 
        Your contribution will help make a significant impact in the lives of many individuals in our community.
        """
    )
    
    st.write("### Make a Donation")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Donate via QR Code", key="qr_button"):
            st.session_state["current_page"] = "Donate via QR Code"
            st.experimental_rerun()
    with col2:
        if st.button("Donate via Bank Transfer", key="bank_button"):
            st.session_state["current_page"] = "Donate via Bank Transfer"
            st.experimental_rerun()

    st.write("## Your Impact")
    st.image("https://plus.unsplash.com/premium_photo-1661391634096-d4dd51963dc5?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGltcGFjdCUyMGltYWdlcyUyMGZ1bmQlMjByYWlzZXxlbnwwfHwwfHx8MA%3D%3D", width=700)
    st.write("Every donation helps us support education, healthcare, and community development.")
    
    st.write("## Fundraising Progress")
    st.progress(65)
    
    st.write("## Contact Us")
    st.write("If you have any questions or need more information, feel free to contact us at "
             "[email@example.com](mailto:email@example.com) or call us at +1234567890.")
    
    st.write("## Follow Us")
    social_selected = option_menu(None, ["Facebook", "Twitter", "Instagram"],
                                  icons=["facebook", "twitter", "instagram"],
                                  menu_icon="cast", default_index=0, orientation="horizontal")
    if social_selected == "Facebook":
        st.write("Follow us on [Facebook](https://facebook.com)")
    elif social_selected == "Twitter":
        st.write("Follow us on [Twitter](https://twitter.com)")
    elif social_selected == "Instagram":
        st.write("Follow us on [Instagram](https://instagram.com)")

# QR Code Donation Page
elif selected == "Donate via QR Code":
    st.markdown("<div class='title'>Donate via QR Code</div>", unsafe_allow_html=True)
    st.image("qrcode.jpeg", caption="Scan to Donate", width=300)  # Replace with your QR code image

# Bank Transfer Donation Page
elif selected == "Donate via Bank Transfer":
    st.markdown("<div class='title'>Donate via Bank Transfer</div>", unsafe_allow_html=True)
    st.write("**Bank Name:** Your Bank\n**Account Number:** 158100080200952\n**IFSC Code:** TMBL0000158")

# Impact Page
elif selected == "Impact":
    st.markdown("<div class='title'>Your Impact</div>", unsafe_allow_html=True)
    st.image("https://plus.unsplash.com/premium_photo-1661391634096-d4dd51963dc5?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGltcGFjdCUyMGltYWdlcyUyMGZ1bmQlMjByYWlzZXxlbnwwfHwwfHx8MA%3D%3D", width=700)
    st.write("Every donation helps us support education, healthcare, and community development.")

# Contact Page
elif selected == "Contact Us":
    st.markdown("<div class='title'>Contact Us</div>", unsafe_allow_html=True)
    st.write("If you have any questions or need more information, feel free to contact us at "
             "[email@example.com](mailto:email@example.com) or call us at +1234567890.")

# Social Media Page
elif selected == "Social Media":
    st.markdown("<div class='title'>Follow Us on Social Media</div>", unsafe_allow_html=True)
    social_selected = option_menu(None, ["Facebook", "Twitter", "Instagram"],
                                  icons=["facebook", "twitter", "instagram"],
                                  menu_icon="cast", default_index=0, orientation="horizontal")
    if social_selected == "Facebook":
        st.write("Follow us on [Facebook](https://facebook.com)")
    elif social_selected == "Twitter":
        st.write("Follow us on [Twitter](https://twitter.com)")
    elif social_selected == "Instagram":
        st.write("Follow us on [Instagram](https://instagram.com)")
