def filter_users(users, search_value, field):
    if not search_value:
        return users

    search_value = search_value.strip().lower()
    if field not in ("name", "city", "company"):
        raise ValueError("Search field must be one of: name, city, company")

    def matches(user):
        if field == "name":
            return search_value in user.get("name", "").lower()
        if field == "city":
            return search_value in user.get("address", {}).get("city", "").lower()
        if field == "company":
            return search_value in user.get("company", {}).get("name", "").lower()
        return False

    return [user for user in users if matches(user)]
