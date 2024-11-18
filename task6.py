import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

clients = pd.read_csv('clients.csv')
movies = pd.read_csv('movies.csv')
orders = pd.concat([pd.read_csv(f'orders_{i}.csv') for i in range(1, 3)], ignore_index=True)

df = orders.merge(clients, on='client_id').merge(movies, on='movie_id')

top_ua_movies = df[df['country'] == 'Україна'].groupby('title')['order_id'].count().sort_values(ascending=False).head(3)
print("Три найпопулярніші вітчизняні фільми:")
print(top_ua_movies)

plt.pie(df['country'].value_counts(), labels=df['country'].value_counts().index)
plt.title('Обсяги замовлень за країною-виробником')
plt.show()

date_picker = widgets.DatePicker(
    description='Виберіть дату:',
    disabled=False
)

def on_value_change(change):
    selected_date = change['new']
    filtered_df = df[df['date'] >= selected_date]
    display(filtered_df[['client_name', 'title']])

date_picker.observe(on_value_change, names='value')
display(date_picker)