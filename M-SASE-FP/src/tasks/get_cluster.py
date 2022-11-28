from glob import glob
import torch
import faiss

def get_embeddings(folder):
    files = glob(f'{folder}/*_video_feats.bin')
    for i,file in enumerate(files):
        embeddings = torch.load(file).view(1,-1)
        if i==0:
            all_embeddings = embeddings
        else:
            all_embeddings = torch.stack([all_embeddings,embeddings])
    return all_embeddings, files

def cluster_fp(files, embeddings, K=300, M=5, epsilon=0.015):
    d = embeddings.shape[1]
    kmeans = faiss.Kmeans(d, K)
    kmeans.train(embeddings)

    for file,emb in zip(files,embeddings):
        index = faiss.IndexFlatL2(emb)
        index.add(emb)
        D, I = index.search(kmeans.centroids, M)
        for i in range(M):
            fp_emb = emb + epsilon*embeddings[I[i]]
            torch.save(fp_emb,f'{file}[:-4]_fp_{i}.bin')

folder = '../datasets/MSRVTT-V2/videos/'
K = 300
M = 5
epsilon = 0.015

embeddings, files = get_embeddings(folder)
cluster_fp(files, embeddings, K=300, M=5, epsilon=0.015)