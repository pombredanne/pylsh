###A basic Locality Sensitve Hashing Library for python 
  
##### How to use
To initialize a lsh indexer/querier

```
lshash = lsh.Lsh(feat_dim=50, sig_dim=500, similarity_measure=lsh.CosineSimilarity(), b=10)
```
where 

- `feat_dim` specifies the feature dimension
- `sig_dim` specifies the signature dimension
- `similarity_measure` specifies the similarity measure to use. Currently pylsh supports two similarity measures: `lsh.JaccardSimilarity` and `lsh.CosineSimilarity`.
- `b` specifies the number of bands for hashing

to instantiate a object that can be indexed in pylsh

```
obj = lsh.LshObject(feature_vector)
```

To index an object

```
lshash.index(obj)
```

to retrieve similar object
```
lshash.retrieve(obj)
```

#####dependencies
1. mmh3
2. numpy
3. bitarray

#####TODO:
- Use Redis as backend storage