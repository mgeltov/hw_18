import sqlite3

# get tables
# with sqlite3.connect("movies.db") as connection:
#     cursor = connection.cursor()
#     query = """
#                 select *
#                 from sqlite_master
#                 where type = 'table'
#         """
#     cursor.execute(query)
#
#     tables = cursor.fetchall()
#     for table in tables:
#         print(table)
# table director -> id, name
# table genre -> id, name
# table movie -> id, title, description, trailer, year, rating, genre_id, director_id


# get columns
# with sqlite3.connect("movies.db") as connection:
#     cursor = connection.cursor()
#     query = """
#             select *
#             from movie
#             limit 1
#     """
#     cursor.execute(query)
#
#     for column in cursor.description:
#         print(column[0])


with sqlite3.connect("movies.db") as connection:
    cursor = connection.cursor()
    query = """
            select *
            from movie
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row[0], row[1])