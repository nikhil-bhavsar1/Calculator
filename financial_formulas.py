"""
Comprehensive Financial Metrics Calculator
===========================================
This module contains Python implementations of all financial formulas including:
- Valuation Ratios
- Profitability Metrics
- Cash Flow Metrics
- Liquidity Metrics
- Leverage/Solvency Metrics
- Efficiency/Activity Metrics
- Growth Metrics
- Market Metrics
- Dividend Metrics
- DuPont Analysis
- Statistical Metrics
- DCF Valuation Framework
- Aswath Damodaran Formulas
- Benjamin Graham Formulas
- Modern Value Investing Formulas
"""

import math
from typing import List, Optional, Tuple

try:
    from scipy import stats
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False


# ============================================================================
# 1. VALUATION RATIOS
# ============================================================================

def price_to_earnings_ratio(market_price_per_share: float, eps: float) -> float:
    """
    Price-to-Earnings (P/E) Ratio
    Formula: Market Price Per Share / Earnings Per Share (EPS)
    """
    if eps == 0:
        raise ValueError("EPS cannot be zero")
    return market_price_per_share / eps


def price_to_earnings_ratio_market_cap(market_cap: float, net_income: float) -> float:
    """
    P/E Ratio using Market Capitalization
    Formula: Market Capitalization / Net Income
    """
    if net_income == 0:
        raise ValueError("Net Income cannot be zero")
    return market_cap / net_income


def price_to_book_ratio(market_price_per_share: float, book_value_per_share: float) -> float:
    """
    Price-to-Book (P/B) Ratio
    Formula: Market Price Per Share / Book Value Per Share
    """
    if book_value_per_share == 0:
        raise ValueError("Book Value Per Share cannot be zero")
    return market_price_per_share / book_value_per_share


def book_value_per_share(total_equity: float, shares_outstanding: float) -> float:
    """
    Book Value Per Share
    Formula: Total Equity / Shares Outstanding
    """
    if shares_outstanding == 0:
        raise ValueError("Shares Outstanding cannot be zero")
    return total_equity / shares_outstanding


def price_to_sales_ratio(market_price_per_share: float, revenue_per_share: float) -> float:
    """
    Price-to-Sales (P/S) Ratio
    Formula: Market Price Per Share / Revenue Per Share
    """
    if revenue_per_share == 0:
        raise ValueError("Revenue Per Share cannot be zero")
    return market_price_per_share / revenue_per_share


def price_to_sales_ratio_market_cap(market_cap: float, total_revenue: float) -> float:
    """
    P/S Ratio using Market Capitalization
    Formula: Market Capitalization / Total Revenue
    """
    if total_revenue == 0:
        raise ValueError("Total Revenue cannot be zero")
    return market_cap / total_revenue


def price_to_cash_flow_ratio(market_price_per_share: float, operating_cf_per_share: float) -> float:
    """
    Price-to-Cash Flow (P/CF) Ratio
    Formula: Market Price Per Share / Operating Cash Flow Per Share
    """
    if operating_cf_per_share == 0:
        raise ValueError("Operating Cash Flow Per Share cannot be zero")
    return market_price_per_share / operating_cf_per_share


def peg_ratio(pe_ratio: float, annual_eps_growth_rate: float) -> float:
    """
    PEG Ratio (Price/Earnings to Growth)
    Formula: P/E Ratio / Annual EPS Growth Rate (%)
    """
    if annual_eps_growth_rate == 0:
        raise ValueError("Annual EPS Growth Rate cannot be zero")
    return pe_ratio / annual_eps_growth_rate


def earnings_yield(eps: float, market_price_per_share: float) -> float:
    """
    Earnings-to-Price (E/P) Ratio (Earnings Yield)
    Formula: Earnings Per Share / Market Price Per Share
    """
    if market_price_per_share == 0:
        raise ValueError("Market Price Per Share cannot be zero")
    return eps / market_price_per_share


def enterprise_value(market_cap: float, total_debt: float, cash_and_equivalents: float,
                     minority_interest: float = 0, preferred_equity: float = 0) -> float:
    """
    Enterprise Value (EV)
    Formula: Market Cap + Total Debt + Minority Interest + Preferred Equity - Cash and Cash Equivalents
    """
    return market_cap + total_debt + minority_interest + preferred_equity - cash_and_equivalents


def ev_to_ebitda(enterprise_value: float, ebitda: float) -> float:
    """
    Enterprise Value-to-EBITDA (EV/EBITDA)
    Formula: Enterprise Value / EBITDA
    """
    if ebitda == 0:
        raise ValueError("EBITDA cannot be zero")
    return enterprise_value / ebitda


def ev_to_ebit(enterprise_value: float, ebit: float) -> float:
    """
    Enterprise Value-to-EBIT (EV/EBIT)
    Formula: Enterprise Value / EBIT
    """
    if ebit == 0:
        raise ValueError("EBIT cannot be zero")
    return enterprise_value / ebit


def ev_to_sales(enterprise_value: float, total_revenue: float) -> float:
    """
    Enterprise Value-to-Sales (EV/Sales)
    Formula: Enterprise Value / Total Revenue
    """
    if total_revenue == 0:
        raise ValueError("Total Revenue cannot be zero")
    return enterprise_value / total_revenue


def ev_to_free_cash_flow(enterprise_value: float, free_cash_flow: float) -> float:
    """
    Enterprise Value-to-Free Cash Flow (EV/FCF)
    Formula: Enterprise Value / Free Cash Flow
    """
    if free_cash_flow == 0:
        raise ValueError("Free Cash Flow cannot be zero")
    return enterprise_value / free_cash_flow


def price_to_tangible_book_value(market_price_per_share: float, tangible_book_value_per_share: float) -> float:
    """
    Price-to-Tangible Book Value
    Formula: Market Price Per Share / Tangible Book Value Per Share
    """
    if tangible_book_value_per_share == 0:
        raise ValueError("Tangible Book Value Per Share cannot be zero")
    return market_price_per_share / tangible_book_value_per_share


def tangible_book_value_per_share(total_equity: float, intangible_assets: float,
                                  goodwill: float, shares_outstanding: float) -> float:
    """
    Tangible Book Value Per Share
    Formula: (Total Equity - Intangible Assets - Goodwill) / Shares Outstanding
    """
    if shares_outstanding == 0:
        raise ValueError("Shares Outstanding cannot be zero")
    return (total_equity - intangible_assets - goodwill) / shares_outstanding


def price_to_free_cash_flow(market_price_per_share: float, fcf_per_share: float) -> float:
    """
    Price-to-Free Cash Flow (P/FCF)
    Formula: Market Price Per Share / Free Cash Flow Per Share
    """
    if fcf_per_share == 0:
        raise ValueError("Free Cash Flow Per Share cannot be zero")
    return market_price_per_share / fcf_per_share


def ev_to_operating_income(enterprise_value: float, operating_income: float) -> float:
    """
    EV-to-Operating Income
    Formula: Enterprise Value / Operating Income
    """
    if operating_income == 0:
        raise ValueError("Operating Income cannot be zero")
    return enterprise_value / operating_income


# ============================================================================
# 2. PROFITABILITY METRICS
# ============================================================================

def net_income(total_revenue: float, total_expenses: float) -> float:
    """
    Net Income
    Formula: Total Revenue - Total Expenses
    """
    return total_revenue - total_expenses


def gross_profit(total_revenue: float, cogs: float) -> float:
    """
    Gross Profit
    Formula: Total Revenue - Cost of Goods Sold (COGS)
    """
    return total_revenue - cogs


def operating_income(gross_profit: float, operating_expenses: float) -> float:
    """
    Operating Income (EBIT)
    Formula: Gross Profit - Operating Expenses
    """
    return gross_profit - operating_expenses


def ebitda(operating_income: float, depreciation: float, amortization: float) -> float:
    """
    EBITDA
    Formula: Operating Income + Depreciation + Amortization
    """
    return operating_income + depreciation + amortization


def ebitda_from_net_income(net_income: float, interest: float, taxes: float,
                           depreciation: float, amortization: float) -> float:
    """
    EBITDA from Net Income
    Formula: Net Income + Interest + Taxes + Depreciation + Amortization
    """
    return net_income + interest + taxes + depreciation + amortization


def earnings_per_share(net_income: float, preferred_dividends: float,
                       weighted_avg_shares: float) -> float:
    """
    Earnings Per Share (EPS)
    Formula: (Net Income - Preferred Dividends) / Weighted Average Shares Outstanding
    """
    if weighted_avg_shares == 0:
        raise ValueError("Weighted Average Shares cannot be zero")
    return (net_income - preferred_dividends) / weighted_avg_shares


def diluted_eps(net_income: float, preferred_dividends: float,
                weighted_avg_shares: float, dilutive_securities: float) -> float:
    """
    Diluted EPS
    Formula: (Net Income - Preferred Dividends) / (Weighted Avg Shares + Dilutive Securities)
    """
    denominator = weighted_avg_shares + dilutive_securities
    if denominator == 0:
        raise ValueError("Total shares (including dilutive) cannot be zero")
    return (net_income - preferred_dividends) / denominator


def gross_profit_margin(gross_profit: float, total_revenue: float) -> float:
    """
    Gross Profit Margin (%)
    Formula: (Gross Profit / Total Revenue) × 100
    """
    if total_revenue == 0:
        raise ValueError("Total Revenue cannot be zero")
    return (gross_profit / total_revenue) * 100


def operating_margin(operating_income: float, total_revenue: float) -> float:
    """
    Operating Margin (%)
    Formula: (Operating Income / Total Revenue) × 100
    """
    if total_revenue == 0:
        raise ValueError("Total Revenue cannot be zero")
    return (operating_income / total_revenue) * 100


def net_profit_margin(net_income: float, total_revenue: float) -> float:
    """
    Net Profit Margin (%)
    Formula: (Net Income / Total Revenue) × 100
    """
    if total_revenue == 0:
        raise ValueError("Total Revenue cannot be zero")
    return (net_income / total_revenue) * 100


def ebitda_margin(ebitda: float, total_revenue: float) -> float:
    """
    EBITDA Margin (%)
    Formula: (EBITDA / Total Revenue) × 100
    """
    if total_revenue == 0:
        raise ValueError("Total Revenue cannot be zero")
    return (ebitda / total_revenue) * 100


def return_on_assets(net_income: float, average_total_assets: float) -> float:
    """
    Return on Assets (ROA) (%)
    Formula: (Net Income / Average Total Assets) × 100
    """
    if average_total_assets == 0:
        raise ValueError("Average Total Assets cannot be zero")
    return (net_income / average_total_assets) * 100


def return_on_equity(net_income: float, average_shareholders_equity: float) -> float:
    """
    Return on Equity (ROE) (%)
    Formula: (Net Income / Average Shareholders' Equity) × 100
    """
    if average_shareholders_equity == 0:
        raise ValueError("Average Shareholders' Equity cannot be zero")
    return (net_income / average_shareholders_equity) * 100


def return_on_investment(current_value: float, cost_of_investment: float) -> float:
    """
    Return on Investment (ROI) (%)
    Formula: [(Current Value of Investment - Cost of Investment) / Cost of Investment] × 100
    """
    if cost_of_investment == 0:
        raise ValueError("Cost of Investment cannot be zero")
    return ((current_value - cost_of_investment) / cost_of_investment) * 100


def nopat(ebit: float, tax_rate: float) -> float:
    """
    Net Operating Profit After Tax (NOPAT)
    Formula: EBIT × (1 - Tax Rate)
    """
    return ebit * (1 - tax_rate)


