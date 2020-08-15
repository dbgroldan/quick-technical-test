# -*-coding: utf-8 -*-

def generateSQLFilter(filt, params):
    complet_filt = ''
    for param in params:
        filter = filt.get(param)
        if filter:
            if param != params[0]:
                complet_filt += ' '+ param.upper() +' '
            complet_filt += generateFilter(filter, param)

    return complet_filt

def generateFilter(filt, separator):
    final_filter = ''
    for f in filt:
        if f != filt[0]:
            final_filter += ' '+ separator.upper() +' '
        final_filter += generateComparisson(f)
    return final_filter

def generateComparisson(data):
    return data.get('param') + ' ' + data.get('condition') + ' ' + data.get('value')
