# MAViC: Multimodal Active Learning for Video Captioning

This is the offical codebase for the work "MAViC: Multimodal Active Learning for Video Captioning" (arxiv link to be added)

We base our code on SwinBERT (https://github.com/microsoft/SwinBERT). Refer the details mentioned there for more instructions on how to download datasets, and train models.

Through this work we explore active learning for video captioning, and have introduced a novel method named MAViC, which utilises our proposed Semantically Aware Sequential Entropy (SASE) acquisition function to discourage querying less-informative samples which exhibit high entropy due to semantically similar captions. We also extended our approach to capture the model uncertainty in the visual dimension by feature perturbation (M-SASE-FP) and model perturbation (M-SASE-MP) and propose multimodal extension of SASE termed as M-SASE in our study.

## To Run MAViC

1. Please refer https://github.com/microsoft/SwinBERT#download to obtain the datasets and pre-trained models.
2. Get x% of data
3. Get the required Acquisition Function Scores