def return_on_invested_capital(nopat: float, total_debt: float, total_equity: float) -> float:
    """
    Return on Invested Capital (ROIC) (%)
    Formula: [NOPAT / (Total Debt + Total Equity)] × 100
    """
    invested_capital = total_debt + total_equity
    if invested_capital == 0:
        raise ValueError("Invested Capital cannot be zero")
    return (nopat / invested_capital) * 100


def return_on_capital_employed(ebit: float, total_assets: float, current_liabilities: float) -> float:
    """
    Return on Capital Employed (ROCE) (%)
    Formula: [EBIT / (Total Assets - Current Liabilities)] × 100
    """
    capital_employed = total_assets - current_liabilities
    if capital_employed == 0:
        raise ValueError("Capital Employed cannot be zero")
    return (ebit / capital_employed) * 100


def return_on_net_assets(net_income: float, fixed_assets: float, net_working_capital: float) -> float:
    """
    Return on Net Assets (RONA) (%)
    Formula: (Net Income / (Fixed Assets + Net Working Capital)) × 100
    """
    denominator = fixed_assets + net_working_capital
    if denominator == 0:
        raise ValueError("Fixed Assets + Net Working Capital cannot be zero")
    return (net_income / denominator) * 100


def pre_tax_profit_margin(earnings_before_tax: float, total_revenue: float) -> float:
    """
    Pre-Tax Profit Margin (%)
    Formula: (Earnings Before Tax / Total Revenue) × 100
    """
    if total_revenue == 0:
        raise ValueError("Total Revenue cannot be zero")
    return (earnings_before_tax / total_revenue) * 100


def after_tax_margin(net_income_after_tax: float, total_revenue: float) -> float:
    """
    After-Tax Margin (%)
    Formula: (Net Income After Tax / Total Revenue) × 100
    """
    if total_revenue == 0:
        raise ValueError("Total Revenue cannot be zero")
    return (net_income_after_tax / total_revenue) * 100


def cash_return_on_assets(operating_cash_flow: float, average_total_assets: float) -> float:
    """
    Cash Return on Assets (%)
    Formula: (Operating Cash Flow / Average Total Assets) × 100
    """
    if average_total_assets == 0:
        raise ValueError("Average Total Assets cannot be zero")
    return (operating_cash_flow / average_total_assets) * 100


def cash_return_on_equity(operating_cash_flow: float, average_shareholders_equity: float) -> float:
    """
    Cash Return on Equity (%)
    Formula: (Operating Cash Flow / Average Shareholders' Equity) × 100
    """
    if average_shareholders_equity == 0:
        raise ValueError("Average Shareholders' Equity cannot be zero")
    return (operating_cash_flow / average_shareholders_equity) * 100


# ============================================================================
# 3. CASH FLOW METRICS
# ============================================================================

def operating_cash_flow(net_income: float, non_cash_expenses: float,
                       change_in_working_capital: float) -> float:
    """
    Operating Cash Flow (OCF)
    Formula: Net Income + Non-Cash Expenses + Changes in Working Capital
    """
    return net_income + non_cash_expenses + change_in_working_capital


def operating_cash_flow_alt(ebitda: float, taxes_paid: float,
                            change_in_net_working_capital: float) -> float:
    """
    Operating Cash Flow (Alternative)
    Formula: EBITDA - Taxes Paid - Change in Net Working Capital
    """
    return ebitda - taxes_paid - change_in_net_working_capital


def free_cash_flow(operating_cash_flow: float, capital_expenditures: float) -> float:
    """
    Free Cash Flow (FCF)
    Formula: Operating Cash Flow - Capital Expenditures
    """
    return operating_cash_flow - capital_expenditures


def free_cash_flow_to_equity(net_income: float, capex: float, depreciation: float,
                             change_in_nwc: float, new_debt: float, debt_repayment: float) -> float:
    """
    Free Cash Flow to Equity (FCFE)
    Formula: Net Income - (CapEx - Depreciation) - Change in NWC + (New Debt - Debt Repayment)
    """
    return net_income - (capex - depreciation) - change_in_nwc + (new_debt - debt_repayment)


def free_cash_flow_to_firm(ebit: float, tax_rate: float, depreciation: float,
                          capex: float, change_in_nwc: float) -> float:
    """
    Free Cash Flow to Firm (FCFF)
    Formula: EBIT(1 - Tax Rate) + Depreciation - CapEx - Change in NWC
    """
    return ebit * (1 - tax_rate) + depreciation - capex - change_in_nwc


def fcff_from_nopat(nopat: float, depreciation: float, capex: float,
                    change_in_nwc: float) -> float:
    """
    FCFF from NOPAT
    Formula: NOPAT + Depreciation - CapEx - Change in NWC
    """
    return nopat + depreciation - capex - change_in_nwc


def fcff_from_cfo(cfo: float, interest_expense: float, tax_rate: float, capex: float) -> float:
    """
    FCFF from Cash Flow Statement
    Formula: CFO + Interest Expense(1 - Tax Rate) - CapEx
    """
    return cfo + interest_expense * (1 - tax_rate) - capex


def cash_flow_per_share(operating_cash_flow: float, shares_outstanding: float) -> float:
    """
    Cash Flow Per Share
    Formula: Operating Cash Flow / Shares Outstanding
    """
    if shares_outstanding == 0:
        raise ValueError("Shares Outstanding cannot be zero")
    return operating_cash_flow / shares_outstanding


def free_cash_flow_per_share(free_cash_flow: float, shares_outstanding: float) -> float:
    """
    Free Cash Flow Per Share
    Formula: Free Cash Flow / Shares Outstanding
    """
    if shares_outstanding == 0:
        raise ValueError("Shares Outstanding cannot be zero")
    return free_cash_flow / shares_outstanding


def free_cash_flow_margin(free_cash_flow: float, total_revenue: float) -> float:
    """
    Free Cash Flow Margin (%)
    Formula: (Free Cash Flow / Total Revenue) × 100
    """
    if total_revenue == 0:
        raise ValueError("Total Revenue cannot be zero")
    return (free_cash_flow / total_revenue) * 100


def cash_flow_to_debt_ratio(operating_cash_flow: float, total_debt: float) -> float:
    """
    Cash Flow-to-Debt Ratio
    Formula: Operating Cash Flow / Total Debt
    """
    if total_debt == 0:
        raise ValueError("Total Debt cannot be zero")
    return operating_cash_flow / total_debt


def operating_cash_flow_ratio(operating_cash_flow: float, current_liabilities: float) -> float:
    """
    Operating Cash Flow Ratio
    Formula: Operating Cash Flow / Current Liabilities
    """
    if current_liabilities == 0:
        raise ValueError("Current Liabilities cannot be zero")
    return operating_cash_flow / current_liabilities


def cash_flow_return_on_investment(gross_cash_flow: float, gross_investment: float) -> float:
    """
    Cash Flow Return on Investment (CFROI) (%)
    Formula: [Gross Cash Flow / Gross Investment] × 100
    """
    if gross_investment == 0:
        raise ValueError("Gross Investment cannot be zero")
    return (gross_cash_flow / gross_investment) * 100


def gross_cash_flow(ebitda: float, cash_taxes: float) -> float:
    """
    Gross Cash Flow
    Formula: EBITDA - Cash Taxes
    """
    return ebitda - cash_taxes


def unlevered_free_cash_flow(ebit: float, tax_rate: float, depreciation: float,
                             capex: float, change_in_nwc: float) -> float:
    """
    Unlevered Free Cash Flow
    Formula: EBIT(1 - Tax Rate) + Depreciation - CapEx - Change in NWC
    """
    return ebit * (1 - tax_rate) + depreciation - capex - change_in_nwc


def levered_free_cash_flow(net_income: float, depreciation: float, capex: float,
                           change_in_nwc: float, debt_repayment: float, new_debt: float) -> float:
    """
    Levered Free Cash Flow
    Formula: Net Income + Depreciation - CapEx - Change in NWC - Debt Repayment + New Debt
    """
    return net_income + depreciation - capex - change_in_nwc - debt_repayment + new_debt


def owner_earnings(net_income: float, depreciation_amortization: float,
                  capex: float, additional_working_capital: float) -> float:
    """
    Owner Earnings (Buffett's metric)
    Formula: Net Income + Depreciation & Amortization - CapEx - Additional Working Capital
    """
    return net_income + depreciation_amortization - capex - additional_working_capital


# ============================================================================
# 4. LIQUIDITY METRICS
# ============================================================================

def current_ratio(current_assets: float, current_liabilities: float) -> float:
    """
    Current Ratio
    Formula: Current Assets / Current Liabilities
    """
    if current_liabilities == 0:
        raise ValueError("Current Liabilities cannot be zero")
    return current_assets / current_liabilities


def quick_ratio(current_assets: float, inventory: float, current_liabilities: float) -> float:
    """
    Quick Ratio (Acid-Test Ratio)
    Formula: (Current Assets - Inventory) / Current Liabilities
    """
    if current_liabilities == 0:
        raise ValueError("Current Liabilities cannot be zero")
    return (current_assets - inventory) / current_liabilities


def quick_ratio_alt(cash: float, marketable_securities: float,
                    accounts_receivable: float, current_liabilities: float) -> float:
    """
    Quick Ratio (Alternative)
    Formula: (Cash + Marketable Securities + Accounts Receivable) / Current Liabilities
    """
    if current_liabilities == 0:
        raise ValueError("Current Liabilities cannot be zero")
    return (cash + marketable_securities + accounts_receivable) / current_liabilities


def cash_ratio(cash: float, cash_equivalents: float, current_liabilities: float) -> float:
    """
    Cash Ratio
    Formula: (Cash + Cash Equivalents) / Current Liabilities
    """
    if current_liabilities == 0:
        raise ValueError("Current Liabilities cannot be zero")
    return (cash + cash_equivalents) / current_liabilities


def working_capital(current_assets: float, current_liabilities: float) -> float:
    """
    Working Capital
    Formula: Current Assets - Current Liabilities
    """
    return current_assets - current_liabilities


def net_working_capital_ratio(current_assets: float, current_liabilities: float,
                              total_assets: float) -> float:
    """
    Net Working Capital Ratio
    Formula: (Current Assets - Current Liabilities) / Total Assets
    """
    if total_assets == 0:
        raise ValueError("Total Assets cannot be zero")
    return (current_assets - current_liabilities) / total_assets


def defensive_interval_ratio(cash: float, marketable_securities: float,
                            accounts_receivable: float, daily_operating_expenses: float) -> float:
    """
    Defensive Interval Ratio
    Formula: (Cash + Marketable Securities + Accounts Receivable) / Daily Operating Expenses
    """
    if daily_operating_expenses == 0:
        raise ValueError("Daily Operating Expenses cannot be zero")
    return (cash + marketable_securities + accounts_receivable) / daily_operating_expenses


def daily_operating_expenses(annual_operating_expenses: float) -> float:
    """
    Daily Operating Expenses
    Formula: Annual Operating Expenses / 365
    """
    return annual_operating_expenses / 365


def cash_flow_coverage_ratio(operating_cash_flow: float, total_debt: float) -> float:
    """
    Cash Flow Coverage Ratio
    Formula: Operating Cash Flow / Total Debt
    """
    if total_debt == 0:
        raise ValueError("Total Debt cannot be zero")
    return operating_cash_flow / total_debt


