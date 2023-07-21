import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
@st.cache_data
def load_data():
    df=pd.read_csv("datasets/cleaned.csv")
    
    return df.head(1000)

st.subheader("Learn the basic structure")

st.write("Bakery Sales Data")

try:
    df = load_data()
    articles = df.article.unique()
    articles_selection = st.multiselect(

        "choose product", articles
    )
    article_selected = (df[df['article'].isin(articles_selection)].head())
    st.write(article_selected.head())

    # bar chart
    st.write("""### Total Sales of Selected Product(s) """)
    bar1 = article_selected.groupby(['article'])['Sales'].sum().sort_values(ascending=True)
    st.bar_chart(bar1)
   
    #line chart
    st.write("""### Sales over Time """)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(article_selected['datetime'], article_selected['Sales'])
    st.pyplot(fig)
    
    #pie chart
    st.write("""### Products sold""")
    pie_data = article_selected['article'].value_counts()
    fig2, ax2 = plt.subplots(figsize= (7,7))
    ax2.pie(pie_data, labels=pie_data.index,autopct="%1.1f%%", shadow=True)
    ax2.axis("equal") # gives equal aspect ratio
    st.write("Note: this is showing percentages for only the values selected")
    st.pyplot(fig2)
except ValueError as e:
    st.error("""
    
    """)
    
    


# # plotting 
# fig, ax = plt.subplots()
# ax.plot(df['datetime'], df['Sales'])
# st.pyplot(fig)