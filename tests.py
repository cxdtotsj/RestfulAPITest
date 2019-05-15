import resources.settings as s

print(s.BASE_DIR)
print(s.BASE_URL)
print(s.CASE_DATABASE.get("default").get("HOST"))
print(s.CASE_DATABASE.get("default").get("PORT"))
print(s.CASE_DATABASE.get("default").get("NAME"))
print(s.CASE_DATABASE.get("default").get("USER"))
print(s.CASE_DATABASE.get("default").get("PASSWORD"))