def operating_cash_flow_to_current_liabilities(operating_cash_flow: float,
                                               current_liabilities: float) -> float:
    """
    Operating Cash Flow to Current Liabilities
    Formula: Operating Cash Flow / Current Liabilities
    """
    if current_liabilities == 0:
        raise ValueError("Current Liabilities cannot be zero")
    return operating_cash_flow / current_liabilities


# ============================================================================
# 5. LEVERAGE/SOLVENCY METRICS
# ============================================================================

def debt_to_equity_ratio(total_debt: float, total_shareholders_equity: float) -> float:
    """
    Debt-to-Equity Ratio
    Formula: Total Debt / Total Shareholders' Equity
    """
    if total_shareholders_equity == 0:
        raise ValueError("Total Shareholders' Equity cannot be zero")
    return total_debt / total_shareholders_equity


def debt_to_assets_ratio(total_debt: float, total_assets: float) -> float:
    """
    Debt-to-Assets Ratio
    Formula: Total Debt / Total Assets
    """
    if total_assets == 0:
        raise ValueError("Total Assets cannot be zero")
    return total_debt / total_assets


def debt_to_ebitda_ratio(total_debt: float, ebitda: float) -> float:
    """
    Debt-to-EBITDA Ratio
    Formula: Total Debt / EBITDA
    """
    if ebitda == 0:
        raise ValueError("EBITDA cannot be zero")
    return total_debt / ebitda


def interest_coverage_ratio(ebit: float, interest_expense: float) -> float:
    """
    Interest Coverage Ratio
    Formula: EBIT / Interest Expense
    """
    if interest_expense == 0:
        raise ValueError("Interest Expense cannot be zero")
    return ebit / interest_expense


def debt_service_coverage_ratio(net_operating_income: float, total_debt_service: float) -> float:
    """
    Debt Service Coverage Ratio (DSCR)
    Formula: Net Operating Income / Total Debt Service
    """
    if total_debt_service == 0:
        raise ValueError("Total Debt Service cannot be zero")
    return net_operating_income / total_debt_service


def total_debt_service(principal_repayment: float, interest_payments: float) -> float:
    """
    Total Debt Service
    Formula: Principal Repayment + Interest Payments
    """
    return principal_repayment + interest_payments


def equity_multiplier(total_assets: float, total_shareholders_equity: float) -> float:
    """
    Equity Multiplier
    Formula: Total Assets / Total Shareholders' Equity
    """
    if total_shareholders_equity == 0:
        raise ValueError("Total Shareholders' Equity cannot be zero")
    return total_assets / total_shareholders_equity


def equity_multiplier_from_debt_equity(debt_to_equity: float) -> float:
    """
    Equity Multiplier from Debt-to-Equity
    Formula: 1 + Debt-to-Equity Ratio
    """
    return 1 + debt_to_equity


def financial_leverage_ratio(total_assets: float, total_equity: float) -> float:
    """
    Financial Leverage Ratio
    Formula: Total Assets / Total Equity
    """
    if total_equity == 0:
        raise ValueError("Total Equity cannot be zero")
    return total_assets / total_equity


def total_debt_ratio(total_debt: float, total_assets: float) -> float:
    """
    Total Debt Ratio
    Formula: Total Debt / Total Assets
    """
    if total_assets == 0:
        raise ValueError("Total Assets cannot be zero")
    return total_debt / total_assets


def long_term_debt_to_equity(long_term_debt: float, total_shareholders_equity: float) -> float:
    """
    Long-term Debt to Equity
    Formula: Long-term Debt / Total Shareholders' Equity
    """
    if total_shareholders_equity == 0:
        raise ValueError("Total Shareholders' Equity cannot be zero")
    return long_term_debt / total_shareholders_equity


def fixed_charge_coverage_ratio(ebit: float, fixed_charges: float, interest_expense: float) -> float:
    """
    Fixed Charge Coverage Ratio
    Formula: (EBIT + Fixed Charges) / (Fixed Charges + Interest Expense)
    """
    denominator = fixed_charges + interest_expense
    if denominator == 0:
        raise ValueError("Fixed Charges + Interest Expense cannot be zero")
    return (ebit + fixed_charges) / denominator


def times_interest_earned(ebit: float, interest_expense: float) -> float:
    """
    Times Interest Earned (TIE)
    Formula: EBIT / Interest Expense
    """
    if interest_expense == 0:
        raise ValueError("Interest Expense cannot be zero")
    return ebit / interest_expense


def debt_to_capital_ratio(total_debt: float, total_equity: float) -> float:
    """
    Debt-to-Capital Ratio
    Formula: Total Debt / (Total Debt + Total Equity)
    """
    total_capital = total_debt + total_equity
    if total_capital == 0:
        raise ValueError("Total Capital cannot be zero")
    return total_debt / total_capital


def net_debt_to_ebitda(total_debt: float, cash_and_equivalents: float, ebitda: float) -> float:
    """
    Net Debt-to-EBITDA
    Formula: (Total Debt - Cash & Cash Equivalents) / EBITDA
    """
    if ebitda == 0:
        raise ValueError("EBITDA cannot be zero")
    return (total_debt - cash_and_equivalents) / ebitda


def net_debt_to_equity(total_debt: float, cash_and_equivalents: float,
                      total_equity: float) -> float:
    """
    Net Debt-to-Equity
    Formula: (Total Debt - Cash & Cash Equivalents) / Total Equity
    """
    if total_equity == 0:
        raise ValueError("Total Equity cannot be zero")
    return (total_debt - cash_and_equivalents) / total_equity


def capitalization_ratio(long_term_debt: float, shareholders_equity: float) -> float:
    """
    Capitalization Ratio
    Formula: Long-term Debt / (Long-term Debt + Shareholders' Equity)
    """
    total_capitalization = long_term_debt + shareholders_equity
    if total_capitalization == 0:
        raise ValueError("Total Capitalization cannot be zero")
    return long_term_debt / total_capitalization


# ============================================================================
# 6. EFFICIENCY/ACTIVITY METRICS
# ============================================================================

def asset_turnover_ratio(net_sales: float, average_total_assets: float) -> float:
    """
    Asset Turnover Ratio
    Formula: Net Sales / Average Total Assets
    """
    if average_total_assets == 0:
        raise ValueError("Average Total Assets cannot be zero")
    return net_sales / average_total_assets


def inventory_turnover_ratio(cogs: float, average_inventory: float) -> float:
    """
    Inventory Turnover Ratio
    Formula: Cost of Goods Sold / Average Inventory
    """
    if average_inventory == 0:
        raise ValueError("Average Inventory cannot be zero")
    return cogs / average_inventory


def inventory_turnover_ratio_alt(net_sales: float, average_inventory: float) -> float:
    """
    Inventory Turnover Ratio (Alternative)
    Formula: Net Sales / Average Inventory
    """
    if average_inventory == 0:
        raise ValueError("Average Inventory cannot be zero")
    return net_sales / average_inventory


def receivables_turnover_ratio(net_credit_sales: float, average_accounts_receivable: float) -> float:
    """
    Receivables Turnover Ratio
    Formula: Net Credit Sales / Average Accounts Receivable
    """
    if average_accounts_receivable == 0:
        raise ValueError("Average Accounts Receivable cannot be zero")
    return net_credit_sales / average_accounts_receivable


def days_sales_outstanding(accounts_receivable: float, total_credit_sales: float) -> float:
    """
    Days Sales Outstanding (DSO)
    Formula: (Accounts Receivable / Total Credit Sales) × 365
    """
    if total_credit_sales == 0:
        raise ValueError("Total Credit Sales cannot be zero")
    return (accounts_receivable / total_credit_sales) * 365


def days_sales_outstanding_alt(receivables_turnover: float) -> float:
    """
    Days Sales Outstanding (Alternative)
    Formula: 365 / Receivables Turnover Ratio
    """
    if receivables_turnover == 0:
        raise ValueError("Receivables Turnover cannot be zero")
    return 365 / receivables_turnover


def days_inventory_outstanding(average_inventory: float, cogs: float) -> float:
    """
    Days Inventory Outstanding (DIO)
    Formula: (Average Inventory / COGS) × 365
    """
    if cogs == 0:
        raise ValueError("COGS cannot be zero")
    return (average_inventory / cogs) * 365


def days_inventory_outstanding_alt(inventory_turnover: float) -> float:
    """
    Days Inventory Outstanding (Alternative)
    Formula: 365 / Inventory Turnover Ratio
    """
    if inventory_turnover == 0:
        raise ValueError("Inventory Turnover cannot be zero")
    return 365 / inventory_turnover


def days_payable_outstanding(accounts_payable: float, cogs: float) -> float:
    """
    Days Payable Outstanding (DPO)
    Formula: (Accounts Payable / COGS) × 365
    """
    if cogs == 0:
        raise ValueError("COGS cannot be zero")
    return (accounts_payable / cogs) * 365


def days_payable_outstanding_alt(payables_turnover: float) -> float:
    """
    Days Payable Outstanding (Alternative)
    Formula: 365 / Payables Turnover Ratio
    """
    if payables_turnover == 0:
        raise ValueError("Payables Turnover cannot be zero")
    return 365 / payables_turnover


def cash_conversion_cycle(dso: float, dio: float, dpo: float) -> float:
    """
    Cash Conversion Cycle (CCC)
    Formula: DSO + DIO - DPO
    """
    return dso + dio - dpo


def payables_turnover_ratio(cogs: float, average_accounts_payable: float) -> float:
    """
    Payables Turnover Ratio
    Formula: COGS / Average Accounts Payable
    """
    if average_accounts_payable == 0:
        raise ValueError("Average Accounts Payable cannot be zero")
    return cogs / average_accounts_payable


def fixed_asset_turnover(net_sales: float, net_fixed_assets: float) -> float:
    """
    Fixed Asset Turnover
    Formula: Net Sales / Net Fixed Assets
    """
    if net_fixed_assets == 0:
        raise ValueError("Net Fixed Assets cannot be zero")
    return net_sales / net_fixed_assets


def net_fixed_assets(gross_fixed_assets: float, accumulated_depreciation: float) -> float:
    """
    Net Fixed Assets
    Formula: Gross Fixed Assets - Accumulated Depreciation
    """
    return gross_fixed_assets - accumulated_depreciation


def total_asset_turnover(net_sales: float, average_total_assets: float) -> float:
    """
    Total Asset Turnover
    Formula: Net Sales / Average Total Assets
    """
    if average_total_assets == 0:
        raise ValueError("Average Total Assets cannot be zero")
    return net_sales / average_total_assets


def working_capital_turnover(net_sales: float, average_working_capital: float) -> float:
    """
    Working Capital Turnover
    Formula: Net Sales / Average Working Capital
    """
    if average_working_capital == 0:
        raise ValueError("Average Working Capital cannot be zero")
    return net_sales / average_working_capital


def capital_employed_turnover(revenue: float, capital_employed: float) -> float:
    """
    Capital Employed Turnover
    Formula: Revenue / Capital Employed
    """
    if capital_employed == 0:
        raise ValueError("Capital Employed cannot be zero")
    return revenue / capital_employed


def capital_employed(total_assets: float, current_liabilities: float) -> float:
    """
    Capital Employed
    Formula: Total Assets - Current Liabilities
    """
    return total_assets - current_liabilities


def net_working_capital_turnover(revenue: float, net_working_capital: float) -> float:
    """
    Net Working Capital Turnover
    Formula: Revenue / Net Working Capital
    """
    if net_working_capital == 0:
        raise ValueError("Net Working Capital cannot be zero")
    return revenue / net_working_capital


