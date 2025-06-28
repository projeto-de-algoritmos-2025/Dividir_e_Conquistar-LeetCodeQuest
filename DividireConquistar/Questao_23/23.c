#include <stdlib.h>

struct ListNode* mergeLists(struct ListNode* l1, struct ListNode* l2) {
    if (!l1) return l2;
    if (!l2) return l1;
    if (l1->val < l2->val) {
        l1->next = mergeLists(l1->next, l2);
        return l1;
    } else {
        l2->next = mergeLists(l1, l2->next);
        return l2;
    }
}

struct ListNode* mergeLinkedListArray(struct ListNode** lists, int left, int right) {
    if (left > right) return NULL; //intervalo inválido
    if (left == right) return lists[left];//apenas uma lista
    int mid = (left + right) / 2;
    struct ListNode* l1 = mergeLinkedListArray(lists, left, mid);
    struct ListNode* l2 = mergeLinkedListArray(lists, mid + 1, right);
    return mergeLists(l1, l2);
}

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    return mergeLinkedListArray(lists, 0, listsSize - 1);
}
