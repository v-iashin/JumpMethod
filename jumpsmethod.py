import numpy as np
from sklearn.cluster import KMeans

class JumpsMethod(object):
    
    def __init__(self, data):
        self.data = data
        # dimension of 'data'; data.shape[0] would be size of 'data'
        self.p = data.shape[1]
        # vector of variances (1 by p)
        """ 'using squared error rather than Mahalanobis distance' (SJ, p. 12)
        sigmas = np.var(data, axis=0)
        ## by following the authors we assume 0 covariance between p variables (SJ, p. 12)
        # start with zero-matrix (p by p)
        self.Sigma = np.zeros((self.p, self.p), dtype=np.float32)
        # fill the main diagonal with variances for
        np.fill_diagonal(self.Sigma, val=sigmas)
        # calculate the inversed matrix
        self.Sigma_inv = np.linalg.inv(self.Sigma)"""
    
    
    def Distortions(self, cluster_range=range(1, 10 + 1), random_state=0):
        """ returns a vector of calculated distortions for each cluster number.
            If the number of clusters is 0, distortion is 0 (SJ, p. 2) 
            'cluster_range' -- range of numbers of clusters for KMeans;
            'data' -- n by p array """
        # dummy vector for Distortions
        self.distortions = np.repeat(0, len(cluster_range) + 1).astype(np.float32)

        # for each k in cluster range implement
        for k in cluster_range:
            # initialize and fit the clusterer giving k in the loop
            KM = KMeans(n_clusters=k, random_state=random_state)
            KM.fit(self.data)
            # calculate centers of suggested k clusters
            centers = KM.cluster_centers_
            # since we need to calculate the mean of mins create dummy vec
            for_mean = np.repeat(0, len(self.data)).astype(np.float32)

            # for each observation (i) in data implement
            for i in range(len(self.data)):
                # dummy for vec of distances between i-th obs and k-center
                dists = np.repeat(0, k).astype(np.float32)

                # for each cluster in KMean clusters implement
                for cluster in range(k):
                    # calculate the within cluster dispersion
                    tmp = np.transpose(self.data[i] - centers[cluster])
                    """ 'using squared error rather than Mahalanobis distance' (SJ, p. 12)
                    dists[cluster] = tmp.dot(self.Sigma_inv).dot(tmp)"""
                    dists[cluster] = tmp.dot(tmp.T)

                # take the lowest distance to a class
                for_mean[i] = min(dists)

            # take the mean for mins for each observation
            self.distortions[k] = np.mean(for_mean) / self.p

        return self.distortions
    
    
    def Jumps(self, Y=None):
        """ returns a vector of jumps for each cluster """
        # if Y is not specified use the one that suggested by the authors (SJ, p. 2) 
        if Y is None:
            self.Y = self.p / 2
        
        else:
            self.Y = Y
        
        # the first (by convention it is 0) and the second elements
        self.jumps = [0] + [self.distortions[1] ** (-self.Y) - 0]
        self.jumps += [self.distortions[k] ** (-self.Y) \
                       - self.distortions[k-1] ** (-self.Y) \
                       for k in range(2, len(self.distortions))]
        
        # calculate recommended number of clusters
        self.recommended_cluster_number = np.argmax(np.array(self.jumps))
        
        return self.jumps
