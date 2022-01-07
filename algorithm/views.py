from django.shortcuts import render

from algorithm.forms import sortingForm


def bubbleSort(numbers):
    numbers_len = len(numbers)

    for i in range(numbers_len):
        for j in range(numbers_len - i - 1):
            if numbers[j] > numbers[j + 1]:
               numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def insertionSort(numbers):
    for i in range(1, len(numbers)):
        current_number = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > current_number:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = current_number
    return numbers

def home(request):
    form = sortingForm()
    return render(request, 'home.html', {'form': form})

def processing(request):
    if request.method == 'POST':
        form = sortingForm(request.POST)
        if form.is_valid():
            numbers = form.cleaned_data['numbers']
            algorithm = form.cleaned_data['algorithm']
            if algorithm == 'bubblesort':
                numbers = numbers.split(' ')
                numbers = list(map(int, numbers))
                numbers = bubbleSort(numbers)
                context = {'numbers': numbers}
            elif algorithm == 'insertionsort':
                numbers = numbers.split(' ')
                numbers = list(map(int, numbers))
                numbers = insertionSort(numbers)
                context = {'numbers': numbers}
            else:
                context = {'error': 'Please select an algorithm'}
            
    return render(request, 'processing.html', context)