def equity_turnover(revenue: float, average_shareholders_equity: float) -> float:
    """
    Equity Turnover
    Formula: Revenue / Average Shareholders' Equity
    """
    if average_shareholders_equity == 0:
        raise ValueError("Average Shareholders' Equity cannot be zero")
    return revenue / average_shareholders_equity


# ============================================================================
# 7. GROWTH METRICS
# ============================================================================

def revenue_growth_rate(current_revenue: float, previous_revenue: float) -> float:
    """
    Revenue Growth Rate (%)
    Formula: [(Current Period Revenue - Previous Period Revenue) / Previous Period Revenue] × 100
    """
    if previous_revenue == 0:
        raise ValueError("Previous Period Revenue cannot be zero")
    return ((current_revenue - previous_revenue) / previous_revenue) * 100


def earnings_growth_rate(current_earnings: float, previous_earnings: float) -> float:
    """
    Earnings Growth Rate (%)
    Formula: [(Current Period Earnings - Previous Period Earnings) / Previous Period Earnings] × 100
    """
    if previous_earnings == 0:
        raise ValueError("Previous Period Earnings cannot be zero")
    return ((current_earnings - previous_earnings) / previous_earnings) * 100


def eps_growth_rate(current_eps: float, previous_eps: float) -> float:
    """
    EPS Growth Rate (%)
    Formula: [(Current EPS - Previous EPS) / Previous EPS] × 100
    """
    if previous_eps == 0:
        raise ValueError("Previous EPS cannot be zero")
    return ((current_eps - previous_eps) / previous_eps) * 100


def compound_annual_growth_rate(ending_value: float, beginning_value: float,
                                number_of_years: float) -> float:
    """
    Compound Annual Growth Rate (CAGR) (%)
    Formula: [(Ending Value / Beginning Value)^(1/Number of Years) - 1] × 100
    """
    if beginning_value == 0:
        raise ValueError("Beginning Value cannot be zero")
    if number_of_years == 0:
        raise ValueError("Number of Years cannot be zero")
    return ((ending_value / beginning_value) ** (1 / number_of_years) - 1) * 100


def year_over_year_growth(current_year_value: float, previous_year_value: float) -> float:
    """
    Year-over-Year (YoY) Growth (%)
    Formula: [(Current Year Value - Previous Year Value) / Previous Year Value] × 100
    """
    if previous_year_value == 0:
        raise ValueError("Previous Year Value cannot be zero")
    return ((current_year_value - previous_year_value) / previous_year_value) * 100


def quarter_over_quarter_growth(current_quarter_value: float,
                                previous_quarter_value: float) -> float:
    """
    Quarter-over-Quarter (QoQ) Growth (%)
    Formula: [(Current Quarter Value - Previous Quarter Value) / Previous Quarter Value] × 100
    """
    if previous_quarter_value == 0:
        raise ValueError("Previous Quarter Value cannot be zero")
    return ((current_quarter_value - previous_quarter_value) / previous_quarter_value) * 100


def sustainable_growth_rate(roe: float, dividend_payout_ratio: float) -> float:
    """
    Sustainable Growth Rate (SGR) (%)
    Formula: ROE × (1 - Dividend Payout Ratio)
    """
    return roe * (1 - dividend_payout_ratio)


def sustainable_growth_rate_alt(roe: float, retention_ratio: float) -> float:
    """
    Sustainable Growth Rate (Alternative)
    Formula: ROE × Retention Ratio
    """
    return roe * retention_ratio


def internal_growth_rate(roa: float, retention_ratio: float) -> float:
    """
    Internal Growth Rate (%)
    Formula: (ROA × Retention Ratio) / (1 - ROA × Retention Ratio)
    """
    denominator = 1 - (roa * retention_ratio)
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    return ((roa * retention_ratio) / denominator) * 100


def retention_ratio(dividend_payout_ratio: float) -> float:
    """
    Retention Ratio
    Formula: 1 - Dividend Payout Ratio
    """
    return 1 - dividend_payout_ratio


def dividend_growth_rate(current_dividend: float, previous_dividend: float) -> float:
    """
    Dividend Growth Rate (%)
    Formula: [(Current Dividend - Previous Dividend) / Previous Dividend] × 100
    """
    if previous_dividend == 0:
        raise ValueError("Previous Dividend cannot be zero")
    return ((current_dividend - previous_dividend) / previous_dividend) * 100


def book_value_growth_rate(current_book_value: float, previous_book_value: float) -> float:
    """
    Book Value Growth Rate (%)
    Formula: [(Current Book Value - Previous Book Value) / Previous Book Value] × 100
    """
    if previous_book_value == 0:
        raise ValueError("Previous Book Value cannot be zero")
    return ((current_book_value - previous_book_value) / previous_book_value) * 100


# ============================================================================
# 8. MARKET METRICS
# ============================================================================

def market_capitalization(current_stock_price: float, total_shares_outstanding: float) -> float:
    """
    Market Capitalization
    Formula: Current Stock Price × Total Shares Outstanding
    """
    return current_stock_price * total_shares_outstanding


def book_value(total_assets: float, total_liabilities: float, preferred_stock: float = 0) -> float:
    """
    Book Value
    Formula: Total Assets - Total Liabilities - Preferred Stock
    """
    return total_assets - total_liabilities - preferred_stock


def book_value_per_share_market(total_equity: float, preferred_equity: float,
                                common_shares_outstanding: float) -> float:
    """
    Book Value Per Share
    Formula: (Total Equity - Preferred Equity) / Common Shares Outstanding
    """
    if common_shares_outstanding == 0:
        raise ValueError("Common Shares Outstanding cannot be zero")
    return (total_equity - preferred_equity) / common_shares_outstanding


def market_value(current_market_price: float, number_of_units: float) -> float:
    """
    Market Value
    Formula: Current Market Price × Number of Units
    """
    return current_market_price * number_of_units


def market_share(company_sales: float, total_industry_sales: float) -> float:
    """
    Market Share (%)
    Formula: (Company's Sales / Total Industry Sales) × 100
    """
    if total_industry_sales == 0:
        raise ValueError("Total Industry Sales cannot be zero")
    return (company_sales / total_industry_sales) * 100


def total_addressable_market(annual_market_demand: float, average_selling_price: float) -> float:
    """
    Total Addressable Market (TAM)
    Formula: Annual Market Demand × Average Selling Price
    """
    return annual_market_demand * average_selling_price


def float_shares(shares_outstanding: float, restricted_shares: float,
                insider_holdings: float) -> float:
    """
    Float
    Formula: Shares Outstanding - Restricted Shares - Insider Holdings
    """
    return shares_outstanding - restricted_shares - insider_holdings


def shares_outstanding(issued_shares: float, treasury_shares: float) -> float:
    """
    Shares Outstanding
    Formula: Issued Shares - Treasury Shares
    """
    return issued_shares - treasury_shares


def shares_outstanding_from_capital(paid_up_equity_share_capital: float,
                                   face_value_per_share: float) -> float:
    """
    Shares Outstanding (Alternative - from Capital Structure)
    Formula: Paid-Up Equity Share Capital / Face Value Per Share
    """
    if face_value_per_share == 0:
        raise ValueError("Face Value Per Share cannot be zero")
    return paid_up_equity_share_capital / face_value_per_share


def institutional_ownership_percentage(shares_held_by_institutions: float,
                                      total_shares_outstanding: float) -> float:
    """
    Institutional Ownership Percentage (%)
    Formula: (Shares Held by Institutions / Total Shares Outstanding) × 100
    """
    if total_shares_outstanding == 0:
        raise ValueError("Total Shares Outstanding cannot be zero")
    return (shares_held_by_institutions / total_shares_outstanding) * 100


# ============================================================================
# 9. DIVIDEND METRICS
# ============================================================================

def dividend_yield(annual_dividends_per_share: float, current_stock_price: float) -> float:
    """
    Dividend Yield (%)
    Formula: (Annual Dividends Per Share / Current Stock Price) × 100
    """
    if current_stock_price == 0:
        raise ValueError("Current Stock Price cannot be zero")
    return (annual_dividends_per_share / current_stock_price) * 100


def dividend_payout_ratio(dividends_per_share: float, eps: float) -> float:
    """
    Dividend Payout Ratio (%)
    Formula: (Dividends Per Share / Earnings Per Share) × 100
    """
    if eps == 0:
        raise ValueError("EPS cannot be zero")
    return (dividends_per_share / eps) * 100


def dividend_payout_ratio_alt(total_dividends: float, net_income: float) -> float:
    """
    Dividend Payout Ratio (Alternative)
    Formula: (Total Dividends / Net Income) × 100
    """
    if net_income == 0:
        raise ValueError("Net Income cannot be zero")
    return (total_dividends / net_income) * 100


def dividend_coverage_ratio(eps: float, dividends_per_share: float) -> float:
    """
    Dividend Coverage Ratio
    Formula: Earnings Per Share / Dividends Per Share
    """
    if dividends_per_share == 0:
        raise ValueError("Dividends Per Share cannot be zero")
    return eps / dividends_per_share


def dividend_coverage_ratio_alt(net_income: float, total_dividends_paid: float) -> float:
    """
    Dividend Coverage Ratio (Alternative)
    Formula: Net Income / Total Dividends Paid
    """
    if total_dividends_paid == 0:
        raise ValueError("Total Dividends Paid cannot be zero")
    return net_income / total_dividends_paid


def dividend_per_share(total_dividends_paid: float, number_of_shares_outstanding: float) -> float:
    """
    Dividend Per Share (DPS)
    Formula: Total Dividends Paid / Number of Shares Outstanding
    """
    if number_of_shares_outstanding == 0:
        raise ValueError("Number of Shares Outstanding cannot be zero")
    return total_dividends_paid / number_of_shares_outstanding


def retention_ratio_from_dividend_payout(dividend_payout_ratio: float) -> float:
    """
    Retention Ratio (Plowback Ratio)
    Formula: 1 - Dividend Payout Ratio
    """
    return 1 - dividend_payout_ratio


def retention_ratio_from_income(net_income: float, dividends: float) -> float:
    """
    Retention Ratio (Alternative)
    Formula: (Net Income - Dividends) / Net Income
    """
    if net_income == 0:
        raise ValueError("Net Income cannot be zero")
    return (net_income - dividends) / net_income


def cash_dividend_payout_ratio(cash_dividends_paid: float, operating_cash_flow: float) -> float:
    """
    Cash Dividend Payout Ratio
    Formula: Cash Dividends Paid / Operating Cash Flow
    """
    if operating_cash_flow == 0:
        raise ValueError("Operating Cash Flow cannot be zero")
    return cash_dividends_paid / operating_cash_flow


# ============================================================================
# 10. DUPONT ANALYSIS COMPONENTS
# ============================================================================

def dupont_roe_3_step(net_profit_margin: float, asset_turnover: float,
                     equity_multiplier: float) -> float:
    """
    3-Step DuPont Formula
    ROE = Net Profit Margin × Asset Turnover × Equity Multiplier
    """
    return net_profit_margin * asset_turnover * equity_multiplier


def dupont_roe_3_step_detailed(net_income: float, revenue: float, total_assets: float,
                               equity: float) -> float:
    """
    3-Step DuPont Formula (Detailed)
    ROE = (Net Income / Revenue) × (Revenue / Total Assets) × (Total Assets / Equity)
    """
    if revenue == 0 or total_assets == 0 or equity == 0:
        raise ValueError("Revenue, Total Assets, or Equity cannot be zero")
    return (net_income / revenue) * (revenue / total_assets) * (total_assets / equity)


