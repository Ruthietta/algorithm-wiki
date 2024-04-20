#include <cstdlib>
#include <ctime>
#include <iostream>

const int arrSize = 50;
int operationNumber = 0;

int partition(int arr[], int start, int end) {
  int pivot = arr[start];

  int count = 0;
  for (int i = start + 1; i <= end; i++) {
    operationNumber++;
    if (arr[i] <= pivot) count++;
  }

  int pivotIndex = start + count;
  std::swap(arr[pivotIndex], arr[start]);

  int i = start, j = end;

  while (i < pivotIndex && j > pivotIndex) {
    while (arr[i] <= pivot) {
      i++;
      operationNumber++;
    }

    while (arr[j] > pivot) {
      j--;
      operationNumber++;
    }

    if (i < pivotIndex && j > pivotIndex) {
      std::swap(arr[i++], arr[j--]);
      operationNumber++;
    }
  }

  return pivotIndex;
}

void quickSortHelper(int arr[], int start, int end) {
  if (start >= end) return;

  int p = partition(arr, start, end);

  quickSortHelper(arr, start, p - 1);
  quickSortHelper(arr, p + 1, end);
}

int* quickSort(int arr[]) {
  int* sortedArr = new int[arrSize];
  for (int i = 0; i < arrSize; ++i) sortedArr[i] = arr[i];

  operationNumber = 0;
  quickSortHelper(sortedArr, 0, arrSize - 1);

  return sortedArr;
}

int main() {
  int arr[arrSize];

  srand(time(nullptr));
  for (int i = 0; i < arrSize; ++i) arr[i] = rand() % 100;

  int* sortedArr = quickSort(arr);

  std::cout << "\n\tRandom array:\n";
  for (int i = 0; i < arrSize; i++) std::cout << arr[i] << " ";

  std::cout << "\n\tSorted array:\n";
  for (int i = 0; i < arrSize; i++) std::cout << sortedArr[i] << " ";

  std::cout << "\n\tReversed array:\n";
  for (int i = arrSize - 1; i >= 0; i--) std::cout << sortedArr[i] << " ";

  std::cout << "\n\tNumber of operations done: " << operationNumber
            << std::endl;

  delete[] sortedArr;
  return 0;
}
