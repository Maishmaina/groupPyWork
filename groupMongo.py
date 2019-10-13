#SIMPLE CRUID METHOD python for altas
from pymongo import MongoClient
client=MongoClient("mongodb+srv://daniel:mnbvcxz1@cluster0-lcthw.mongodb.net/test?retryWrites=true&w=majority")
#call altas dbname 
db=client.get_database('student_db')
#name of coll.
records=db.students_records
#coutColl.
records.count_documents({})
#create newDocUseDictionary
new_student={
    'name':'ken',
    'age':20,
    'reg': 'p100/1180g/16'
}
records.insert_one(new_student)
#createInGroup
new_students=[{
    'name':'lint',
    'age':23,
    'reg': 'p101/1280g/16'
},
{
    'name':'kimonyoski',
    'age':24,
    'reg': 'p100/1380g/16'
}]
records.insert_many(new_students)

#PopulateDataFromDb
list(records.find())

#FindSpecific
records.find_one({'reg':'p100/1173g/16'})

#UpdateSpesificDictionary
student_updates={
    'name':'maina'
}
records.update_one({'reg':'p100/1173g/16'},{'$set':student_updates})

#DELETECODE
records.delete_one({'reg':'p100/1180g/16'})
