# KS-KSS Dataset

# Kinetics Subsets (KS) 

This folder contains a curated subset of the Kinetics-600 dataset. These classes have been selected to represent a diverse range of physical activities relevant to children's action recognition tasks.

## Included Action Classes

| Class Name      | Kinetics-600 Class ID |
|-----------------|------------------------|
| pullups         | 255                    |
| squat           | 330                    |
| watermelon      | 83                     |
| baseball        | 48                     |
| clapping        | 57                     |
| climbingTree    | 68                     |
| hopscotch       | 156                    |
| jumping         | 30                     |

## Accessing Raw Video References

The `Raw files` directory in this repository contains metadata files categorized under:

- `All adult`
- `all child`
- `All data (child and adult)`

Each file in these folders lists YouTube video IDs corresponding to a specific action class. The filenames follow the format `<class_name>_<class_id>.txt`, and each file contains a list of samples for that class.

These `.txt` files reference the original Kinetics-600 videos and can be used—along with the official [Kinetics-600 dataset](https://github.com/cvdfoundation/kinetics-dataset)—to obtain the RGB action clips. The official dataset provides CSV files containing key metadata such as:

- `youtube_id`
- `label` (action class)
- `start_time` and `end_time` of the action
- `subset` (train/val/test split)

Using this information, you can download the full videos and extract the relevant action clips.

Alternatively, already-trimmed action clips can be directly downloaded from the [CVD Foundation Kinetics Dataset](https://github.com/cvdfoundation/kinetics-dataset), which provides easy access to preprocessed segments. You can select the KS subset from this RGB dataset.


**Note**: The Kinetics-600 dataset must be separately obtained and is not included in this repository due to licensing and size constraints.

---

### Pre-Processed RGB Videos Available

For convenience, we have already trimmed and processed the required RGB videos corresponding to the KS dataset. These are available for direct access via Google Drive:

[Download RGB Videos (KS Dataset)](https://drive.google.com/drive/folders/1CaeN2eee1TLbrFxCGEdWhGis-AaZXvD7?usp=sharing)

This saves users the effort of video collection and processing, making it easier to directly work on downstream tasks like action recognition or transfer learning.






Please contact Sanka Mohottala (sanka.m@sliit.lk) for detailed guidelines on how to use this dataset along with necessary codes.
