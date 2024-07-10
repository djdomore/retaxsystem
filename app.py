import streamlit as st
import pandas as pd
import os

# File path for the local CSV database
file_path = "properties.csv"

# Sample data for multiple demo properties if the file doesn't exist
sample_data = [
    {
        "State": "Florida",
        "County": "Miami-Dade",
        "Auction Type": "Tax Deed",
        "Auction Date": "2024-08-15",
        "Online/Offline Auction": "Online",
        "Property Address": "1234 Elm Street, Miami, FL",
        "Parcel Number": "123456789",
        "Property Description": "Residential lot, 0.5 acres",
        "Zoning Information": "Residential",
        "Assessed Value": "$50,000",
        "Market Value": "$120,000",
        "Auction Platform/Location": "GovDeals",
        "Registration Requirements": "Pre-registration required",
        "Bidding Process": "Incremental bidding",
        "Starting Bid Amount": "$10,000",
        "Payment Terms": "Due within 24 hours",
        "Redemption Period": "N/A",
        "State and Local Laws": "Florida Statutes",
        "Tax Sale Regulations": "Chapter 197",
        "Redemption Rights": "2 years",
        "Notification Requirements": "Certified mail",
        "Legal Fees": "$500",
        "Required Documentation": "Government-issued ID, Proof of funds",
        "Initial Investment Amount": "$10,000",
        "Winning Bid Amount": "$12,000",
        "Additional Costs": "$500 (registration fee)",
        "Potential Returns": "$15,000",
        "Payment Due Dates": "2024-08-16",
        "Payment Methods": "Wire transfer",
        "Title Search Results": "Clear title",
        "Environmental Concerns": "No environmental issues",
        "Property Condition Reports": "Good condition",
        "Liens and Encumbrances": "None",
        "Occupancy Status": "Vacant",
        "Properties Bid On": "1234 Elm Street, Miami, FL",
        "Bid Amounts": "$12,000",
        "Winning/Losing Status": "Winning",
        "Follow-up Actions for Winning Bids": "Submit payment, transfer deed",
        "Payment Confirmation": "Confirmed",
        "Deed/Lien Transfer Process": "In process",
        "Follow-up on Redemption Period": "Monitor redemption period",
        "Property Management Plans": "Rent or sell",
        "Sale or Investment Strategy": "Hold for 2 years, then sell",
        "Auction Officials": "Jane Doe (Auctioneer)",
        "County Tax Office": "Miami-Dade Tax Office",
        "Legal Advisors": "John Smith (Attorney)",
        "Property Inspectors": "ABC Inspections",
        "Financial Institutions": "XYZ Bank",
        "Auction Day Notes": "Smooth process, well-organized",
        "Competitor Bidding Patterns": "Aggressive bidding by competitors",
        "Lessons Learned": "Focus on residential areas",
        "Market Trends and Insights": "Market improving",
        "Copies of Auction Certificates": "Attached",
        "Receipts and Payment Confirmations": "Attached",
        "Correspondence with Authorities": "Filed",
        "Legal Documents and Filings": "Filed"
    },
    {
        "State": "California",
        "County": "Los Angeles",
        "Auction Type": "Foreclosure Sale",
        "Auction Date": "2024-09-10",
        "Online/Offline Auction": "Offline",
        "Property Address": "5678 Oak Avenue, Los Angeles, CA",
        "Parcel Number": "987654321",
        "Property Description": "Commercial building, 10,000 sq ft",
        "Zoning Information": "Commercial",
        "Assessed Value": "$500,000",
        "Market Value": "$800,000",
        "Auction Platform/Location": "Courthouse Steps",
        "Registration Requirements": "On-site registration",
        "Bidding Process": "Competitive bidding",
        "Starting Bid Amount": "$300,000",
        "Payment Terms": "Due at auction close",
        "Redemption Period": "90 days",
        "State and Local Laws": "California Civil Code",
        "Tax Sale Regulations": "Chapter 341",
        "Redemption Rights": "1 year",
        "Notification Requirements": "Public notice",
        "Legal Fees": "$1,000",
        "Required Documentation": "Photo ID, Proof of financing",
        "Initial Investment Amount": "$300,000",
        "Winning Bid Amount": "$750,000",
        "Additional Costs": "$1,200 (documentation fee)",
        "Potential Returns": "$200,000",
        "Payment Due Dates": "2024-09-11",
        "Payment Methods": "Cashier's check",
        "Title Search Results": "Title issues found",
        "Environmental Concerns": "Minor contamination",
        "Property Condition Reports": "Needs renovation",
        "Liens and Encumbrances": "Utility liens",
        "Occupancy Status": "Occupied",
        "Properties Bid On": "5678 Oak Avenue, Los Angeles, CA",
        "Bid Amounts": "$750,000",
        "Winning/Losing Status": "Winning",
        "Follow-up Actions for Winning Bids": "Complete payment, transfer title",
        "Payment Confirmation": "Pending",
        "Deed/Lien Transfer Process": "Initiated",
        "Follow-up on Redemption Period": "Notify tenants of change",
        "Property Management Plans": "Renovate and lease",
        "Sale or Investment Strategy": "Long-term hold for rental income",
        "Auction Officials": "John Smith (Auctioneer)",
        "County Tax Office": "Los Angeles Tax Office",
        "Legal Advisors": "Emily Brown (Attorney)",
        "Property Inspectors": "DEF Inspections",
        "Financial Institutions": "ABC Bank",
        "Auction Day Notes": "Competitive bidding atmosphere",
        "Competitor Bidding Patterns": "Strategic bidding on high-value properties",
        "Lessons Learned": "Assess renovation costs upfront",
        "Market Trends and Insights": "Stable commercial market",
        "Copies of Auction Certificates": "Attached",
        "Receipts and Payment Confirmations": "Pending",
        "Correspondence with Authorities": "In process",
        "Legal Documents and Filings": "In progress"
    },
    {
        "State": "New York",
        "County": "New York",
        "Auction Type": "Tax Lien",
        "Auction Date": "2024-08-25",
        "Online/Offline Auction": "Online",
        "Property Address": "910 Broadway, New York, NY",
        "Parcel Number": "246810123",
        "Property Description": "Commercial office space",
        "Zoning Information": "Commercial",
        "Assessed Value": "$1,000,000",
        "Market Value": "$1,500,000",
        "Auction Platform/Location": "Online Auction Platform",
        "Registration Requirements": "Online registration",
        "Bidding Process": "Sealed bid",
        "Starting Bid Amount": "$700,000",
        "Payment Terms": "Within 48 hours of bid acceptance",
        "Redemption Period": "120 days",
        "State and Local Laws": "New York State Tax Law",
        "Tax Sale Regulations": "Chapter 47",
        "Redemption Rights": "1 year",
        "Notification Requirements": "Email notification",
        "Legal Fees": "$1,500",
        "Required Documentation": "ID verification, Proof of financial capability",
        "Initial Investment Amount": "$700,000",
        "Winning Bid Amount": "$1,200,000",
        "Additional Costs": "$2,000 (processing fee)",
        "Potential Returns": "$500,000",
        "Payment Due Dates": "2024-08-26",
        "Payment Methods": "Bank transfer",
        "Title Search Results": "Clear title",
        "Environmental Concerns": "No environmental issues",
        "Property Condition Reports": "Excellent condition",
        "Liens and Encumbrances": "None",
        "Occupancy Status": "Vacant",
        "Properties Bid On": "910 Broadway, New York, NY",
        "Bid Amounts": "$1,200,000",
        "Winning/Losing Status": "Winning",
        "Follow-up Actions for Winning Bids": "Complete payment, transfer title",
        "Payment Confirmation": "Pending",
        "Deed/Lien Transfer Process": "To be initiated",
        "Follow-up on Redemption Period": "Notify current tenants",
        "Property Management Plans": "Lease to corporate tenants",
        "Sale or Investment Strategy": "Immediate lease, potential resale",
        "Auction Officials": "Mary Johnson (Auctioneer)",
        "County Tax Office": "New York City Tax Office",
        "Legal Advisors": "Michael Wilson (Attorney)",
        "Property Inspectors": "EFG Inspections",
        "Financial Institutions": "PQR Bank",
        "Auction Day Notes": "High competition among bidders",
        "Competitor Bidding Patterns": "Strategic bidding on prime properties",
        "Lessons Learned": "Research local market demand",
        "Market Trends and Insights": "Strong demand for commercial spaces",
        "Copies of Auction Certificates": "Attached",
        "Receipts and Payment Confirmations": "Attached",
        "Correspondence with Authorities": "Filed",
        "Legal Documents and Filings": "Filed"
    },
    {
        "State": "Texas",
        "County": "Harris",
        "Auction Type": "Sheriff Sale",
        "Auction Date": "2024-09-01",
        "Online/Offline Auction": "Offline",
        "Property Address": "7890 Maple Avenue, Houston, TX",
        "Parcel Number": "135792468",
        "Property Description": "Single-family home, 3 bedrooms",
        "Zoning Information": "Residential",
        "Assessed Value": "$150,000",
        "Market Value": "$200,000",
        "Auction Platform/Location": "County Courthouse",
        "Registration Requirements": "In-person registration",
        "Bidding Process": "Public auction",
        "Starting Bid Amount": "$100,000",
        "Payment Terms": "Immediately after auction",
        "Redemption Period": "None",
        "State and Local Laws": "Texas Property Code",
        "Tax Sale Regulations": "Chapter 33",
        "Redemption Rights": "None",
        "Notification Requirements": "Public notice",
        "Legal Fees": "$800",
        "Required Documentation": "Driver's license, Cashier's check",
        "Initial Investment Amount": "$100,000",
        "Winning Bid Amount": "$180,000",
        "Additional Costs": "$300 (auction fee)",
        "Potential Returns": "$20,000",
        "Payment Due Dates": "2024-09-02",
        "Payment Methods": "Cashier's check",
        "Title Search Results": "Title issues found",
        "Environmental Concerns": "Mild structural issues",
        "Property Condition Reports": "Needs renovation",
        "Liens and Encumbrances": "Utility liens",
        "Occupancy Status": "Vacant",
        "Properties Bid On": "7890 Maple Avenue, Houston, TX",
        "Bid Amounts": "$180,000",
        "Winning/Losing Status": "Winning",
        "Follow-up Actions for Winning Bids": "Complete payment, transfer title",
        "Payment Confirmation": "Pending",
        "Deed/Lien Transfer Process": "To be initiated",
        "Follow-up on Redemption Period": "Notify previous owner",
        "Property Management Plans": "Renovate and sell",
        "Sale or Investment Strategy": "Fix and flip",
        "Auction Officials": "Mark Thompson (Sheriff)",
        "County Tax Office": "Harris County Tax Office",
        "Legal Advisors": "Sarah Davis (Attorney)",
        "Property Inspectors": "GHI Inspections",
        "Financial Institutions": "LMN Bank",
        "Auction Day Notes": "Successful bidding process",
        "Competitor Bidding Patterns": "Competitive bidding on desirable properties",
        "Lessons Learned": "Assess renovation costs accurately",
        "Market Trends and Insights": "Strong demand for investment properties",
        "Copies of Auction Certificates": "Attached",
        "Receipts and Payment Confirmations": "Pending",
        "Correspondence with Authorities": "In process",
        "Legal Documents and Filings": "In progress"
    },
    {
        "State": "Illinois",
        "County": "Cook",
        "Auction Type": "Tax Deed",
        "Auction Date": "2024-08-20",
        "Online/Offline Auction": "Offline",
        "Property Address": "2468 Pine Street, Chicago, IL",
        "Parcel Number": "314159265",
        "Property Description": "Vacant land, 1 acre",
        "Zoning Information": "Residential",
        "Assessed Value": "$30,000",
        "Market Value": "$50,000",
        "Auction Platform/Location": "County Treasurer's Office",
        "Registration Requirements": "In-person registration",
        "Bidding Process": "Competitive bidding",
        "Starting Bid Amount": "$20,000",
        "Payment Terms": "Within 48 hours of auction",
        "Redemption Period": "180 days",
        "State and Local Laws": "Illinois Property Tax Code",
        "Tax Sale Regulations": "Chapter 35",
        "Redemption Rights": "3 years",
        "Notification Requirements": "Public notice",
        "Legal Fees": "$300",
        "Required Documentation": "Valid ID, Proof of funds",
        "Initial Investment Amount": "$20,000",
        "Winning Bid Amount": "$25,000",
        "Additional Costs": "$100 (administration fee)",
        "Potential Returns": "$25,000",
        "Payment Due Dates": "2024-08-21",
        "Payment Methods": "Cash or certified funds",
        "Title Search Results": "Title issues found",
        "Environmental Concerns": "No environmental issues",
        "Property Condition Reports": "Land requires clearing",
        "Liens and Encumbrances": "None",
        "Occupancy Status": "Vacant",
        "Properties Bid On": "2468 Pine Street, Chicago, IL",
        "Bid Amounts": "$25,000",
        "Winning/Losing Status": "Winning",
        "Follow-up Actions for Winning Bids": "Complete payment, transfer deed",
        "Payment Confirmation": "Pending",
        "Deed/Lien Transfer Process": "To be initiated",
        "Follow-up on Redemption Period": "Notify previous owner",
        "Property Management Plans": "Hold for future development",
        "Sale or Investment Strategy": "Long-term investment",
        "Auction Officials": "Michael Brown (Auctioneer)",
        "County Tax Office": "Cook County Treasurer's Office",
        "Legal Advisors": "Lisa Green (Attorney)",
        "Property Inspectors": "JKL Inspections",
        "Financial Institutions": "NOP Bank",
        "Auction Day Notes": "Smooth auction process",
        "Competitor Bidding Patterns": "Strategic bidding on land parcels",
        "Lessons Learned": "Research local development plans",
        "Market Trends and Insights": "Growing interest in land investments",
        "Copies of Auction Certificates": "Attached",
        "Receipts and Payment Confirmations": "Pending",
        "Correspondence with Authorities": "In process",
        "Legal Documents and Filings": "In progress"
    },
    {
        "State": "Arizona",
        "County": "Maricopa",
        "Auction Type": "Tax Lien",
        "Auction Date": "2024-09-05",
        "Online/Offline Auction": "Online",
        "Property Address": "1357 Desert Road, Phoenix, AZ",
        "Parcel Number": "246801357",
        "Property Description": "Vacant residential lot",
        "Zoning Information": "Residential",
        "Assessed Value": "$40,000",
        "Market Value": "$60,000",
        "Auction Platform/Location": "Online Auction Platform",
        "Registration Requirements": "Online registration",
        "Bidding Process": "Sealed bid",
        "Starting Bid Amount": "$25,000",
        "Payment Terms": "Within 72 hours of bid acceptance",
        "Redemption Period": "180 days",
        "State and Local Laws": "Arizona Revised Statutes",
        "Tax Sale Regulations": "Chapter 27",
        "Redemption Rights": "3 years",
        "Notification Requirements": "Email notification",
        "Legal Fees": "$200",
        "Required Documentation": "Identification, Proof of funds",
        "Initial Investment Amount": "$25,000",
        "Winning Bid Amount": "$40,000",
        "Additional Costs": "$50 (processing fee)",
        "Potential Returns": "$20,000",
        "Payment Due Dates": "2024-09-06",
        "Payment Methods": "Bank transfer",
        "Title Search Results": "Clear title",
        "Environmental Concerns": "No environmental issues",
        "Property Condition Reports": "Vacant lot with no structures",
        "Liens and Encumbrances": "None",
        "Occupancy Status": "Vacant",
        "Properties Bid On": "1357 Desert Road, Phoenix, AZ",
        "Bid Amounts": "$40,000",
        "Winning/Losing Status": "Winning",
        "Follow-up Actions for Winning Bids": "Complete payment, transfer title",
        "Payment Confirmation": "Pending",
        "Deed/Lien Transfer Process": "To be initiated",
        "Follow-up on Redemption Period": "Notify previous owner",
        "Property Management Plans": "Hold for future development",
        "Sale or Investment Strategy": "Potential resale to developer",
        "Auction Officials": "David White (Auctioneer)",
        "County Tax Office": "Maricopa County Treasurer's Office",
        "Legal Advisors": "Jennifer Lee (Attorney)",
        "Property Inspectors": "MNO Inspections",
        "Financial Institutions": "QRS Bank",
        "Auction Day Notes": "High interest in vacant lots",
        "Competitor Bidding Patterns": "Strategic bidding on prime locations",
        "Lessons Learned": "Evaluate local zoning regulations",
        "Market Trends and Insights": "Growing demand for residential lots",
        "Copies of Auction Certificates": "Attached",
        "Receipts and Payment Confirmations": "Pending",
        "Correspondence with Authorities": "In process",
        "Legal Documents and Filings": "In progress"
    },
    {
        "State": "Nevada",
        "County": "Clark",
        "Auction Type": "Tax Deed",
        "Auction Date": "2024-09-15",
        "Online/Offline Auction": "Offline",
        "Property Address": "1010 Casino Road, Las Vegas, NV",
        "Parcel Number": "9876543210",
        "Property Description": "Commercial property, 20,000 sq ft",
        "Zoning Information": "Commercial",
        "Assessed Value": "$2,000,000",
        "Market Value": "$3,000,000",
        "Auction Platform/Location": "County Tax Office",
        "Registration Requirements": "In-person registration",
        "Bidding Process": "Competitive bidding",
        "Starting Bid Amount": "$1,500,000",
        "Payment Terms": "Within 24 hours of auction close",
        "Redemption Period": "None",
        "State and Local Laws": "Nevada Revised Statutes",
        "Tax Sale Regulations": "Chapter 361",
        "Redemption Rights": "None",
        "Notification Requirements": "Public notice",
        "Legal Fees": "$3,000",
        "Required Documentation": "Government ID, Proof of financing",
        "Initial Investment Amount": "$1,500,000",
        "Winning Bid Amount": "$2,500,000",
        "Additional Costs": "$2,500 (auction fee)",
        "Potential Returns": "$500,000",
        "Payment Due Dates": "2024-09-16",
        "Payment Methods": "Wire transfer",
        "Title Search Results": "Title issues found",
        "Environmental Concerns": "Asbestos abatement needed",
        "Property Condition Reports": "Requires renovation",
        "Liens and Encumbrances": "Utility liens",
        "Occupancy Status": "Vacant",
        "Properties Bid On": "1010 Casino Road, Las Vegas, NV",
        "Bid Amounts": "$2,500,000",
        "Winning/Losing Status": "Winning",
        "Follow-up Actions for Winning Bids": "Complete payment, transfer title",
        "Payment Confirmation": "Pending",
        "Deed/Lien Transfer Process": "To be initiated",
        "Follow-up on Redemption Period": "None",
        "Property Management Plans": "Renovate and lease",
        "Sale or Investment Strategy": "Renovate for higher lease value",
        "Auction Officials": "Sarah Johnson (Auctioneer)",
        "County Tax Office": "Clark County Treasurer's Office",
        "Legal Advisors": "Robert Green (Attorney)",
        "Property Inspectors": "PQR Inspections",
        "Financial Institutions": "STU Bank",
        "Auction Day Notes": "Competitive bidding atmosphere",
        "Competitor Bidding Patterns": "Aggressive bidding on prime commercial sites",
        "Lessons Learned": "Assess renovation costs accurately",
        "Market Trends and Insights": "Strong commercial property demand",
        "Copies of Auction Certificates": "Attached",
        "Receipts and Payment Confirmations": "Pending",
        "Correspondence with Authorities": "In process",
        "Legal Documents and Filings": "In progress"
    }
]

