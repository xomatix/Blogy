from fastapi import APIRouter
from Posts.PostModel import Post
from DB.DataBaseConnect import ConnectToDB
from datetime import datetime
import json
import random

router = APIRouter()

@router.get("/tylko/do/dodania/danych/{category}")
async def read_item(category: int):
    list = []

    for i in range(30):
        if category == 0:
            list.append(Post(id=0,title=f"Tytuł aukcji Mieszkania nr {i}", description=f"Opis mieszkania z balkonem nr {i}", price=random.randrange(100_000, 1_000_000, 10_000),
            surface=random.randint(20,90), category=category, location="lang0:long0", date_of_creation=datetime.now(), parameters=json.dumps({
                "liczba pokoi": "3",
                "stan wykończenia": "stan surowy"
            })))
        if category == 1:
            list.append(Post(id=0,title=f"Tytuł aukcji Domu nr {i}", description=f"Opis domu z ogrodem nr {i}", price=random.randrange(200_000, 1_500_000, 10_000),
            surface=random.randint(80,300), category=category, location="lang0:long0", date_of_creation=datetime.now(), parameters=json.dumps({
                "liczba pokoi": "5",
                "stan wykończenia": "stan pod klucz"
            })))
        if category == 2:
            list.append(Post(id=0,title=f"Tytuł aukcji Działki nr {i}", description=f"Opis działki nr {i}", price=random.randrange(50_000, 1_500_000, 10_000),
            surface=random.randint(100,1_000), category=category, location="lang0:long0", date_of_creation=datetime.now(), parameters=json.dumps({
                "dostępne media": "woda, prąd",
                "stan": "wyrównana goła gleba"
            })))
    for i in list:
        await add_item(i)
    return {"message": f"route testowy nie używać do produkcji. item_id: {category}"}


#a potem auth
@router.post("/")
async def add_item(post: Post):
    conn = ConnectToDB()
    cursor = conn.cursor()
    post.date_of_creation = datetime.now()
    #print(Post.generate_insert_query(post))
    response = cursor.execute(Post.generate_insert_query(post))
    conn.commit()
    conn.close()

    return response

#put update
@router.put("/{item_id}")
async def update_item(item_id: int,post: Post):
    conn = ConnectToDB()
    cursor = conn.cursor()
    post.date_of_creation = datetime.now()
    post.id = item_id
    response = cursor.execute(Post.generate_update_query(post)).fetchone()
    conn.commit()
    conn.close()

    return {"message": "success"}

#delete 
@router.delete("/{item_id}")
async def delete_item(item_id: int):
    conn = ConnectToDB()
    cursor = conn.cursor()
    print(Post.generate_delete_query(item_id))
    response = cursor.execute(Post.generate_delete_query(item_id)).fetchmany(0)
    conn.commit()
    conn.close()

    return response

#query with list with filters like category and number of rows page skip like that
#dodaj filter po kategorii
# dodaj po 20 rekordów żeby coś było
@router.get("/")
async def read_items(category: int):
    conn = ConnectToDB()
    cursor = conn.cursor()
    print(Post.generate_select_query(category))
    response = cursor.execute(Post.generate_select_query(category)).fetchall()
    conn.commit()
    conn.close()

    objects_list = [Post(id=row[0], title=row[1], description=row[2], surface=row[3], price=row[4], category=row[5], location=row[6], date_of_creation=row[7], parameters=row[8]) for row in response]
    for i in objects_list:
        i.parameters = json.loads(i.parameters)
    return objects_list

