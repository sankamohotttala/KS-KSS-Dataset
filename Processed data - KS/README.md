## JSON File Structure

The dataset is organized as a list of frame-wise pose annotations in JSON format.

### Top-Level
- `data`: List of frame entries.

### Each Frame Entry (`data[i]`)
- `frame_index` *(int)*: Index of the frame.
- `skeleton` *(list)*: List of detected persons in the frame.

### Each Skeleton Entry (`skeleton[j]`)
- `pose` *(list of floats)*: Flattened list of keypoint coordinates `[x1, y1, x2, y2, ..., xn, yn]`.
- `score` *(list of floats)*: Confidence scores corresponding to each keypoint.

### Schema Overview
```json
{
  "data": [
    {
      "frame_index": <int>,
      "skeleton": [
        {
          "pose": [x1, y1, x2, y2, ..., xn, yn],
          "score": [s1, s2, ..., sn]
        }
      ]
    }
  ]
}


## Dataset File Details

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