def dupont_roe_5_step(tax_burden: float, interest_burden: float, ebit_margin: float,
                     asset_turnover: float, equity_multiplier: float) -> float:
    """
    5-Step DuPont Formula
    ROE = Tax Burden × Interest Burden × EBIT Margin × Asset Turnover × Equity Multiplier
    """
    return tax_burden * interest_burden * ebit_margin * asset_turnover * equity_multiplier


def tax_burden(net_income: float, pretax_income: float) -> float:
    """
    Tax Burden (5-Step DuPont)
    Formula: Net Income / Pretax Income
    """
    if pretax_income == 0:
        raise ValueError("Pretax Income cannot be zero")
    return net_income / pretax_income


def interest_burden(pretax_income: float, ebit: float) -> float:
    """
    Interest Burden (5-Step DuPont)
    Formula: Pretax Income / EBIT
    """
    if ebit == 0:
        raise ValueError("EBIT cannot be zero")
    return pretax_income / ebit


def ebit_margin(ebit: float, revenue: float) -> float:
    """
    EBIT Margin (5-Step DuPont)
    Formula: EBIT / Revenue
    """
    if revenue == 0:
        raise ValueError("Revenue cannot be zero")
    return ebit / revenue


def dupont_asset_turnover(revenue: float, total_assets: float) -> float:
    """
    Asset Turnover (DuPont)
    Formula: Revenue / Total Assets
    """
    if total_assets == 0:
        raise ValueError("Total Assets cannot be zero")
    return revenue / total_assets


def dupont_equity_multiplier(total_assets: float, shareholders_equity: float) -> float:
    """
    Equity Multiplier (DuPont)
    Formula: Total Assets / Shareholders' Equity
    """
    if shareholders_equity == 0:
        raise ValueError("Shareholders' Equity cannot be zero")
    return total_assets / shareholders_equity


# ============================================================================
# 11. STATISTICAL METRICS
# ============================================================================

def sample_variance(data: List[float]) -> float:
    """
    Sample Variance (s²)
    Formula: Σ(xi - x̄)² / (n - 1)
    """
    if len(data) < 2:
        raise ValueError("Need at least 2 data points for sample variance")
    mean = sum(data) / len(data)
    sum_squared_diff = sum((x - mean) ** 2 for x in data)
    return sum_squared_diff / (len(data) - 1)


def population_variance(data: List[float]) -> float:
    """
    Population Variance (σ²)
    Formula: Σ(xi - μ)² / N
    """
    if len(data) == 0:
        raise ValueError("Data cannot be empty")
    mean = sum(data) / len(data)
    sum_squared_diff = sum((x - mean) ** 2 for x in data)
    return sum_squared_diff / len(data)


def portfolio_variance_two_assets(weight1: float, variance1: float, weight2: float,
                                  variance2: float, covariance: float) -> float:
    """
    Portfolio Variance (Two Assets)
    Formula: w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov(1,2)
    """
    return (weight1 ** 2 * variance1) + (weight2 ** 2 * variance2) + (2 * weight1 * weight2 * covariance)


def sample_standard_deviation(data: List[float]) -> float:
    """
    Sample Standard Deviation (s)
    Formula: √[Σ(xi - x̄)² / (n - 1)]
    """
    return math.sqrt(sample_variance(data))


def population_standard_deviation(data: List[float]) -> float:
    """
    Population Standard Deviation (σ)
    Formula: √[Σ(xi - μ)² / N]
    """
    return math.sqrt(population_variance(data))


def returns_standard_deviation(returns: List[float]) -> float:
    """
    Returns Standard Deviation (Volatility)
    Formula: √[Σ(Ri - R̄)² / (n - 1)]
    """
    return sample_standard_deviation(returns)


def sample_covariance(x: List[float], y: List[float]) -> float:
    """
    Sample Covariance
    Formula: Cov(X,Y) = Σ[(xi - x̄)(yi - ȳ)] / (n - 1)
    """
    if len(x) != len(y):
        raise ValueError("X and Y must have the same length")
    if len(x) < 2:
        raise ValueError("Need at least 2 data points")
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    sum_product = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    return sum_product / (len(x) - 1)


def population_covariance(x: List[float], y: List[float]) -> float:
    """
    Population Covariance
    Formula: Cov(X,Y) = Σ[(xi - μx)(yi - μy)] / N
    """
    if len(x) != len(y):
        raise ValueError("X and Y must have the same length")
    if len(x) == 0:
        raise ValueError("Data cannot be empty")
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    sum_product = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    return sum_product / len(x)


def correlation_coefficient(x: List[float], y: List[float]) -> float:
    """
    Correlation Coefficient (Pearson's r)
    Formula: r = Cov(X,Y) / (σx × σy)
    """
    if len(x) != len(y):
        raise ValueError("X and Y must have the same length")
    cov = sample_covariance(x, y)
    std_x = sample_standard_deviation(x)
    std_y = sample_standard_deviation(y)
    if std_x == 0 or std_y == 0:
        raise ValueError("Standard deviation cannot be zero")
    return cov / (std_x * std_y)


def coefficient_of_variation(standard_deviation: float, mean: float) -> float:
    """
    Coefficient of Variation (CV) (%)
    Formula: (Standard Deviation / Mean) × 100
    """
    if mean == 0:
        raise ValueError("Mean cannot be zero")
    return (standard_deviation / mean) * 100


def beta(covariance_ri_rm: float, variance_rm: float) -> float:
    """
    Beta (Systematic Risk)
    Formula: β = Cov(Ri, Rm) / Var(Rm)
    """
    if variance_rm == 0:
        raise ValueError("Market variance cannot be zero")
    return covariance_ri_rm / variance_rm


def beta_alt(correlation: float, sigma_i: float, sigma_m: float) -> float:
    """
    Beta (Alternative)
    Formula: β = (Correlation × σi) / σm
    """
    if sigma_m == 0:
        raise ValueError("Market standard deviation cannot be zero")
    return (correlation * sigma_i) / sigma_m


def sharpe_ratio(portfolio_return: float, risk_free_rate: float,
                portfolio_std_dev: float) -> float:
    """
    Sharpe Ratio
    Formula: (Rp - Rf) / σp
    """
    if portfolio_std_dev == 0:
        raise ValueError("Portfolio standard deviation cannot be zero")
    return (portfolio_return - risk_free_rate) / portfolio_std_dev


def treynor_ratio(portfolio_return: float, risk_free_rate: float, portfolio_beta: float) -> float:
    """
    Treynor Ratio
    Formula: (Rp - Rf) / βp
    """
    if portfolio_beta == 0:
        raise ValueError("Portfolio beta cannot be zero")
    return (portfolio_return - risk_free_rate) / portfolio_beta


def information_ratio(portfolio_return: float, benchmark_return: float,
                     tracking_error: float) -> float:
    """
    Information Ratio
    Formula: (Rp - Rb) / Tracking Error
    """
    if tracking_error == 0:
        raise ValueError("Tracking Error cannot be zero")
    return (portfolio_return - benchmark_return) / tracking_error


def downside_deviation(returns: List[float], mar: float = 0.0) -> float:
    """
    Downside Deviation
    Formula: √[Σ(min(Ri - MAR, 0))² / n]
    """
    if len(returns) == 0:
        raise ValueError("Returns list cannot be empty")
    downside_squared = sum(min(0, r - mar) ** 2 for r in returns)
    return math.sqrt(downside_squared / len(returns))


def sortino_ratio(portfolio_return: float, risk_free_rate: float,
                 downside_dev: float) -> float:
    """
    Sortino Ratio
    Formula: (Rp - Rf) / Downside Deviation
    """
    if downside_dev == 0:
        raise ValueError("Downside Deviation cannot be zero")
    return (portfolio_return - risk_free_rate) / downside_dev


def value_at_risk(portfolio_value: float, z_score: float, std_dev: float,
                 time_horizon: float) -> float:
    """
    Parametric VaR (Normal Distribution)
    Formula: VaR = Portfolio Value × z-score × σ × √t
    """
    return portfolio_value * z_score * std_dev * math.sqrt(time_horizon)


def arithmetic_mean(data: List[float]) -> float:
    """
    Arithmetic Mean
    Formula: x̄ = Σxi / n
    """
    if len(data) == 0:
        raise ValueError("Data cannot be empty")
    return sum(data) / len(data)


def weighted_average(values: List[float], weights: List[float]) -> float:
    """
    Weighted Average
    Formula: x̄w = Σ(wi × xi) / Σwi
    """
    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length")
    if len(values) == 0:
        raise ValueError("Data cannot be empty")
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero")
    return weighted_sum / total_weight


def geometric_mean(returns: List[float]) -> float:
    """
    Geometric Mean (for returns)
    Formula: [(1 + R₁) × (1 + R₂) × ... × (1 + Rn)]^(1/n) - 1
    """
    if len(returns) == 0:
        raise ValueError("Returns list cannot be empty")
    product = 1.0
    for r in returns:
        product *= (1 + r)
    return (product ** (1 / len(returns))) - 1


# ============================================================================
# 12. DCF VALUATION FRAMEWORK
# ============================================================================

def wacc(equity_value: float, debt_value: float, cost_of_equity: float,
         cost_of_debt: float, tax_rate: float, preferred_value: float = 0,
         cost_of_preferred: float = 0) -> float:
    """
    Weighted Average Cost of Capital (WACC)
    Formula: (E/V × Re) + (D/V × Rd × (1 - Tc)) + (P/V × Rp)
    """
    total_value = equity_value + debt_value + preferred_value
    if total_value == 0:
        raise ValueError("Total firm value cannot be zero")
    equity_weight = equity_value / total_value
    debt_weight = debt_value / total_value
    preferred_weight = preferred_value / total_value if preferred_value > 0 else 0
    
    wacc_value = (equity_weight * cost_of_equity) + \
                 (debt_weight * cost_of_debt * (1 - tax_rate))
    
    if preferred_value > 0:
        wacc_value += (preferred_weight * cost_of_preferred)
    
    return wacc_value


def cost_of_equity_capm(risk_free_rate: float, beta: float, market_return: float) -> float:
    """
    Cost of Equity (CAPM)
    Formula: Re = Rf + β × (Rm - Rf)
    """
    return risk_free_rate + beta * (market_return - risk_free_rate)


def terminal_value_gordon_growth(fcf_next_year: float, wacc: float, growth_rate: float) -> float:
    """
    Terminal Value (Gordon Growth Model)
    Formula: TV = FCFFn+1 / (WACC - g)
    """
    if wacc <= growth_rate:
        raise ValueError("WACC must be greater than growth rate")
    return fcf_next_year / (wacc - growth_rate)


def terminal_value_exit_multiple_ebitda(exit_multiple: float, ebitda_n: float) -> float:
    """
    Terminal Value (Exit Multiple - EBITDA)
    Formula: TV = Exit Multiple × EBITDAn
    """
    return exit_multiple * ebitda_n


def terminal_value_exit_multiple_ebit(exit_multiple: float, ebit_n: float) -> float:
    """
    Terminal Value (Exit Multiple - EBIT)
    Formula: TV = Exit Multiple × EBITn
    """
    return exit_multiple * ebit_n


def terminal_value_exit_multiple_sales(exit_multiple: float, sales_n: float) -> float:
    """
    Terminal Value (Exit Multiple - Sales)
    Formula: TV = Exit Multiple × Salesn
    """
    return exit_multiple * sales_n


