import streamlit as st
import pandas as pd
import os

# File path for the local CSV database
file_path = "properties.csv"

# Sample data for one full demo property if the file doesn't exist
sample_data = {
    "State": ["Florida"],
    "County": ["Miami-Dade"],
    "Auction Type": ["Tax Deed"],
    "Auction Date": ["2024-08-15"],
    "Online/Offline Auction": ["Online"],
    "Property Address": ["1234 Elm Street, Miami, FL"],
    "Parcel Number": ["123456789"],
    "Property Description": ["Residential lot, 0.5 acres"],
    "Zoning Information": ["Residential"],
    "Assessed Value": ["$50,000"],
    "Market Value": ["$120,000"],
    "Auction Platform/Location": ["GovDeals"],
    "Registration Requirements": ["Pre-registration required"],
    "Bidding Process": ["Incremental bidding"],
    "Starting Bid Amount": ["$10,000"],
    "Payment Terms": ["Due within 24 hours"],
    "Redemption Period": ["N/A"],
    "State and Local Laws": ["Florida Statutes"],
    "Tax Sale Regulations": ["Chapter 197"],
    "Redemption Rights": ["2 years"],
    "Notification Requirements": ["Certified mail"],
    "Legal Fees": ["$500"],
    "Required Documentation": ["Government-issued ID, Proof of funds"],
    "Initial Investment Amount": ["$10,000"],
    "Winning Bid Amount": ["$12,000"],
    "Additional Costs": ["$500 (registration fee)"],
    "Potential Returns": ["$15,000"],
    "Payment Due Dates": ["2024-08-16"],
    "Payment Methods": ["Wire transfer"],
    "Title Search Results": ["Clear title"],
    "Environmental Concerns": ["No environmental issues"],
    "Property Condition Reports": ["Good condition"],
    "Liens and Encumbrances": ["None"],
    "Occupancy Status": ["Vacant"],
    "Properties Bid On": ["1234 Elm Street, Miami, FL"],
    "Bid Amounts": ["$12,000"],
    "Winning/Losing Status": ["Winning"],
    "Follow-up Actions for Winning Bids": ["Submit payment, transfer deed"],
    "Payment Confirmation": ["Confirmed"],
    "Deed/Lien Transfer Process": ["In process"],
    "Follow-up on Redemption Period": ["Monitor redemption period"],
    "Property Management Plans": ["Rent or sell"],
    "Sale or Investment Strategy": ["Hold for 2 years, then sell"],
    "Auction Officials": ["Jane Doe (Auctioneer)"],
    "County Tax Office": ["Miami-Dade Tax Office"],
    "Legal Advisors": ["John Smith (Attorney)"],
    "Property Inspectors": ["ABC Inspections"],
    "Financial Institutions": ["XYZ Bank"],
    "Auction Day Notes": ["Smooth process, well-organized"],
    "Competitor Bidding Patterns": ["Aggressive bidding by competitors"],
    "Lessons Learned": ["Focus on residential areas"],
    "Market Trends and Insights": ["Market improving"],
    "Copies of Auction Certificates": ["Attached"],
    "Receipts and Payment Confirmations": ["Attached"],
    "Correspondence with Authorities": ["Filed"],
    "Legal Documents and Filings": ["Filed"]
}

# Load or initialize the CSV file
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame(sample_data)
    df.to_csv(file_path, index=False)

# Streamlit app
st.title("Tax Auction Property Manager")

# Displaying the DataFrame
st.dataframe(df)

# Function to save the DataFrame to CSV
def save_data(dataframe, path):
    dataframe.to_csv(path, index=False)

# Add a new property form
st.header("Add New Property")
with st.form("add_property"):
    form_data = {}
    for col in df.columns:
        form_data[col] = st.text_input(f"{col}")
    submitted = st.form_submit_button("Add Property")
    if submitted:
        new_row = pd.DataFrame([form_data])
        df = pd.concat([df, new_row], ignore_index=True)
        save_data(df, file_path)
        st.success("Property added successfully")

# Edit an existing property
st.header("Edit Existing Property")
property_to_edit = st.selectbox("Select Property to Edit", df["Property Address"].unique())
if property_to_edit:
    with st.form("edit_property"):
        row_index = df[df["Property Address"] == property_to_edit].index[0]
        form_data = {}
        for col in df.columns:
            form_data[col] = st.text_input(f"{col}", value=df.at[row_index, col])
        submitted = st.form_submit_button("Update Property")
        if submitted:
            for col in df.columns:
                df.at[row_index, col] = form_data[col]
            save_data(df, file_path)
            st.success("Property updated successfully")
