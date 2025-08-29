import os
import segmentation
import joblib

current_dir = os.path.dirname(os.path.realpath(__file__))
model_dir = os.path.join(current_dir, 'models/svc/svc.pkl')
model = joblib.load(model_dir)

classifaction_result = []
for character in segmentation.characters:
    character = character.reshape(1, -1);
    result = model.predict(character)
    classifaction_result.append(result)

print(classifaction_result)

plate_string = ''
for each in classifaction_result:
    plate_string += each[0]

print(plate_string)

colum_list_copy = segmentation.column_list[:]
segmentation.column_list.sort()
rightplate_string = ''
for each in segmentation.column_list:
    rightplate_string += plate_string[colum_list_copy.index(each)]

print(rightplate_string)