def present_value_cash_flow(cash_flow: float, discount_rate: float, period: int) -> float:
    """
    Present Value of Cash Flow
    Formula: CF / (1 + r)^t
    """
    return cash_flow / ((1 + discount_rate) ** period)


def present_value_cash_flows(cash_flows: List[float], discount_rate: float) -> float:
    """
    Present Value of Multiple Cash Flows
    Formula: Σ[CFt / (1 + r)^t]
    """
    pv = 0.0
    for i, cf in enumerate(cash_flows, start=1):
        pv += present_value_cash_flow(cf, discount_rate, i)
    return pv


def enterprise_value_dcf(pv_fcff: float, pv_terminal_value: float) -> float:
    """
    Enterprise Value from DCF
    Formula: PV of FCFF during projection period + PV of Terminal Value
    """
    return pv_fcff + pv_terminal_value


def equity_value_from_ev(enterprise_value: float, net_debt: float,
                        preferred_stock: float = 0, non_operating_assets: float = 0) -> float:
    """
    Equity Value from Enterprise Value
    Formula: Enterprise Value - Net Debt - Preferred Stock + Non-Operating Assets
    """
    return enterprise_value - net_debt - preferred_stock + non_operating_assets


def fair_value_per_share(equity_value: float, shares_outstanding: float) -> float:
    """
    Fair Value Per Share
    Formula: Equity Value / Shares Outstanding
    """
    if shares_outstanding == 0:
        raise ValueError("Shares Outstanding cannot be zero")
    return equity_value / shares_outstanding


def fcfe_from_fcff(fcff: float, interest_expense: float, tax_rate: float,
                   net_borrowing: float) -> float:
    """
    FCFE from FCFF
    Formula: FCFE = FCFF - Interest(1-T) + Net Borrowing
    """
    return fcff - (interest_expense * (1 - tax_rate)) + net_borrowing


def fcfe_terminal_value(fcfe_next_year: float, cost_of_equity: float,
                       growth_rate: float) -> float:
    """
    Terminal Value for FCFE
    Formula: TV = FCFEn+1 / (Re - g)
    """
    if cost_of_equity <= growth_rate:
        raise ValueError("Cost of Equity must be greater than growth rate")
    return fcfe_next_year / (cost_of_equity - growth_rate)


def gordon_growth_model(dividend_next_year: float, cost_of_equity: float,
                       growth_rate: float) -> float:
    """
    Gordon Growth Model (Constant Growth DDM)
    Formula: P₀ = D₁ / (Re - g)
    """
    if cost_of_equity <= growth_rate:
        raise ValueError("Cost of Equity must be greater than growth rate")
    return dividend_next_year / (cost_of_equity - growth_rate)


def dividend_next_year(current_dividend: float, growth_rate: float) -> float:
    """
    Expected Dividend Next Year
    Formula: D₁ = D₀(1 + g)
    """
    return current_dividend * (1 + growth_rate)


def apv_unlevered_firm_value(fcff_flows: List[float], unlevered_cost: float,
                             terminal_value: float, n_periods: int) -> float:
    """
    Unlevered Firm Value (APV)
    Formula: VU = Σ[FCFF/(1+Ru)^t] + TV/(1+Ru)^n
    """
    pv_flows = present_value_cash_flows(fcff_flows, unlevered_cost)
    pv_tv = terminal_value / ((1 + unlevered_cost) ** n_periods)
    return pv_flows + pv_tv


def unlevered_cost_of_equity(risk_free_rate: float, unlevered_beta: float,
                            equity_risk_premium: float) -> float:
    """
    Unlevered Cost of Equity
    Formula: Ru = Rf + βU × ERP
    """
    return risk_free_rate + unlevered_beta * equity_risk_premium


def pv_tax_shield_perpetual(debt: float, tax_rate: float) -> float:
    """
    Present Value of Tax Shield (Perpetual Debt)
    Formula: PV(Tax Shield) = Tax Rate × Debt
    """
    return tax_rate * debt


def pv_tax_shield_changing(interest_payments: List[float], tax_rate: float,
                          cost_of_debt: float) -> float:
    """
    Present Value of Tax Shield (Changing Debt)
    Formula: PV(Tax Shield) = Σ[Interest × Tax Rate / (1+Rd)^t]
    """
    pv = 0.0
    for i, interest in enumerate(interest_payments, start=1):
        pv += (interest * tax_rate) / ((1 + cost_of_debt) ** i)
    return pv


def adjusted_present_value(unlevered_value: float, pv_tax_shield: float,
                           pv_bankruptcy_costs: float = 0) -> float:
    """
    Adjusted Present Value (APV)
    Formula: APV = VU + PV(Tax Shield) - PV(Bankruptcy Costs)
    """
    return unlevered_value + pv_tax_shield - pv_bankruptcy_costs


# ============================================================================
# 13. OTHER KEY METRICS
# ============================================================================

def economic_value_added(nopat: float, wacc: float, invested_capital: float) -> float:
    """
    Economic Value Added (EVA)
    Formula: NOPAT - (WACC × Invested Capital)
    """
    return nopat - (wacc * invested_capital)


def eva_alt(roic: float, wacc: float, invested_capital: float) -> float:
    """
    Economic Value Added (Alternative)
    Formula: (ROIC - WACC) × Invested Capital
    """
    return (roic - wacc) * invested_capital


def market_value_added(market_value_firm: float, invested_capital: float) -> float:
    """
    Market Value Added (MVA)
    Formula: Market Value of Firm - Invested Capital
    """
    return market_value_firm - invested_capital


def mva_alt(market_capitalization: float, book_value_equity: float) -> float:
    """
    Market Value Added (Alternative)
    Formula: Market Capitalization - Book Value of Equity
    """
    return market_capitalization - book_value_equity


def shareholder_value_added(return_on_investment: float, cost_of_capital: float,
                           invested_capital: float) -> float:
    """
    Shareholder Value Added (SVA)
    Formula: (Return on Investment - Cost of Capital) × Invested Capital
    """
    return (return_on_investment - cost_of_capital) * invested_capital


def altman_z_score(working_capital: float, total_assets: float, retained_earnings: float,
                   ebit: float, market_value_equity: float, book_value_liabilities: float,
                   sales: float) -> float:
    """
    Altman Z-Score (Bankruptcy Prediction) - Public Manufacturing
    Formula: Z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E
    """
    A = working_capital / total_assets
    B = retained_earnings / total_assets
    C = ebit / total_assets
    D = market_value_equity / book_value_liabilities
    E = sales / total_assets
    
    return 1.2 * A + 1.4 * B + 3.3 * C + 0.6 * D + 1.0 * E


def altman_z_score_private(working_capital: float, total_assets: float,
                          retained_earnings: float, ebit: float,
                          book_value_equity: float, total_liabilities: float,
                          sales: float) -> float:
    """
    Altman Z-Score for Private Companies
    Formula: Z' = 0.717A + 0.847B + 3.107C + 0.420D + 0.998E
    """
    A = working_capital / total_assets
    B = retained_earnings / total_assets
    C = ebit / total_assets
    D = book_value_equity / total_liabilities
    E = sales / total_assets
    
    return 0.717 * A + 0.847 * B + 3.107 * C + 0.420 * D + 0.998 * E


def piotroski_f_score(roa_current: float, operating_cf_current: float,
                     roa_previous: float, operating_cf_previous: float,
                     net_income_current: float, long_term_debt_current: float,
                     long_term_debt_previous: float, current_ratio_current: float,
                     current_ratio_previous: float, shares_current: float,
                     shares_previous: float, gross_margin_current: float,
                     gross_margin_previous: float, asset_turnover_current: float,
                     asset_turnover_previous: float) -> int:
    """
    Piotroski F-Score (Quality Assessment)
    Score range: 0-9 (sum of nine binary scores)
    """
    score = 0
    
    # Profitability (4 points)
    if roa_current > 0:
        score += 1
    if operating_cf_current > 0:
        score += 1
    if roa_current > roa_previous:
        score += 1
    if operating_cf_current > net_income_current:
        score += 1
    
    # Leverage, Liquidity, Source of Funds (3 points)
    if long_term_debt_current < long_term_debt_previous:
        score += 1
    if current_ratio_current > current_ratio_previous:
        score += 1
    if shares_current <= shares_previous:
        score += 1
    
    # Operating Efficiency (2 points)
    if gross_margin_current > gross_margin_previous:
        score += 1
    if asset_turnover_current > asset_turnover_previous:
        score += 1
    
    return score


def beneish_m_score(dsri: float, gmi: float, aqi: float, sgi: float, depi: float,
                    sgai: float, tata: float, lvgi: float) -> float:
    """
    Beneish M-Score (Earnings Manipulation Detection)
    Formula: M = -4.84 + 0.92×DSRI + 0.528×GMI + 0.404×AQI + 0.892×SGI + 0.115×DEPI 
             - 0.172×SGAI + 4.679×TATA - 0.327×LVGI
    """
    return (-4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi +
            0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)


def jensens_alpha(actual_return: float, risk_free_rate: float, beta: float,
                  market_return: float) -> float:
    """
    Alpha (Jensen's Alpha)
    Formula: αi = Ri - [Rf + βi(Rm - Rf)]
    """
    expected_return = risk_free_rate + beta * (market_return - risk_free_rate)
    return actual_return - expected_return


def tobins_q_ratio(market_value_firm: float, replacement_cost_assets: float) -> float:
    """
    Tobin's Q Ratio
    Formula: Market Value of Firm / Replacement Cost of Assets
    """
    if replacement_cost_assets == 0:
        raise ValueError("Replacement Cost of Assets cannot be zero")
    return market_value_firm / replacement_cost_assets


def tobins_q_ratio_alt(market_cap: float, total_debt: float, total_assets: float) -> float:
    """
    Tobin's Q Ratio (Alternative)
    Formula: (Market Cap + Total Debt) / Total Assets
    """
    if total_assets == 0:
        raise ValueError("Total Assets cannot be zero")
    return (market_cap + total_debt) / total_assets


def earnings_quality_ratio(operating_cash_flow: float, net_income: float) -> float:
    """
    Earnings Quality Ratio
    Formula: Operating Cash Flow / Net Income
    """
    if net_income == 0:
        raise ValueError("Net Income cannot be zero")
    return operating_cash_flow / net_income


def accruals_ratio(net_income: float, operating_cash_flow: float, total_assets: float) -> float:
    """
    Accruals Ratio
    Formula: (Net Income - Operating Cash Flow) / Total Assets
    """
    if total_assets == 0:
        raise ValueError("Total Assets cannot be zero")
    return (net_income - operating_cash_flow) / total_assets


# ============================================================================
# 14. ASWATH DAMODARAN VALUATION FORMULAS
# ============================================================================

def cost_of_equity_build_up(risk_free_rate: float, equity_risk_premium: float,
                            size_premium: float = 0, industry_risk_premium: float = 0,
                            company_specific_risk: float = 0) -> float:
    """
    Cost of Equity (Build-Up Method)
    Formula: Re = Rf + Equity Risk Premium + Size Premium + Industry Risk Premium + Company-Specific Risk
    """
    return (risk_free_rate + equity_risk_premium + size_premium +
            industry_risk_premium + company_specific_risk)


def cost_of_debt(interest_expense: float, average_debt_outstanding: float) -> float:
    """
    Cost of Debt
    Formula: Rd = Interest Expense / Average Debt Outstanding
    """
    if average_debt_outstanding == 0:
        raise ValueError("Average Debt Outstanding cannot be zero")
    return interest_expense / average_debt_outstanding


