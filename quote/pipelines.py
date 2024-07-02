# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# import pymongo

# class QuotePipeline:

#     def __init__(self):
#         self.conn = pymongo.MongoClient(
#             'localhost',
#             27017
#         )
#         db = self.conn['myquotes']
#         self.collection = db['quotes_tb']

#     def process_item(self, item, spider):
#         self.collection.insert_one(dict(ItemAdapter(item).asdict()))
#         return item

## SQl 
# import mysql.connector
# from itemadapter import ItemAdapter

# class QuotePipeline:
#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host='localhost',
#             user='root',        
#             password='inshaalsql@123',    
#             database='myquotes'     
#         )
#         self.cursor = self.conn.cursor()
#         self.create_table()

#     def create_table(self):
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS quotes_tb (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 title TEXT,
#                 author VARCHAR(255),
#                 tag TEXT
#             )
#         """)

#     def process_item(self, item, spider):
#         data = ItemAdapter(item).asdict()
#         self.cursor.execute("""
#             INSERT INTO quotes_tb (title, author, tag) VALUES (%s, %s, %s)
#         """, (data['title'], data['author'], ','.join(data['tag'])))
#         self.conn.commit()
#         return item

#     def close_spider(self, spider):
#         self.cursor.close()
#         self.conn.close()



from sqlalchemy.orm import sessionmaker
from itemadapter import ItemAdapter
from .models import Quote, engine

class QuotePipeline:

    def __init__(self):
        # SQLAlchemy session
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        data = ItemAdapter(item).asdict()
        
        # Quote object
        quote = Quote(
            title=data['title'],
            author=data['author'],
            tag=', '.join(data['tag'])
        )
        
        try:
            session.add(quote)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

    def close_spider(self, spider):
        pass