# Function to initialize or load existing CSV data
def load_data(file_path):
    if not os.path.exists(file_path):
        df = pd.DataFrame(sample_data)
        df.to_csv(file_path, index=False)
    else:
        df = pd.read_csv(file_path)
    return df

# Function to add new properties to the CSV file
def add_properties(data):
    df = load_data(file_path)
    new_data = pd.DataFrame(data)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(file_path, index=False)

# Function to display the Streamlit interface
def main():
    st.title("Tax Auction Property Management")

    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "View Properties", "Add Property"))

    if page == "Home":
        st.header("Welcome to Tax Auction Property Management")
        st.write("This application helps manage tax auction properties.")

    elif page == "View Properties":
        st.header("View Properties")
        df = load_data(file_path)
        st.dataframe(df)

    elif page == "Add Property":
        st.header("Add Property")
        state = st.text_input("State")
        county = st.text_input("County")
        auction_type = st.selectbox("Auction Type", ["Tax Deed", "Foreclosure Sale", "Tax Lien", "Sheriff Sale"])
        auction_date = st.date_input("Auction Date")
        online_offline = st.selectbox("Online/Offline Auction", ["Online", "Offline"])
        property_address = st.text_input("Property Address")
        parcel_number = st.text_input("Parcel Number")
        property_description = st.text_area("Property Description")
        zoning_info = st.text_input("Zoning Information")
        assessed_value = st.text_input("Assessed Value")
        market_value = st.text_input("Market Value")
        auction_platform = st.text_input("Auction Platform/Location")
        registration_req = st.text_area("Registration Requirements")
        bidding_process = st.text_area("Bidding Process")
        starting_bid = st.text_input("Starting Bid Amount")
        payment_terms = st.text_area("Payment Terms")
        redemption_period = st.text_input("Redemption Period")
        state_local_laws = st.text_area("State and Local Laws")
        tax_sale_reg = st.text_area("Tax Sale Regulations")
        redemption_rights = st.text_input("Redemption Rights")
        notification_req = st.text_area("Notification Requirements")
        legal_fees = st.text_input("Legal Fees")
        req_docs = st.text_area("Required Documentation")
        initial_investment = st.text_input("Initial Investment Amount")
        winning_bid = st.text_input("Winning Bid Amount")
        additional_costs = st.text_input("Additional Costs")
        potential_returns = st.text_input("Potential Returns")
        payment_due_dates = st.text_input("Payment Due Dates")
        payment_methods = st.text_area("Payment Methods")
        title_search = st.text_area("Title Search Results")
        env_concerns = st.text_input("Environmental Concerns")
        property_condition = st.text_area("Property Condition Reports")
        liens_encumbrances = st.text_area("Liens and Encumbrances")
        occupancy_status = st.text_area("Occupancy Status")
        properties_bid_on = st.text_area("Properties Bid On")
        bid_amounts = st.text_area("Bid Amounts")
        winning_status = st.text_area("Winning/Losing Status")
        followup_actions = st.text_area("Follow-up Actions for Winning Bids")
        payment_confirm = st.text_area("Payment Confirmation")
        deed_transfer = st.text_area("Deed/Lien Transfer Process")
        followup_redemption = st.text_area("Follow-up on Redemption Period")
        property_mgmt_plans = st.text_area("Property Management Plans")
        sale_strategy = st.text_area("Sale or Investment Strategy")
        auction_officials = st.text_area("Auction Officials")
        tax_office = st.text_area("County Tax Office")
        legal_advisors = st.text_area("Legal Advisors")
        property_inspectors = st.text_area("Property Inspectors")
        financial_institutions = st.text_area("Financial Institutions")
        auction_notes = st.text_area("Auction Day Notes")
        competitor_patterns = st.text_area("Competitor Bidding Patterns")
        lessons_learned = st.text_area("Lessons Learned")
        market_trends = st.text_area("Market Trends and Insights")
        cert_attached = st.text_area("Copies of Auction Certificates")
        receipts_attached = st.text_area("Receipts and Payment Confirmations")
        correspondence_files = st.text_area("Correspondence with Authorities")
        legal_files = st.text_area("Legal Documents and Filings")

        if st.button("Add Property"):
            new_property = {
                "State": state,
                "County": county,
                "Auction Type": auction_type,
                "Auction Date": auction_date,
                "Online/Offline Auction": online_offline,
                "Property Address": property_address,
                "Parcel Number": parcel_number,
                "Property Description": property_description,
                "Zoning Information": zoning_info,
                "Assessed Value": assessed_value,
                "Market Value": market_value,
                "Auction Platform/Location": auction_platform,
                "Registration Requirements": registration_req,
                "Bidding Process": bidding_process,
                "Starting Bid Amount": starting_bid,
                "Payment Terms": payment_terms,
                "Redemption Period": redemption_period,
                "State and Local Laws": state_local_laws,
                "Tax Sale Regulations": tax_sale_reg,
                "Redemption Rights": redemption_rights,
                "Notification Requirements": notification_req,
                "Legal Fees": legal_fees,
                "Required Documentation": req_docs,
                "Initial Investment Amount": initial_investment,
                "Winning Bid Amount": winning_bid,
                "Additional Costs": additional_costs,
                "Potential Returns": potential_returns,
                "Payment Due Dates": payment_due_dates,
                "Payment Methods": payment_methods,
                "Title Search Results": title_search,
                "Environmental Concerns": env_concerns,
                "Property Condition Reports": property_condition,
                "Liens and Encumbrances": liens_encumbrances,
                "Occupancy Status": occupancy_status,
                "Properties Bid On": properties_bid_on,
                "Bid Amounts": bid_amounts,
                "Winning/Losing Status": winning_status,
                "Follow-up Actions for Winning Bids": followup_actions,
                "Payment Confirmation": payment_confirm,
                "Deed/Lien Transfer Process": deed_transfer,
                "Follow-up on Redemption Period": followup_redemption,
                "Property Management Plans": property_mgmt_plans,
                "Sale or Investment Strategy": sale_strategy,
                "Auction Officials": auction_officials,
                "County Tax Office": tax_office,
                "Legal Advisors": legal_advisors,
                "Property Inspectors": property_inspectors,
                "Financial Institutions": financial_institutions,
                "Auction Day Notes": auction_notes,
                "Competitor Bidding Patterns": competitor_patterns,
                "Lessons Learned": lessons_learned,
                "Market Trends and Insights": market_trends,
                "Copies of Auction Certificates": cert_attached,
                "Receipts and Payment Confirmations": receipts_attached,
                "Correspondence with Authorities": correspondence_files,
                "Legal Documents and Filings": legal_files
            }
            add_properties([new_property])
            st.success("Property added successfully!")

# Entry point of the application
if __name__ == "__main__":
    main()

