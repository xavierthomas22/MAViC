# MAViC: Multimodal Active Learning for Video Captioning

This is the offical codebase for the work "MAViC: Multimodal Active Learning for Video Captioning" (arxiv link to be added)

We use the codebase introduced by SwinBERT (https://github.com/microsoft/SwinBERT) for our experiments. Refer the details mentioned there to train the model for the MSRVTT and MSVD Datasets.

We explore active learning for video captioning in this work, and have introduced a novel method named MAViC, which utilises our proposed Semantically Aware Sequential Entropy (SASE) acquisition function to discourage querying less-informative samples which exhibit high entropy due to semantically similar captions. We also extended our approach to capture the model uncertainty in the visual dimension by feature perturbation (M-SASE-FP) and model perturbation (M-SASE-MP) and propose multimodal extension of SASE termed as M-SASE in our study.

## To Run MAViC

1. Please refer https://github.com/microsoft/SwinBERT#download to obtain the datasets and pre-trained models.
2. Get x% of data
3. Get the required Acquisition Function Scores
