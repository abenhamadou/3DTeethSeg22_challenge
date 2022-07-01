import glob
import json
import os
import trimesh
import numpy as np
import traceback
import logging


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


class ScanSegmentation():  # SegmentationAlgorithm is not inherited in this class anymore
    def __init__(self):
        """
        Write your own input validators here
        Initialize your model etc.
        """

        #self.model = load_model()

        pass

    def load_inputs(self, input_dir): # TODO load list
        """
        Read from /input/
        Check https://grand-challenge.org/algorithms/interfaces/
        """
        # assign directory

        # iterate over files in
        # that directory
        inputs = glob.glob(f'{input_dir}/*.obj')
        logging.info("scans to proccess:", inputs)
        return inputs


    def write_outputs(self,labels, instances, jaw):
        """
        Write to /output/dental-labels.json your predicted labels and instances
        Check https://grand-challenge.org/components/interfaces/outputs/
        """
        pred_output = {'id_patient': "",
                       'jaw': jaw,
                       'labels': labels,
                       'instances': instances
                       }
        with open('/output/dental-labels.json', 'w') as fp:
            json.dump(pred_output, fp, cls=NpEncoder)

        return

    @staticmethod
    def get_jaw(scan_path):
        try:
            # read jaw from filename
            _, jaw = os.path.basename(scan_path).split('.')[0].split('_')
        except:
            # read from first line in obj file
            try:
                with open(scan_path, 'r') as f:
                    jaw = f.readline()[2:-1]
            except Exception as e:
                logging.error(str(e))
                logging.error(traceback.format_exc())
                return None

        return jaw

    def predict(self, inputs):
        """
        Your algorithm goes here
        """

        for scan_path in inputs:
            print(f"loading scan : {scan_path}")
            # read input 3D scan .obj
            try:
                # you can use trimesh or other any loader we keep the same order
                mesh = trimesh.load(scan_path, process=False)
                jaw = self.get_jaw(scan_path)
                print("jaw processed is:", jaw)
            except Exception as e:
                logging.error(str(e))
                logging.error(traceback.format_exc())
                raise
            # preprocessing if needed
            # prep_data = preprocess_function(mesh)
            # inference data here
            # labels, instances = self.model(mesh, jaw=None)
            nb_vertices = mesh.vertices.shape[0]
            instances = [2 for i in range(nb_vertices)]
            labels = [43 for i in range(nb_vertices)]
            assert (len(labels) == len(instances) and len(labels) == mesh.vertices.shape[0])

        return labels, instances, jaw

    def process(self):
        """
        Read inputs from /input, process with your algorithm and write to /output
        """
        inputs = self.load_inputs(input_dir='/input')
        print(inputs)
        labels, instances, jaw = self.predict(inputs)
        self.write_outputs(labels=labels, instances=instances, jaw=jaw)


if __name__ == "__main__":
    ScanSegmentation().process()
