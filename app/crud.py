from app.db_client import get_supabase_client

supabase = get_supabase_client()

def insert_user(first_name: str, last_name: str, city: str, country: str, zip_code: str):
    response = (
        supabase.table("user")
        .insert({
           "first_name": first_name,
            "last_name": last_name,
            "city": city,
            "country": country,
            "zip_code": zip_code
        })
        .execute()
    )
    return response


def get_all_users():
    response = (
        supabase.table("user")
        .select("*")
        .execute()
    )
    return response.data


def update_user(user_id: int, update_data: dict):
    response = (
        supabase.table("user")
        .update(update_data)
        .eq("id", user_id)
        .execute()
    )
    return response



def delete_user(user_id: int):
    response = (
        supabase.table("user")
        .delete()
        .eq("id", user_id)
        .execute()
    )
    return response
