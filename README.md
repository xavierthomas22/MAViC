# MAViC: Multimodal Active Learning for Video Captioning

This is the offical codebase for the work "MAViC: Multimodal Active Learning for Video Captioning" (arxiv link to be added)

We base our code on SwinBERT (https://github.com/microsoft/SwinBERT). Refer the details mentioned there for more instructions on how to download datasets, and train models.

Through this work we explore active learning for video captioning, and have introduced a novel method named MAViC, which utilises our proposed Semantically Aware Sequential Entropy (SASE) acquisition function to discourage querying less-informative samples which exhibit high entropy due to semantically similar captions. We also extended our approach to capture the model uncertainty in the visual dimension by feature perturbation (M-SASE-FP) and model perturbation (M-SASE-MP) and propose multimodal extension of SASE termed as M-SASE in our study.

## To Run MAViC

1. run_caption_VidSwinBert.py using deafult parameters, using 5% data
2. run_caption_VidSwinBert_inference.py using  best checkpiont to get top_selected_samples.pkl as unlabelled indices
3. Add above indeices with previous train indices and do step 1