def after_tax_cost_of_debt(cost_of_debt: float, tax_rate: float) -> float:
    """
    After-Tax Cost of Debt
    Formula: Rd(after-tax) = Rd × (1 - Tax Rate)
    """
    return cost_of_debt * (1 - tax_rate)


def levered_beta(unlevered_beta: float, tax_rate: float, debt_to_equity: float) -> float:
    """
    Levered Beta (Adding Financial Leverage)
    Formula: βL = βU × [1 + (1 - T) × (D/E)]
    """
    return unlevered_beta * (1 + (1 - tax_rate) * debt_to_equity)


def unlevered_beta(levered_beta: float, tax_rate: float, debt_to_equity: float) -> float:
    """
    Unlevered Beta (Removing Financial Leverage)
    Formula: βU = βL / [1 + (1 - T) × (D/E)]
    """
    denominator = 1 + (1 - tax_rate) * debt_to_equity
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    return levered_beta / denominator


def adjusted_beta_bloomberg(raw_beta: float) -> float:
    """
    Adjusted Beta (Bloomberg Method)
    Formula: Adjusted β = (0.67 × Raw β) + (0.33 × 1.0)
    """
    return (0.67 * raw_beta) + 0.33


def bottom_up_beta(business_segment_weights: List[float], unlevered_betas: List[float],
                   tax_rate: float, debt_to_equity: float) -> float:
    """
    Bottom-Up Beta
    Formula: βFirm = Σ(Business Segment Weightᵢ × βUnlevered,i) × [1 + (1-T) × (D/E)]
    """
    if len(business_segment_weights) != len(unlevered_betas):
        raise ValueError("Weights and betas must have the same length")
    
    weighted_beta = sum(w * b for w, b in zip(business_segment_weights, unlevered_betas))
    return weighted_beta * (1 + (1 - tax_rate) * debt_to_equity)


def country_risk_premium(country_default_spread: float, sigma_equity_country: float,
                        sigma_bond_country: float) -> float:
    """
    Country Risk Premium (Relative Volatility Method)
    Formula: CRP = Country Default Spread × (σEquity,Country / σBond,Country)
    """
    if sigma_bond_country == 0:
        raise ValueError("Bond volatility cannot be zero")
    return country_default_spread * (sigma_equity_country / sigma_bond_country)


def cost_of_equity_with_country_risk(risk_free_rate: float, beta: float,
                                     mature_market_erp: float,
                                     country_risk_premium: float) -> float:
    """
    Total Cost of Equity (with Country Risk)
    Formula: Re = Rf + β × Mature Market ERP + Country Risk Premium
    """
    return risk_free_rate + beta * mature_market_erp + country_risk_premium


def fundamental_growth_rate_equity(roe: float, retention_ratio: float) -> float:
    """
    Fundamental Growth Rate (Equity Perspective)
    Formula: g = ROE × Retention Ratio
    """
    return roe * retention_ratio


def fundamental_growth_rate_firm(return_on_capital: float, reinvestment_rate: float) -> float:
    """
    Fundamental Growth Rate (Firm Perspective)
    Formula: g = Return on Capital × Reinvestment Rate
    """
    return return_on_capital * reinvestment_rate


def expected_growth_rate_historical(ending_value: float, beginning_value: float,
                                   n_periods: float) -> float:
    """
    Expected Growth Rate (Historical)
    Formula: g = (Ending Value / Beginning Value)^(1/n) - 1
    """
    if beginning_value == 0:
        raise ValueError("Beginning Value cannot be zero")
    if n_periods == 0:
        raise ValueError("Number of periods cannot be zero")
    return ((ending_value / beginning_value) ** (1 / n_periods)) - 1


def reinvestment_rate(capex: float, depreciation: float, change_in_wc: float,
                     ebit: float, tax_rate: float) -> float:
    """
    Reinvestment Rate
    Formula: (CapEx - Depreciation + ΔWC) / EBIT(1-T)
    """
    numerator = capex - depreciation + change_in_wc
    denominator = ebit * (1 - tax_rate)
    if denominator == 0:
        raise ValueError("EBIT(1-T) cannot be zero")
    return numerator / denominator


def reinvestment_rate_alt(net_capex: float, change_in_wc: float, nopat: float) -> float:
    """
    Reinvestment Rate (Alternative)
    Formula: (Net CapEx + ΔWC) / NOPAT
    """
    if nopat == 0:
        raise ValueError("NOPAT cannot be zero")
    return (net_capex + change_in_wc) / nopat


def stable_period_fcff(ebit: float, tax_rate: float, reinvestment_rate: float) -> float:
    """
    Stable Period FCFF
    Formula: FCFF (stable) = EBIT(1-T) × (1 - Reinvestment Rate)
    """
    return (ebit * (1 - tax_rate)) * (1 - reinvestment_rate)


def justified_pe_stable_growth(payout_ratio: float, growth_rate: float,
                               cost_of_equity: float) -> float:
    """
    Justified P/E (Stable Growth)
    Formula: P/E = Payout Ratio × (1 + g) / (Re - g)
    """
    if cost_of_equity <= growth_rate:
        raise ValueError("Cost of Equity must be greater than growth rate")
    return (payout_ratio * (1 + growth_rate)) / (cost_of_equity - growth_rate)


def justified_pb_ratio(roe: float, growth_rate: float, cost_of_equity: float) -> float:
    """
    Justified P/B Ratio
    Formula: P/B = (ROE - g) / (Re - g)
    """
    if cost_of_equity <= growth_rate:
        raise ValueError("Cost of Equity must be greater than growth rate")
    return (roe - growth_rate) / (cost_of_equity - growth_rate)


def justified_ps_ratio(profit_margin: float, payout_ratio: float, growth_rate: float,
                      cost_of_equity: float) -> float:
    """
    Justified P/S Ratio
    Formula: P/S = [Profit Margin × Payout Ratio × (1+g)] / (Re - g)
    """
    if cost_of_equity <= growth_rate:
        raise ValueError("Cost of Equity must be greater than growth rate")
    return (profit_margin * payout_ratio * (1 + growth_rate)) / (cost_of_equity - growth_rate)


def justified_ev_ebitda(tax_rate: float, reinvestment_rate: float, growth_rate: float,
                       wacc: float) -> float:
    """
    Justified EV/EBITDA
    Formula: EV/EBITDA = [(1-T) × (1 - Reinvestment Rate) × (1+g)] / (WACC - g)
    """
    if wacc <= growth_rate:
        raise ValueError("WACC must be greater than growth rate")
    return ((1 - tax_rate) * (1 - reinvestment_rate) * (1 + growth_rate)) / (wacc - growth_rate)


def justified_ev_sales(operating_margin: float, tax_rate: float, reinvestment_rate: float,
                       growth_rate: float, wacc: float) -> float:
    """
    Justified EV/Sales
    Formula: EV/Sales = [Operating Margin × (1-T) × (1 - Reinvestment Rate) × (1+g)] / (WACC - g)
    """
    if wacc <= growth_rate:
        raise ValueError("WACC must be greater than growth rate")
    return ((operating_margin * (1 - tax_rate) * (1 - reinvestment_rate) * (1 + growth_rate)) /
            (wacc - growth_rate))


def peg_ratio_damodaran(pe_ratio: float, expected_growth_rate: float) -> float:
    """
    PEG Ratio (Damodaran Version)
    Formula: PEG = P/E / Expected Growth Rate
    """
    if expected_growth_rate == 0:
        raise ValueError("Expected Growth Rate cannot be zero")
    return pe_ratio / expected_growth_rate


def firm_value_eva(invested_capital: float, pv_expected_eva: float) -> float:
    """
    Value of Firm (EVA Model)
    Formula: Firm Value = Invested Capital + PV of Expected EVA
    """
    return invested_capital + pv_expected_eva


def _norm_cdf(x: float) -> float:
    """Cumulative distribution function of standard normal distribution"""
    if not SCIPY_AVAILABLE:
        # Approximation using error function
        return 0.5 * (1 + math.erf(x / math.sqrt(2)))
    return stats.norm.cdf(x)


