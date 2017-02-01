import yaml
import os

"""
Appends more sequences to the db_info.yaml file (only if they are new)

Recommend to backup the db_info.yaml file before the operation
"""
# *** Change here ***
yaml_path = "/Users/eddie/Documents/Projects/Repositories/davis/data/DAVIS/Annotations/db_info.yml"
gygos_frames_path = '/Volumes/Public/GyGO-datasets/GyGO/GyGO-object-frames/seg_prod_t06'

# *** Don't change below ***
print('Running script add_to_db_info_yaml.py')
stream = open(yaml_path, 'r')
data = yaml.load(stream)
existing_seq_names = [seq['name'] for seq in data['sequences']]

root_dir = os.path.basename(gygos_frames_path)

for curr_dir in os.listdir(gygos_frames_path):
    if curr_dir[0] == '.':
        continue  # means it's a hidden folder
    seq_name = os.path.join(root_dir, curr_dir)
    if not seq_name in existing_seq_names:
        """
        Example seq_dict:
        - attributes: [FM, CS, MB, DEF, ROT, EA]
          name: dog
          num_frames: 60
          set: test
          eval_t: False
        """
        seq_dict = {'attributes': [],
                    'name': seq_name,
                    'num_frames': len(
                        os.listdir(os.path.join(gygos_frames_path, curr_dir))),
                    'set': 'gygo-training',
                    'eval_t': False}  # Hardcoded: evaluate T for this video?
        data['sequences'].append(seq_dict)

with open(yaml_path, 'w') as yaml_file:
    yaml_file.write(yaml.dump(data))

print('Finished!')