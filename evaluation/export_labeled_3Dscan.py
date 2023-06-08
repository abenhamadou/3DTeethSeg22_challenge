import trimesh
import json
from colormap import hex2rgb


fdi_colors = {
               "18": "#ffe2e2", "17": "#ffc6c6", "16" : "#ffaaaa", "15":"#ff8d8d", "14":"#ff7171", "13":"#ff5555",
    "12": "#ff3838", "11": "#ff0000", "21": "#0000ff", "22": "#3838ff", "23": "#5555ff", "24": "#7171ff", "25":"#8d8dff","26":"#aaaaff",
    "27": "#c6c6ff",
    "28": "#e2e2ff",
    "38":"#001c00",
     "37":"#003800",
    "36":"#005500",
     "35":"#007100",
     "34":"#008d00",
     "33":"#00aa00",
     "32":"#00c600",
     "31":"#00ff00",
     "48":"#8000ff",
     "47":"#9c38ff",
     "46":"#aa55ff",
     "45":"#b871ff",
     "44":"#c68dff",
     "43":"#d4aaff",
     "42":"#e2c6ff",
     "41":"#f0e2ff",
     "0":"#000000"
}

if __name__ == "__main__":
    obj_path = '**********.obj'
    json_path = obj_path.replace('obj', 'json')

    patient_name = obj_path.split('/')[-1]
    export_path = './test/' + patient_name

    mesh = trimesh.load(obj_path, process=False)
    with open(json_path, 'r') as fp:
        json_data = json.load(fp)
    # color label
    for i, lbl in enumerate(json_data['labels']):
        if lbl != 0:
            color = list(hex2rgb(fdi_colors[str(lbl)]))
            color.append(255)
            mesh.visual.vertex_colors[i] = color

    mesh.export(export_path)
