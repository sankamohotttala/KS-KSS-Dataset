# KS Dataset Repository

This repository contains the dataset and preprocessing code used for the KS dataset, formatted for various protocols and compatibility with pose-estimation-based action recognition pipelines.

---

## 📁 Folder Structure

- `1_kinetics-skeleton format/`  
  This folder contains the KS dataset in the **Kinetics-Skeleton JSON format**, widely used in pose-based human action recognition.  
  This standard format ensures compatibility with common pose-estimation pipelines and simplifies preprocessing workflows.

- `2_full_npy_pkl_format/`  
  Contains the **full KS dataset** converted into `.npy` and `.pkl` formats.  
  These files can be used under various KS-X protocols that apply different train-test splitting strategies.

- `3_final_split_and_tfrecord/`  
  Includes the **final dataset** used in the implementations of this paper and our associated journal publication.  
  This version contains all 8 classes. For experiments using protocol-specific subsets, this dataset should be re-split accordingly.  
  Additionally, `.tfrecord` files for the **KS-Full protocol** are included here. For other protocols, new `.tfrecord` files should be generated.

- `STGCN_PreProcess_code/`  
  This directory holds the preprocessing code used to convert data between various formats:  
  - JSON → `.npy` / `.pkl`  
  - `.npy` / `.pkl` → `.tfrecord`  
  These scripts are essential for standardizing the dataset and preparing it for model training and evaluation.

---

## JSON File Structure (in `1_kinetics-skeleton format/`)

The dataset in this folder is organized using a frame-wise JSON annotation format. Each JSON file corresponds to a video and follows the structure described below.

### Top-Level
- `data`: List of frame entries.

### Each Frame Entry (`data[i]`)
- `frame_index` *(int)*: The frame number within the video.
- `skeleton` *(list)*: List of detected persons for that frame.

### Each Skeleton Entry (`skeleton[j]`)
- `pose` *(list of floats)*: Flattened list of 2D keypoint coordinates `[x1, y1, x2, y2, ..., xn, yn]`.
- `score` *(list of floats)*: Confidence scores for each corresponding keypoint.

### Schema Overview
```json
{
  "data": [
    {
      "frame_index": "int",
      "skeleton": [
        {
          "pose": ["x1", "y1", "x2", "y2", "...", "xn", "yn"],
          "score": ["s1", "s2", "...", "sn"]
        }
      ]
    }
  ]
}
```



## Dataset File Details (in 2_full_npy_pkl_format/)

The dataset consists of feature arrays stored in `.npy` files and associated class labels and YouTube IDs stored in `.pkl` files. The key statistics for each are summarized below:

| File Type | Description                          | Shape / Details            | Unique Classes         |
|-----------|--------------------------------------|----------------------------|------------------------|
| `.npy`    | Sample features (skeleton format)     | `(1400, 3, 300, 25, 2)`     | –                      |
| `.pkl`    | Class labels & YouTube IDs            | 1400 entries in second list | `[48, 83, 156, 68]`     |
| `.npy`    | Sample features (skeleton format)     | `(993, 3, 300, 25, 2)`      | –                      |
| `.pkl`    | Class labels & YouTube IDs            | 993 entries in second list  | `[57, 330, 30, 255]`    |

### Notes:
- The `.npy` files follow the format: `(N, C, T, V, M)`  
  - `N`: Number of samples  
  - `C`: Number of channels (e.g., x, y, confidence)  
  - `T`: Number of frames  
  - `V`: Number of joints  
  - `M`: Number of persons  
- The `.pkl` files contain:
  - A second list of length equal to `N`
  - Labels and IDs, where labels are encoded as integers for classification tasks
