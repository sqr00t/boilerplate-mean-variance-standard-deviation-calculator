import numpy as np

def calculate(list):
    #raise ValueError if list not 9 elements
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
    #reshape list into 3x3 np array
        arr = np.reshape(list,(3,3))
    #initialise empty dictionary calc
        calc = {}
    #add keys:values to calc, with according np.operation converted to list
        calc['mean'] = [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr).tolist()]
        calc['variance'] = [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr).tolist()]
        calc['standard deviation'] = [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr).tolist()]
        calc['max'] = [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr).tolist()]
        calc['min'] = [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr).tolist()]
        calc['sum'] = [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr).tolist()]
    #return dictionary calc
    return calc