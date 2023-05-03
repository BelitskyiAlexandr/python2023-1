def merge_sorted_arrays(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        arr1 = list(map(int, f1.read().split()))
        arr2 = list(map(int, f2.read().split()))

        merged = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        while i < len(arr1):
            merged.append(arr1[i])
            i += 1
        while j < len(arr2):
            merged.append(arr2[j])
            j += 1

        out.write(' '.join(map(str, merged)))


merge_sorted_arrays('file1.txt', 'file2.txt', 'merged_file.txt')
