# -*- coding: utf-8 -*-
import psycopg2

connection = None

class Connection:
    def __init__(self, config):
        self.conn = connection
        self.cursor = None
        try:
            if not self.conn:
                self.conn = psycopg2.connect(config)
                self.cursor = self.conn.cursor()
            print('Database: Database Connected')
        except (Exception, psycopg2.DatabaseError) as error:
            print('ERROR:', error)

    def createTables(self, tables_config_path):
        querys = ''
        for line in open(tables_config_path):
            querys += line[:-1]
        created = map(self.executeQuery, querys.split(';'))
        res = False
        for executed in (list(created)[:-1]):
            res = True if executed else False
        return res

    def executeQuery(self, query):
        if query:
            if self.cursor:
                query += ';'
                self.cursor.execute(query)
                self.conn.commit()
                return True
        return False

    def getConnection(self):
        return self.conn, self.cursor

    def disconnect(self):
        try:
            self.cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
            print('DATABASE: Connection closed.')
