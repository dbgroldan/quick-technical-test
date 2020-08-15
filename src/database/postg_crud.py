# -*- coding: utf-8 -*-
import psycopg2
from utils.filter_generators import generateSQLFilter

class ObjectDAO:
    def __init__(self, connection, table_name):
        self.conn, self.cursor =  connection.getConnection()
        self.table_name = table_name
        self.params = self.defineParams()

    def defineParams(self):
        table = self.table_name.split('.')[-1]
        query = """SELECT column_name
            FROM information_schema.columns
            WHERE table_name = '{}';
            """.format(table)
        params = []
        try:
            self.cursor.execute(query)
            objs_query = self.cursor.fetchall()
            for elem in objs_query:
                params.append(elem[0])
        except (Exception, psycopg2.Error) as error:
            print("TB Error:", error)
        return params

    def add(self, elem):
        query = 'INSERT INTO {}('.format(self.table_name)
        data_spc_query = ''
        data_query = []
        attrbs_table = list(elem.keys())
        for a in attrbs_table:
            if a != attrbs_table[-1]:
                query += a + ', '
                data_spc_query += '%s, '
            else:
                query += a + ') VALUES('
                data_spc_query += '%s);'
            data_query.append(elem.get(a))
        query+= data_spc_query
        query = '{} RETURNING id;'.format(query[:-1])
        try:
            self.cursor.execute(query, tuple(data_query))
            res = self.cursor.fetchone()[0]
            self.conn.commit()
            print('Database: New data added')
            return res
        except (Exception, psycopg2.Error) as error:
            print(error)
            return False


    def findAll(self):
        objs = []
        query = 'SELECT * FROM {};'.format(self.table_name)
        try:
            self.cursor.execute(query)
            objs_query = self.cursor.fetchall()
            for elem in objs_query:
                res = {self.params[i] : elem[i] for i, _ in enumerate(elem)}
                objs.append(res)
        except (Exception, psycopg2.Error) as error:
            print("TB Error:", error)
        return objs

    def findById(self, id):
        filt = {
            'and': [
                {
                    'condition': '=',
                    'param': 'id',
                    'value': id
                }
                ]}
        return self.findByFilter(filt)


    def findByFilter(self, filt):
        query = 'SELECT * FROM {} WHERE '.format(self.table_name)
        query += generateSQLFilter(filt, ['and', 'or'])
        query += ';'
        objs = []
        try:
            self.cursor.execute(query)
            objs_query = self.cursor.fetchall()
            for elem in objs_query:
                res = {self.params[i] : elem[i] for i, _ in enumerate(elem)}
                objs.append(res)
        except (Exception, psycopg2.Error) as error:
            print("TB Error:", error)
        return objs

    def update(self, data, filt):
        query = 'UPDATE {} SET '.format(self.table_name)
        attribs = list(data.keys())
        data_query = []
        for attrib_data in attribs:
            current_data = data.get(attrib_data)
            data_query.append(current_data)
            query += attrib_data + ' = %s'
            if current_data != data[attribs[-1]]:
                query += ', '
        query += ' WHERE ' + generateSQLFilter(filt, ['and', 'or'])
        try:
            self.cursor.execute(query, tuple(data_query))
            self.conn.commit()
            print('Database: Data updated')
            return True
        except (Exception, psycopg2.Error) as error:
            print(error)
            return False

    def delete(self, id):
        query = 'DELETE FROM {}'.format(self.table_name)
        filt = {
            'and': [
                {
                    'condition': '=',
                    'param': 'id',
                    'value': id
                }
                ]}
        query += ' WHERE ' + generateSQLFilter(filt, ['and', 'or'])
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print('Database: Data deleted')
            return True
        except (Exception, psycopg2.Error) as error:
            print(error)
            return False
