#include <stdlib.h>
#include <string.h>

typedef struct {
    int num;
    int freq;
} Pair;

void merge(Pair* arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    Pair* L = malloc(n1 * sizeof(Pair));
    Pair* R = malloc(n2 * sizeof(Pair));

    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int i = 0; i < n2; i++) R[i] = arr[mid + 1 + i];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i].freq >= R[j].freq) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];

    free(L);
    free(R);
}

void mergeSort(Pair* arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {
    int hash [20001] = {0};
    for (int i = 0; i < numsSize; i++) {
        hash[nums[i] + 10000]++;
    }

    int uniqueCount = 0;
    for (int i = 0; i < 20001; i++) {
        if (hash[i] > 0) uniqueCount++;
    }

    Pair* pairs = malloc(uniqueCount * sizeof(Pair));
    int idx = 0;
    for (int i = 0; i < 20001; i++) {
        if (hash[i] > 0) {
            pairs[idx].num = i - 10000;
            pairs[idx].freq = hash[i];
            idx++;
        }
    }

    mergeSort(pairs, 0, uniqueCount - 1);

    int* result = malloc(k * sizeof(int));
    for (int i = 0; i < k; i++) {
        result[i] = pairs[i].num;
    }

    *returnSize = k;
    free(pairs);
    return result;
}
