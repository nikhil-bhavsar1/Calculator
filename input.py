import sys

# This is a standalone Python script. No external libraries are needed.

# Define conversion factors to a base unit (1)
CONVERSION_FACTORS = {
    'thousand': 1_000,
    'lakhs': 100_000,
    'million': 1_000_000,
    'cr': 10_000_000,
    'billion': 1_000_000_000,
}

# Define display names and zero counts for the table
UNIT_DETAILS = {
    'thousand': {'name': 'Thousand', 'zeroes': 3},
    'lakhs':    {'name': 'Lakhs', 'zeroes': 5},
    'million':  {'name': 'Million', 'zeroes': 6},
    'cr':       {'name': 'Crore (Cr)', 'zeroes': 7},
    'billion':  {'name': 'Billion', 'zeroes': 9},
}

# Get a sorted list of unit keys based on their value (magnitude)
SORTED_UNIT_KEYS = sorted(CONVERSION_FACTORS, key=CONVERSION_FACTORS.get)

def get_validated_float(prompt_message: str) -> float:
    """
    Prompts the user for a number and validates it,
    handling errors until a valid float is entered.
    """
    while True:
        try:
            user_input = input(prompt_message).strip()
            # Allow empty input for optional fields, default to 0.0
            if not user_input:
                return 0.0
            # Remove commas if user enters them (e.g., 1,000,000)
            user_input = user_input.replace(',', '')
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g., 1234.56) or leave blank for 0.")

