from db_client import get_supabase_client

supabase = get_supabase_client()

def insert_user(first_name: str, last_name: str, city: str, country: str, zip_code: str):
    response = (
        supabase.table("user")
        .insert({
            "First name": first_name,
            "Last name": last_name,
            "City": city,
            "Country": country,
            "Zip Code": zip_code
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