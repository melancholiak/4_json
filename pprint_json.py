import json,sys
def load_data(filepath):
  with open(filepath,encoding='cp1251') as json_record:
    result = json.load(json_record)
  return result
def pretty_print_json(json_obj):
  def sub_print(json_record,ind=0,ignore=False):
    if isinstance(json_record,dict):
      lst = [sub_print(key,ind+1,False)+':'+\
             sub_print(json_record[key],ind+1,True)\
            for key in json_record]
      if ignore: # if this dict is content of other dont add indent
        return '{{\n{}\n{}}}'.format(',\n'.join(lst),'  '*ind)
      else:
        return '{}{{\n{}\n{}}}'.format('  '*ind,',\n'.join(lst),'  '*ind)
    elif isinstance(json_record,list):
      lst = [sub_print(i,ind+1,False) for i in json_record]
      if ignore: #if this list is content of other dont add indent
        return '[\n{}\n{}]'.format(',\n'.join(lst),'  '*ind)
      else:
        return '{}[\n{}\n{}]'.format('   '*ind,',\n'.join(lst),'  '*ind)
    else:
      if ignore:
        return repr(json_record)
      else:
        return '  '*ind+repr(json_record)
  print(sub_print(json_obj))
if __name__ == '__main__':
  null = None
  pretty_print_json((load_data(sys.argv[1])))
