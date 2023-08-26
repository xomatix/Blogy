import datetime
from pydantic import BaseModel
from typing import Optional

table_name = "tb_posts"

class Post(BaseModel):
    id: int
    title: str
    description: str
    surface: float
    price: float
    category: int
    location: str
    date_of_creation: datetime.datetime
    parameters: str

    def generate_create_table_sql():
        columns = []
        for attr_name, attr_type in Post.__annotations__.items():
            if attr_name == "id":
                columns.append(f"{attr_name} INTEGER PRIMARY KEY AUTOINCREMENT")
            else:
                columns.append(f"{attr_name} {attr_type.__name__}")
                
        return f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
    
    def generate_insert_query(data_dict):
        return f"INSERT INTO {table_name} (title, description, surface, price, category, location, date_of_creation, parameters) VALUES \
            ('{data_dict.title}', '{data_dict.description}', {data_dict.surface}, {data_dict.price}, {data_dict.category}, '{data_dict.location}',\
            '{data_dict.date_of_creation}', '{data_dict.parameters}');"
    
    def generate_update_query(data_dict):
        return f"UPDATE {table_name} SET title = '{data_dict.title}', description = '{data_dict.description}', surface = {data_dict.surface}, \
            price = {data_dict.price}, category = {data_dict.category}, location = '{data_dict.location}', date_of_creation = '{data_dict.date_of_creation}'\
            , parameters = '{data_dict.parameters}' WHERE id = {data_dict.id};"
    
    def generate_delete_query(data_id):
        return f"DELETE FROM {table_name} WHERE id = {data_id};"

    def generate_select_query(category = None):
        return f"SELECT id AS 'id', title, description, surface, price, category, location, date_of_creation, parameters FROM \
        {table_name} WHERE {'category' if category != None else ''} {'=' if category != None else ''} {category if category != None else ''};"
    


