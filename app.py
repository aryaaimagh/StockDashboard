import streamlit as st
from financial_data import get_income_statement_df
from charts import create_bar_chart, create_stack_bar_chart

def main():
    st.title("stock dashboard")
    ticker = st.text_input("ticker")
    if ticker:
        income_statement_data_df = get_income_statement_df(ticker)
        st.write(income_statement_data_df)

        # create a 2 column layout
        col1, col2, col3 = st.columns(3)
            
        with col1:
            create_bar_chart_te=create_bar_chart(income_statement_data_df, "calendarYear", "revenue",  "Revenue")
            st.plotly_chart(create_bar_chart_te, config={"displayModeBar": False}, use_container_width=True)
            
        with col2:
            create_stack_bar_chart_te = create_stack_bar_chart(income_statement_data_df, "calendarYear", ["grossProfitRatio", "operatingIncomeRatio"],  "")
            st.plotly_chart(create_stack_bar_chart_te, config={"displayModeBar": False}, use_container_width=True)

        with col3:
            create_stack_bar_chart_teh = create_stack_bar_chart(income_statement_data_df, "calendarYear", ["researchAndDevelopmentExpenses","sellingGeneralAndAdministrativeExpenses"],  "")
            st.plotly_chart(create_stack_bar_chart_teh, config={"displayModeBar": False}, use_container_width=True)
    
if __name__ == "__main__":
    main()