def get_unit_choice(prompt_message: str) -> str:
    """
    Prompts the user to choose from a list of options and validates the choice.
    """
    print(f"\n{prompt_message}")
    
    # --- Reference Table ---
    print("\n  --- Unit Reference Table ---")
    print(f"  | {'Unit':<12} | {'Number of Zeroes':<18} |")
    print(f"  | :{'-'*10}: | :{'-'*16}: |")
    for key in SORTED_UNIT_KEYS:
        details = UNIT_DETAILS[key]
        print(f"  | {details['name']:<12} | {details['zeroes']:<18} |")
    print("  ----------------------------------\n")
    # --- End Table ---

    print("Please choose one of the following units by entering its number:")
    
    # Display numbered options
    for i, key in enumerate(SORTED_UNIT_KEYS, 1):
        print(f"  {i}: {UNIT_DETAILS[key]['name']}")
        
    while True:
        try:
            choice_str = input(f"Your choice (1-{len(SORTED_UNIT_KEYS)}): ").strip()
            choice_num = int(choice_str)
            if 1 <= choice_num <= len(SORTED_UNIT_KEYS):
                # Map the number back to the unit key (e.g., 1 -> 'thousand')
                return SORTED_UNIT_KEYS[choice_num - 1]
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(SORTED_UNIT_KEYS)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def convert_units(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converts a value from one financial unit to another.
    """
    if from_unit == to_unit:
        return value
        
    # Convert to base value (absolute number)
    absolute_value = value * CONVERSION_FACTORS[from_unit]
    
    # Convert from base value to target unit
    converted_value = absolute_value / CONVERSION_FACTORS[to_unit]
    
    return converted_value

def collect_financial_data(base_unit: str) -> dict:
    """
    Guides the user to enter all raw data from financial statements.
    """
    base_unit_name = UNIT_DETAILS[base_unit]['name']
    print("\n--- 📊 Data Collection ---")
    print(f"Please enter all values in {base_unit_name.upper()} unless specified otherwise.")
    print("Press ENTER to skip a field (it will be recorded as 0.0).\n")
    
    data = {}
    
    # ======================================================================
    # 🏛️ Balance Sheet (Statement of Financial Position)
    # ======================================================================
    print("--- 🏛️ Balance Sheet (Statement of Financial Position) ---")
    
    # --- Assets ---
    print("\n--- ASSETS ---")
    print("\n(Non-Current Assets)")
    data['ppe_gross'] = get_validated_float(f"  (-> Property, Plant and Equipment (Gross Block)) (in {base_unit_name}): ")
    data['accumulated_depreciation'] = get_validated_float(f"  (-> Accumulated Depreciation) (in {base_unit_name}): ")
    data['goodwill'] = get_validated_float(f"  (-> Goodwill) (in {base_unit_name}): ")
    data['other_intangible_assets'] = get_validated_float(f"  (-> Other Intangible Assets) (in {base_unit_name}): ")
    data['non_current_investments'] = get_validated_float(f"  (-> Financial Assets -> Investments) (in {base_unit_name}): ")

    print("\n(Current Assets)")
    data['inventories'] = get_validated_float(f"  (-> Inventories) (in {base_unit_name}): ")
    data['current_investments'] = get_validated_float(f"  (-> Financial Assets -> Current Investments) (in {base_unit_name}): ")
    data['trade_receivables'] = get_validated_float(f"  (-> Financial Assets -> Trade Receivables) (in {base_unit_name}): ")
    data['cash_and_equivalents'] = get_validated_float(f"  (-> Financial Assets -> Cash and Cash Equivalents) (in {base_unit_name}): ")
    data['bank_balances'] = get_validated_float(f"  (-> Financial Assets -> Bank Balances) (in {base_unit_name}): ")
    data['other_current_assets'] = get_validated_float(f"  (-> Other Current Assets) (in {base_unit_name}): ")

    # --- Equity and Liabilities ---
    print("\n--- EQUITY AND LIABILITIES ---")
    print("\n(Equity)")
    data['equity_share_capital'] = get_validated_float(f"  (-> Equity Share Capital) (in {base_unit_name}): ")
    data['other_equity'] = get_validated_float(f"  (-> Other Equity (incl. Retained Earnings)) (in {base_unit_name}): ")
    data['non_controlling_interest'] = get_validated_float(f"  (-> Non-Controlling Interests) (in {base_unit_name}): ")

    print("\n(Non-Current Liabilities)")
    data['long_term_borrowings'] = get_validated_float(f"  (-> Financial Liabilities -> Borrowings) (in {base_unit_name}): ")
    
    print("\n(Current Liabilities)")
    data['short_term_borrowings'] = get_validated_float(f"  (-> Financial Liabilities -> Borrowings) (in {base_unit_name}): ")
    data['trade_payables'] = get_validated_float(f"  (-> Financial Liabilities -> Trade Payables) (in {base_unit_name}): ")
    data['other_current_liabilities'] = get_validated_float(f"  (-> Other Current Liabilities) (in {base_unit_name}): ")
    data['current_provisions'] = get_validated_float(f"  (-> Provisions) (in {base_unit_name}): ")

    print("\n(Notes to Accounts - *Enter in absolute numbers, not units*)")
    data['shares_outstanding'] = get_validated_float("  (-> Notes -> Share Capital -> Number of Equity Shares Outstanding) (in absolute numbers): ")
    data['face_value_per_share'] = get_validated_float("  (-> Notes -> Share Capital -> Face Value per Share) (in currency, e.g., 10): ")

    # ======================================================================
    # 🧾 Statement of Profit and Loss (P&L)
    # ======================================================================
    print("\n\n--- 🧾 Statement of Profit and Loss (P&L) ---")
    
    print("\n(Income)")
    data['revenue_from_operations'] = get_validated_float(f"  (-> Revenue from Operations) (in {base_unit_name}): ")
    data['other_income'] = get_validated_float(f"  (-> Other Income) (in {base_unit_name}): ")

    print("\n(Expenses)")
    data['cost_materials_consumed'] = get_validated_float(f"  (-> Cost of Materials Consumed) (in {base_unit_name}): ")
    data['purchases_stock_in_trade'] = get_validated_float(f"  (-> Purchases of Stock-in-Trade) (in {base_unit_name}): ")
    data['changes_in_inventories'] = get_validated_float(f"  (-> Changes in Inventories) (in {base_unit_name}): ")
    data['employee_benefits_expense'] = get_validated_float(f"  (-> Employee Benefits Expense) (in {base_unit_name}): ")
    data['finance_costs'] = get_validated_float(f"  (-> Finance Costs (Interest Expense)) (in {base_unit_name}): ")
    data['depreciation_amortisation'] = get_validated_float(f"  (-> Depreciation and Amortisation Expense) (in {base_unit_name}): ")
    data['other_expenses'] = get_validated_float(f"  (-> Other Expenses) (in {base_unit_name}): ")
    
    print("\n(Profit & Tax)")
    data['profit_before_tax'] = get_validated_float(f"  (-> Profit before Tax) (in {base_unit_name}): ")
    data['tax_expense'] = get_validated_float(f"  (-> Tax Expense) (in {base_unit_name}): ")
    data['profit_for_period'] = get_validated_float(f"  (-> Profit for the Period (Net Income)) (in {base_unit_name}): ")

    print("\n(Earnings Per Share - *Enter in absolute numbers, not units*)")
    data['weighted_avg_shares'] = get_validated_float("  (-> Weighted Average Number of Equity Shares) (in absolute numbers): ")
    data['dilutive_potential_shares'] = get_validated_float("  (-> Dilutive Potential Equity Shares) (in absolute numbers): ")

    # ======================================================================
    # 🌊 Statement of Cash Flows
    # ======================================================================
    print("\n\n--- 🌊 Statement of Cash Flows ---")
    
    print("\n(Operating Activities - CFO)")
    data['cfo_profit_before_tax'] = get_validated_float(f"  (-> Profit Before Tax (Starting Point)) (in {base_unit_name}): ")
    data['cfo_depreciation_amortisation'] = get_validated_float(f"  (-> Adjustments -> Depreciation and Amortisation) (in {base_unit_name}): ")
    data['cfo_finance_costs'] = get_validated_float(f"  (-> Adjustments -> Finance Costs) (in {base_unit_name}): ")
    data['cfo_interest_income'] = get_validated_float(f"  (-> Adjustments -> Interest Income) (in {base_input_name}): ")
    data['cfo_change_inventories'] = get_validated_float(f"  (-> Adjustments -> (Increase)/Decrease in Inventories) (in {base_unit_name}): ")
    data['cfo_change_receivables'] = get_validated_float(f"  (-> Adjustments -> (Increase)/Decrease in Trade Receivables) (in {base_unit_name}): ")
    data['cfo_change_payables'] = get_validated_float(f"  (-> Adjustments -> Increase/(Decrease) in Trade Payables) (in {base_unit_name}): ")
    data['cash_generated_from_ops'] = get_validated_float(f"  (-> Cash Generated from Operations) (in {base_unit_name}): ")
    data['income_taxes_paid'] = get_validated_float(f"  (-> Income Taxes Paid) (in {base_unit_name}): ")
    
    print("\n(Investing Activities - CFI)")
    data['purchase_ppe'] = get_validated_float(f"  (-> Purchase of Property, Plant and Equipment) (in {base_unit_name}): ")
    data['sale_ppe'] = get_validated_float(f"  (-> Proceeds from Sale of Property, Plant and Equipment) (in {base_unit_name}): ")
    data['cfi_interest_received'] = get_validated_float(f"  (-> Interest Received) (in {base_unit_name}): ")
    data['cfi_dividends_received'] = get_validated_float(f"  (-> Dividends Received) (in {base_unit_name}): ")
    
    print("\n(Financing Activities - CFF)")
    data['proceeds_issue_shares'] = get_validated_float(f"  (-> Proceeds from Issue of Equity Shares) (in {base_unit_name}): ")
    data['proceeds_long_term_borrowings'] = get_validated_float(f"  (-> Proceeds from Long-Term Borrowings) (in {base_unit_name}): ")
    data['repayment_long_term_borrowings'] = get_validated_float(f"  (-> Repayment of Long-Term Borrowings) (in {base_unit_name}): ")
    data['cff_interest_paid'] = get_validated_float(f"  (-> Interest Paid (Finance Cost)) (in {base_unit_name}): ")
    data['dividends_paid'] = get_validated_float(f"  (-> Dividends Paid) (in {base_unit_name}): ")
    
    print("\n--- ✅ Data Collection Complete ---")
    return data

def main():
    """
    Main function to run the data collection and conversion script.
    """
    print("======================================================")
    print("     Financial Statement Data Collection Script     ")
    print("======================================================")
    print("This script will guide you to input raw data from your")
    print("financial statements (Balance Sheet, P&L, Cash Flow).")
    
    # 1. Get the base unit of the financial statements
    base_unit = get_unit_choice("First, what is the primary unit used in your statements?")
    base_unit_name = UNIT_DETAILS[base_unit]['name']
    
    # 2. Collect all financial data
    financial_data = collect_financial_data(base_unit)
    
    print("\n--- 📝 Collected Data Summary (in original units) ---")
    for key, value in financial_data.items():
        if key in ['shares_outstanding', 'face_value_per_share', 'weighted_avg_shares', 'dilutive_potential_shares']:
             print(f"  {key}: {value:,.0f} (Absolute Number)")
        else:
             print(f"  {key}: {value:,.2f} ({base_unit_name.upper()})")
             
    # 3. Offer to convert the data
    print("\n--- 🔄 Unit Conversion ---")
    while True:
        convert_choice = input("Would you like to convert this data to a different unit? (yes/no): ").strip().lower()
        if convert_choice in ['yes', 'y']:
            break
        elif convert_choice in ['no', 'n']:
            print("\nExiting. Have a great day!")
            sys.exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            
    # 4. Perform conversion
    target_unit = get_unit_choice("What unit would you like to convert TO?")
    target_unit_name = UNIT_DETAILS[target_unit]['name']
    
    if base_unit == target_unit:
        print(f"\nNo conversion needed. The data is already in {target_unit_name.upper()}.")
    else:
        print(f"\n--- 🔀 Converting data from {base_unit_name.upper()} to {target_unit_name.upper()} ---")
        converted_data = {}
        
        for key, value in financial_data.items():
            # Skip fields that are not in monetary units
            if key in ['shares_outstanding', 'face_value_per_share', 'weighted_avg_shares', 'dilutive_potential_shares']:
                converted_data[key] = value
                print(f"  {key}: {value:,.0f} (Absolute Number - Not Converted)")
            else:
                converted_value = convert_units(value, base_unit, target_unit)
                converted_data[key] = converted_value
                print(f"  {key}: {converted_value:,.4f} ({target_unit_name.upper()})")
                
        print("\n--- ✅ Conversion Complete ---")
        # You can now use the `converted_data` dictionary for further processing.
        # For example: print(converted_data)

    print("\nScript finished.")

if __name__ == "__main__":
    main()

# ---
#
# ## 🏛️ Balance Sheet Inputs
#
# * **Non-Current Assets**
#     * Property, Plant and Equipment (Gross Block)
#     * Accumulated Depreciation
#     * Goodwill
#     * Other Intangible Assets
#     * Financial Assets -> Investments
# * **Current Assets**
#     * Inventories
#     * Financial Assets -> Current Investments
#     * Financial Assets -> Trade Receivables
#     * Financial Assets -> Cash and Cash Equivalents
#     * Financial Assets -> Bank Balances
#     * Other Current Assets
# * **Equity**
#     * Equity Share Capital
#     * Other Equity (incl. Retained Earnings)
#     * Non-Controlling Interests
# * **Non-Current Liabilities**
#     * Financial Liabilities -> Borrowings (Long-Term)
# * **Current Liabilities**
#     * Financial Liabilities -> Borrowings (Short-Term)
#     * Financial Liabilities -> Trade Payables
#     * Other Current Liabilities
#     * Provisions
# * **Notes to Accounts**
#     * Number of Equity Shares Outstanding (Absolute Number)
#     * Face Value per Share (Absolute Number)
#
# ---
#
# ## 🧾 Income Statement Inputs (P&L)
#
# * **Income**
#     * Revenue from Operations
#     * Other Income
# * **Expenses**
#     * Cost of Materials Consumed
#     * Purchases of Stock-in-Trade
#     * Changes in Inventories
#     * Employee Benefits Expense
#     * Finance Costs (Interest Expense)
#     * Depreciation and Amortisation Expense
#     * Other Expenses
# * **Profit & Tax**
#     * Profit before Tax
#     * Tax Expense
#     * Profit for the Period (Net Income)
# * **Earnings Per Share (from P&L)**
#     * Weighted Average Number of Equity Shares (Absolute Number)
#     * Dilutive Potential Equity Shares (Absolute Number)
#
# ---
#
# ## 🌊 Cash Flow Inputs
#
# * **Operating Activities (CFO)**
#     * Profit Before Tax (Starting Point)
#     * Adjustments -> Depreciation and Amortisation
#     * Adjustments -> Finance Costs
#     * Adjustments -> Interest Income
#     * Adjustments -> (Increase)/Decrease in Inventories
#     * Adjustments -> (Increase)/Decrease in Trade Receivables
#     * Adjustments -> Increase/(Decrease) in Trade Payables
#     * Cash Generated from Operations
#     * Income Taxes Paid
# * **Investing Activities (CFI)**
#     * Purchase of Property, Plant and Equipment
#     * Proceeds from Sale of Property, Plant and Equipment
#     * Interest Received
#     * Dividends Received
# * **Financing Activities (CFF)**
#     * Proceeds from Issue of Equity Shares
#     * Proceeds from Long-Term Borrowings
#     * Repayment of Long-Term Borrowings
#     * Interest Paid (Finance Cost)
#     * Dividends Paid