def black_scholes_call(s0: float, k: float, r: float, t: float, sigma: float) -> float:
    """
    Black-Scholes Call Option Value
    Formula: C = S₀N(d₁) - Ke^(-rT)N(d₂)
    Requires scipy for accurate results, but will use approximation if not available.
    """
    d1 = (math.log(s0 / k) + (r + (sigma ** 2) / 2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    
    n_d1 = _norm_cdf(d1)
    n_d2 = _norm_cdf(d2)
    
    return s0 * n_d1 - k * math.exp(-r * t) * n_d2


def black_scholes_put(s0: float, k: float, r: float, t: float, sigma: float) -> float:
    """
    Black-Scholes Put Option Value
    Formula: P = Ke^(-rT)N(-d₂) - S₀N(-d₁)
    Requires scipy for accurate results, but will use approximation if not available.
    """
    d1 = (math.log(s0 / k) + (r + (sigma ** 2) / 2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    
    n_neg_d1 = _norm_cdf(-d1)
    n_neg_d2 = _norm_cdf(-d2)
    
    return k * math.exp(-r * t) * n_neg_d2 - s0 * n_neg_d1


# ============================================================================
# 15. BENJAMIN GRAHAM FORMULAS
# ============================================================================

def graham_number(eps: float, bvps: float) -> float:
    """
    Graham Number (Maximum Fair Value)
    Formula: √(22.5 × EPS × BVPS)
    """
    return math.sqrt(22.5 * eps * bvps)


def graham_intrinsic_value_original(eps: float, growth_rate: float) -> float:
    """
    Original Graham Formula (1962)
    Formula: Intrinsic Value = EPS × (8.5 + 2g)
    """
    return eps * (8.5 + 2 * growth_rate)


def graham_intrinsic_value_revised(eps: float, growth_rate: float,
                                  current_aaa_yield: float) -> float:
    """
    Revised Graham Formula (1974 - with bond yields)
    Formula: Intrinsic Value = [EPS × (8.5 + 2g) × 4.4] / Y
    """
    if current_aaa_yield == 0:
        raise ValueError("Current AAA Yield cannot be zero")
    return (eps * (8.5 + 2 * growth_rate) * 4.4) / current_aaa_yield


def ncav_per_share(current_assets: float, total_liabilities: float,
                  shares_outstanding: float) -> float:
    """
    Net Current Asset Value (NCAV) Per Share
    Formula: NCAV = (Current Assets - Total Liabilities) / Shares Outstanding
    """
    if shares_outstanding == 0:
        raise ValueError("Shares Outstanding cannot be zero")
    return (current_assets - total_liabilities) / shares_outstanding


def graham_ncav_buy_rule(stock_price: float, ncav_per_share: float) -> bool:
    """
    Graham's NCAV Buy Rule
    Buy when: Stock Price < (2/3 × NCAV)
    """
    return stock_price < (2/3 * ncav_per_share)


def graham_ncav_buy_rule_conservative(stock_price: float, ncav_per_share: float) -> bool:
    """
    Graham's NCAV Buy Rule (Conservative)
    Buy when: Price < 0.5 × NCAV
    """
    return stock_price < (0.5 * ncav_per_share)


def net_net_working_capital(current_assets: float, total_liabilities: float,
                            inventory: float) -> float:
    """
    Net-Net Working Capital
    Formula: Net-Net = (Current Assets - Total Liabilities) - (0.5 × Inventory)
    """
    return (current_assets - total_liabilities) - (0.5 * inventory)


def net_net_working_capital_per_share(net_net_wc: float, shares_outstanding: float) -> float:
    """
    Net-Net Working Capital Per Share
    Formula: Net-Net / Shares Outstanding
    """
    if shares_outstanding == 0:
        raise ValueError("Shares Outstanding cannot be zero")
    return net_net_wc / shares_outstanding


def margin_of_safety(intrinsic_value: float, market_price: float) -> float:
    """
    Margin of Safety (Percentage)
    Formula: MOS = [(Intrinsic Value - Market Price) / Intrinsic Value] × 100
    """
    if intrinsic_value == 0:
        raise ValueError("Intrinsic Value cannot be zero")
    return ((intrinsic_value - market_price) / intrinsic_value) * 100


def graham_minimum_mos_33(market_price: float, intrinsic_value: float) -> bool:
    """
    Graham's Minimum MOS (33%)
    Buy only with ≥ 33% margin of safety
    """
    return market_price <= (0.67 * intrinsic_value)


def graham_minimum_mos_50(market_price: float, intrinsic_value: float) -> bool:
    """
    Graham's Minimum MOS (50%)
    Preferred: ≥ 50% margin of safety
    """
    return market_price <= (0.50 * intrinsic_value)


def liquidation_value_per_share(current_assets: float, total_liabilities: float,
                               preferred_stock: float, common_shares: float) -> float:
    """
    Liquidation Value Per Share
    Formula: (Current Assets - Total Liabilities - Preferred Stock) / Common Shares
    """
    if common_shares == 0:
        raise ValueError("Common Shares cannot be zero")
    return (current_assets - total_liabilities - preferred_stock) / common_shares


def liquidation_value_conservative(receivables: float, inventory: float, cash: float,
                                 total_liabilities: float) -> float:
    """
    Liquidation Value (Conservative Estimate)
    Formula: (0.75 × Receivables) + (0.5 × Inventory) + Cash - Total Liabilities
    """
    return (0.75 * receivables) + (0.5 * inventory) + cash - total_liabilities


def earnings_power_value(adjusted_earnings: float, required_rate_of_return: float) -> float:
    """
    Earnings Power Value (EPV)
    Formula: EPV = Adjusted Earnings / Required Rate of Return
    """
    if required_rate_of_return == 0:
        raise ValueError("Required Rate of Return cannot be zero")
    return adjusted_earnings / required_rate_of_return


def epv_with_growth(epv: float, pv_growth: float) -> float:
    """
    Full EPV with Growth
    Formula: Value = EPV + PV(Growth)
    """
    return epv + pv_growth


def graham_working_capital_rule(net_working_capital: float, total_debt: float) -> bool:
    """
    Graham's Working Capital Rule
    For industrials: NWC should be ≥ 50% of total debt
    """
    return net_working_capital >= (0.5 * total_debt)


def central_value(assets: float, earning_power: float, multiplier: float = 12.5) -> float:
    """
    Central Value (Simplified)
    Formula: Value = Assets + (Multiplier × Earning Power)
    """
    return assets + (multiplier * earning_power)


# ============================================================================
# 16. MODERN VALUE INVESTING ADDITIONS
# ============================================================================

def look_through_earnings(reported_earnings: float, share_undistributed_earnings: float) -> float:
    """
    Look-Through Earnings
    Formula: Look-Through = Reported Earnings + Share of Undistributed Earnings from Investees
    """
    return reported_earnings + share_undistributed_earnings


def intrinsic_value_growth_rate(dividend_payout_ratio: float,
                               return_on_retained_earnings: float) -> float:
    """
    Intrinsic Value Growth Rate
    Formula: Growth Rate = (1 - Dividend Payout Ratio) × Return on Retained Earnings
    """
    return (1 - dividend_payout_ratio) * return_on_retained_earnings


def return_on_retained_earnings(change_in_eps: float,
                               cumulative_retained_earnings_per_share: float) -> float:
    """
    Return on Retained Earnings
    Formula: Return = Change in EPS / Cumulative Retained Earnings per Share
    """
    if cumulative_retained_earnings_per_share == 0:
        raise ValueError("Cumulative Retained Earnings per Share cannot be zero")
    return change_in_eps / cumulative_retained_earnings_per_share


def return_spread(roic: float, wacc: float) -> float:
    """
    Return Spread
    Formula: Return Spread = ROIC - WACC
    """
    return roic - wacc


def return_on_tangible_capital(nopat: float, net_working_capital: float,
                               net_fixed_assets: float) -> float:
    """
    Return on Tangible Capital
    Formula: ROTC = NOPAT / (Net Working Capital + Net Fixed Assets)
    """
    denominator = net_working_capital + net_fixed_assets
    if denominator == 0:
        raise ValueError("Net Working Capital + Net Fixed Assets cannot be zero")
    return nopat / denominator


def earnings_yield_greenblatt(ebit: float, enterprise_value: float) -> float:
    """
    Earnings Yield (Greenblatt's Magic Formula)
    Formula: Earnings Yield = EBIT / Enterprise Value
    """
    if enterprise_value == 0:
        raise ValueError("Enterprise Value cannot be zero")
    return ebit / enterprise_value


def return_on_capital_greenblatt(ebit: float, net_working_capital: float,
                                net_fixed_assets: float) -> float:
    """
    Return on Capital (Greenblatt's Magic Formula)
    Formula: ROC = EBIT / (Net Working Capital + Net Fixed Assets)
    """
    denominator = net_working_capital + net_fixed_assets
    if denominator == 0:
        raise ValueError("Net Working Capital + Net Fixed Assets cannot be zero")
    return ebit / denominator


def acquirers_multiple(enterprise_value: float, operating_earnings: float) -> float:
    """
    Acquirer's Multiple (Tobias Carlisle)
    Formula: Acquirer's Multiple = Enterprise Value / Operating Earnings
    """
    if operating_earnings == 0:
        raise ValueError("Operating Earnings cannot be zero")
    return enterprise_value / operating_earnings


def shareholder_yield(dividends: float, buybacks: float, share_issuance: float,
                     market_cap: float) -> float:
    """
    Shareholder Yield
    Formula: Shareholder Yield = (Dividends + Buybacks - Share Issuance) / Market Cap
    """
    if market_cap == 0:
        raise ValueError("Market Cap cannot be zero")
    return (dividends + buybacks - share_issuance) / market_cap


def net_payout_yield(dividends: float, net_buybacks: float, market_cap: float) -> float:
    """
    Net Payout Yield
    Formula: Net Payout = (Dividends + Net Buybacks) / Market Cap
    """
    if market_cap == 0:
        raise ValueError("Market Cap cannot be zero")
    return (dividends + net_buybacks) / market_cap


def total_payout_yield(dividends: float, buybacks: float, debt_reduction: float,
                      market_cap: float) -> float:
    """
    Total Payout Yield
    Formula: Total Payout = (Dividends + Buybacks + Debt Reduction) / Market Cap
    """
    if market_cap == 0:
        raise ValueError("Market Cap cannot be zero")
    return (dividends + buybacks + debt_reduction) / market_cap


def gross_profitability(revenue: float, cogs: float, total_assets: float) -> float:
    """
    Gross Profitability
    Formula: Gross Profitability = (Revenue - COGS) / Total Assets
    """
    if total_assets == 0:
        raise ValueError("Total Assets cannot be zero")
    return (revenue - cogs) / total_assets


def asset_growth(current_total_assets: float, prior_total_assets: float) -> float:
    """
    Asset Growth (Red Flag)
    Formula: Asset Growth = (Current Total Assets - Prior Total Assets) / Prior Total Assets
    """
    if prior_total_assets == 0:
        raise ValueError("Prior Total Assets cannot be zero")
    return (current_total_assets - prior_total_assets) / prior_total_assets


def accrual_ratio_quality(net_income: float, operating_cash_flow: float,
                          average_total_assets: float) -> float:
    """
    Accrual Ratio (Earnings Quality)
    Formula: Accruals = (Net Income - Operating Cash Flow) / Average Total Assets
    """
    if average_total_assets == 0:
        raise ValueError("Average Total Assets cannot be zero")
    return (net_income - operating_cash_flow) / average_total_assets


def ohlson_o_score(size: float, tlta: float, wcta: float, clca: float, oeneg: float,
                   nita: float, futl: float, intwo: float, chin: float) -> float:
    """
    Ohlson O-Score (Distress Prediction)
    Formula: O = -1.32 - 0.407×SIZE + 6.03×TLTA - 1.43×WCTA + 0.076×CLCA - 1.72×OENEG 
             - 2.37×NITA - 1.83×FUTL + 0.285×INTWO - 0.521×CHIN
    """
    return (-1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta + 0.076 * clca -
            1.72 * oeneg - 2.37 * nita - 1.83 * futl + 0.285 * intwo - 0.521 * chin)


def probability_of_bankruptcy(ohlson_o_score: float) -> float:
    """
    Probability of Bankruptcy from O-Score
    Formula: Probability = 1 / (1 + e^(-O))
    """
    return 1 / (1 + math.exp(-ohlson_o_score))


def price_momentum_12_month(current_price: float, price_12_months_ago: float) -> float:
    """
    12-Month Price Momentum
    Formula: Momentum = (Current Price / Price 12 months ago) - 1
    """
    if price_12_months_ago == 0:
        raise ValueError("Price 12 months ago cannot be zero")
    return (current_price / price_12_months_ago) - 1


def week_52_high_ratio(current_price: float, week_52_high: float) -> float:
    """
    52-Week High Ratio
    Formula: 52-Week Ratio = Current Price / 52-Week High
    """
    if week_52_high == 0:
        raise ValueError("52-Week High cannot be zero")
    return current_price / week_52_high


def short_term_reversal(current_price: float, price_1_month_ago: float) -> float:
    """
    Short-Term Reversal (Contrarian)
    Formula: 1-Month Return = (Current Price / Price 1 month ago) - 1
    """
    if price_1_month_ago == 0:
        raise ValueError("Price 1 month ago cannot be zero")
    return (current_price / price_1_month_ago) - 1


def shiller_pe(current_price: float, avg_10_year_earnings: float) -> float:
    """
    Shiller P/E (CAPE Ratio)
    Formula: CAPE = Price / 10-Year Average Inflation-Adjusted Earnings
    """
    if avg_10_year_earnings == 0:
        raise ValueError("Average 10-Year Earnings cannot be zero")
    return current_price / avg_10_year_earnings


def graham_dodd_pe(current_price: float, avg_10_year_earnings: float) -> float:
    """
    Graham & Dodd P/E
    Formula: G&D P/E = Current Price / Average 10-Year Earnings
    """
    if avg_10_year_earnings == 0:
        raise ValueError("Average 10-Year Earnings cannot be zero")
    return current_price / avg_10_year_earnings


def value_composite_oshaughnessy(pb_percentile: float, pe_percentile: float,
                                ps_percentile: float, pcf_percentile: float,
                                ev_ebitda_percentile: float,
                                shareholder_yield_percentile: float) -> float:
    """
    Value Composite (O'Shaughnessy)
    Formula: Average Percentile of P/B, P/E, P/S, P/CF, EV/EBITDA, Shareholder Yield
    """
    return ((pb_percentile + pe_percentile + ps_percentile + pcf_percentile +
             ev_ebitda_percentile + shareholder_yield_percentile) / 6)


# ============================================================================
# END OF FINANCIAL FORMULAS MODULE
# ============================================================================

