def clustering_details(model, maximum_value):
    # Get the cluster labels
    labels = model.labels_

    # Initialize a dictionary to store words in each cluster
    words_in_clusters = {i: [] for i in range(len(set(labels)))}
    # Associate each word with its corresponding cluster label
    for word, label in zip(df['word'].tolist(), df['Cluster'].tolist()):
        words_in_clusters[label].append(word)

    # Print words in each cluster
    for cluster, words_in in words_in_clusters.items():
        print(f"Cluster {cluster}: {words_in}")

    # Print the number of words in each cluster
    unique, counts = np.unique(labels, return_counts=True)
    print(dict(zip(unique, counts)))

    # Get the cluster centers
    centroids = model.cluster_centers_

    total_count = []

    # Find the closest word to each centroid
    for i, centroid in enumerate(centroids):
        # Filter embeddings belonging to the current cluster
        # cluster_embeddings = df['embedding'][labels == i]
        cluster_embeddings = np.vstack(df['embedding'][labels == i])

        # Check and adjust shapes
        if cluster_embeddings.shape[1] != centroid.shape[0]:
            print(
                f"Dimension mismatch: Embeddings have {cluster_embeddings.shape[1]} features, but centroid has {centroid.shape[0]} features.")
            continue  # Skip this iteration

        # Reshape centroid to be a 2D array with one row
        # centroid_reshaped = centroids.reshape(1, -1)

        # Calculate the distance between the centroid and embeddings in the cluster
        distances = np.linalg.norm(cluster_embeddings - centroid, axis=1)

        # Find the indices of the 3 closest embeddings
        closest_indices = np.argsort(distances)[:maximum_value]

        # Retrieve the corresponding words
        closest_words = [df['word'].tolist()[np.where(labels == i)[0][index]] for index in closest_indices]

        # Print the closest words to the centroid
        print(f"Closest words to centroid {i}: {closest_words}")

        # create a list counting the number of times a string appears
        count = [0, 0, 0, 0, 0, 0]

        # Assuming 'closest_words' is a list of words and 'dictionary' is structured as provided
        for word in closest_words:
            found = False
            for category, content in hierarchy.items():
                if found:
                    break
                # Check in divisions first
                for division, division_content in content.get('divisions', {}).items():
                    for section, words in division_content.get('sections', {}).items():
                        if word in words:
                            if category == "WORDS EXPRESSING ABSTRACT RELATIONS":
                                count[0] += 1
                            elif category == "WORDS RELATING TO SPACE":
                                count[1] += 1
                            elif category == "WORDS RELATING TO MATTER":
                                count[2] += 1
                            elif category == "WORDS RELATING TO THE INTELLECTUAL FACULTIES":
                                count[3] += 1
                            elif category == "WORDS RELATING TO THE VOLUNTARY POWERS":
                                count[4] += 1
                            elif category == "WORDS RELATING TO THE SENTIENT AND MORAL POWERS":
                                count[5] += 1
                            found = True
                            break
                    if found:
                        break
                # Check in sections if not found in divisions
                if not found:
                    for section, words in content.get('sections', {}).items():
                        if word in words:
                            if category == "WORDS EXPRESSING ABSTRACT RELATIONS":
                                count[0] += 1
                            elif category == "WORDS RELATING TO SPACE":
                                count[1] += 1
                            elif category == "WORDS RELATING TO MATTER":
                                count[2] += 1
                            elif category == "WORDS RELATING TO THE INTELLECTUAL FACULTIES":
                                count[3] += 1
                            elif category == "WORDS RELATING TO THE VOLUNTARY POWERS":
                                count[4] += 1
                            elif category == "WORDS RELATING TO THE SENTIENT AND MORAL POWERS":
                                count[5] += 1
                            found = True
                            break

        # find in which class the closest words are
        # for word in closest_words:
        #    upper_level = dictionary[dictionary[word][0]]
        #    # the number of words in the upper level is less than 4 (divisions have max 3 words)
        #    if len(upper_level.split()) < 4:
        #        upper_level = dictionary[upper_level]
        #
        #    if upper_level == "WORDS EXPRESSING ABSTRACT RELATIONS":
        #        count[0] = count[0] + 1
        #    elif upper_level == "WORDS RELATING TO SPACE":
        #        count[1] = count[1] + 1
        #    elif upper_level == "WORDS RELATING TO MATTER":
        #        count[2] = count[2] + 1
        #    elif upper_level == "WORDS RELATING TO THE INTELLECTUAL FACULTIES":
        #        count[3] = count[3] + 1
        #    elif upper_level == "WORDS RELATING TO THE VOLUNTARY POWERS":
        #        count[4] = count[4] + 1
        #    elif upper_level == "WORDS RELATING TO THE SENTIENT AND MORAL POWERS":
        #        count[5] = count[5] + 1

        total_count.append(count)
    return total_count


def match_clusters_to_classes(total_count):
    relation = []
    for j in range(len(total_count)):
        max_pos = -1
        max_val = -1
        max_index = -1
        # for each list in total_count, get the index of the maximum value and the maximum value
        for i in range(len(total_count)):
            # print(i, total_count[i].index(max(total_count[i])), max(total_count[i]))
            # i is cluster and index is the closest class
            if max(total_count[i]) > max_val:
                max_val = max(total_count[i])
                max_pos = i
                max_index = total_count[i].index(max(total_count[i]))
        print(max_pos, max_index, max_val)
        # cluster and class+
        relation.append([max_pos, max_index])

        # replace the values in position max_index in each of the lists with -1
        for i in range(len(total_count)):
            total_count[i][max_index] = -1
            # print(total_count[i])
        # replace each element of the list in position max_pos with -1
        for i in range(len(total_count[max_pos])):
            total_count[max_pos][i] = -1

    return relation


def remap(labels, relation):
    # remap the clusters to the classes based on the relation
    # (relation[i][0] is the cluster and relation[i][1] is the class to map to)
    for i in range(len(labels)):
        for j in range(len(relation)):
            if labels[i] == relation[j][0]:
                labels[i] = relation[j][1]
                break

    return labels