
from django.shortcuts import render
import datetime

from .models import User



userinformation = []
Test1list = []
Test2list = []
first_text_times = []
final_text_time = []

# Create your views here.

def index(request):
    if request.method == 'POST':
        userinformation.clear()
        final_text_time.clear()
        first_text_times.clear()
        name = request.POST['username']
        age = request.POST['Age']
        gender = request.POST['flexRadioDefault']

        userinformation.append(name)
        userinformation.append(age)
        userinformation.append(gender)
        return render(request, 'intro.html')
    return render(request, 'index.html')


def intro(request):
    if request.method == 'POST':
        choice = request.POST['flexRadioDefault']

        if choice == 'experiment1':
            initial_time = datetime.datetime.now().strftime('%H:%M:%S')
            first_text_times.append(initial_time)

            userinformation.append('TextA and B Enhanced')
            return render(request, 'TextA.html')

        if choice == 'experiment2':
            initial_time = datetime.datetime.now().strftime('%H:%M:%S')
            first_text_times.append(initial_time)

            userinformation.append('TextA Enhanced and Text B')
            return render(request, 'TextAEnhanced.html')

    return render(request, 'intro.html')

def Question1(request):
    if request.method == 'POST':
        Test1list.clear()
        next = request.POST['next']
        print(next)

        if next == 'TextA':
            final_time = datetime.datetime.now().strftime('%H:%M:%S')
            final_text_time.append(final_time)

            Test1list.append(request.POST['option1'])
            Test1list.append(request.POST['option2'])
            Test1list.append(request.POST['option3'])



            return render(request,'TextBEnhanced.html')

        if next == 'TextAEnhanced':
            final_time = datetime.datetime.now().strftime('%H:%M:%S')
            final_text_time.append(final_time)

            Test1list.append(request.POST['option1'])
            Test1list.append(request.POST['option2'])
            Test1list.append(request.POST['option3'])
            return render(request,'TextB.html')

    return render(request, 'Question1.html')

def Question2(request):
    if request.method == 'POST':
        Test2list.clear()
        Test2list.append(request.POST['option1'])
        Test2list.append(request.POST['option2'])

        firt_text = datetime.datetime.strptime(first_text_times[len(first_text_times)-1], '%H:%M:%S') - datetime.datetime.strptime(first_text_times[0], '%H:%M:%S')
        final_text = datetime.datetime.strptime(final_text_time[len(final_text_time)-1], '%H:%M:%S') - datetime.datetime.strptime(final_text_time[0], '%H:%M:%S')

        obj = User.objects.create(name=userinformation[0], age=userinformation[1], gender=userinformation[2], testType=userinformation[len(userinformation)-1],
                                  testAtime=firt_text, question1=Test1list[0], question2=Test1list[1], question3=Test1list[2],
                                  testBtime=final_text, question4=Test2list[0], question5=Test2list[1])

        obj.save()

        userinformation.clear()
        final_text_time.clear()
        first_text_times.clear()
        return render(request,'Thanks.html')
    return render(request, 'Question2.html')

def TextA(request):
    if request.method == 'POST':
        test = request.POST['choice']
        initial_time_2 = datetime.datetime.now().strftime('%H:%M:%S')
        first_text_times.append(initial_time_2)
        return render(request, 'Question1.html', {'test': test})
    return render(request, 'TextA.html')

def TextB(request):
    if request.method == 'POST':
        test = request.POST['choice']
        final_time2 = datetime.datetime.now().strftime('%H:%M:%S')
        final_text_time.append(final_time2)
        return render(request, 'Question2.html', {'test': test})
    return render(request, 'TextB.html')


def TextAEnhanced(request):
    if request.method == 'POST':
        test = request.POST['choice']
        print(test)
        initial_time_2 = datetime.datetime.now().strftime('%H:%M:%S')
        first_text_times.append(initial_time_2)
        return render(request, 'Question1.html', {'test':test})
    return render(request, 'TextAEnhanced.html')


def TextBEnhanced(request):
    if request.method == 'POST':
        final_time2 = datetime.datetime.now().strftime('%H:%M:%S')
        final_text_time.append(final_time2)
        return render(request, 'Question2.html')
    return render(request, 'TextBEnhanced.html')


def Thanks(request):
    return render(request, 'Thanks.html')

def term(request):
    return render(request, 'TermOfUse.html')

