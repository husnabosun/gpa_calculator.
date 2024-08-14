from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def value_error(request):
    return render(request, 'error.html')


def low_inyear(request):
    return render(request, 'low_inyear.html')


def low_final(request):
    return render(request, 'low_final.html')


def low_year_end(request):
    return render(request, 'low_year_end.html')


def gpa_result(request):
    try:
        num1 = float(request.GET.get('Quiz1', '').strip())
        num2 = float(request.GET.get('Quiz2', '').strip())
        num3 = float(request.GET.get('SAG', '').strip())
        num4 = float(request.GET.get('Term_exam', '').strip())
        num5 = float(request.GET.get('Quiz1_2', ''). strip())
        num6 = float(request.GET.get('Quiz2_2', '').strip())
        num7 = float(request.GET.get('SAG_2', '').strip())
        num8 = float(request.GET.get('Term_exam_2', '').strip())
        num9 = float(request.GET.get('Final', '').strip())

        if request.GET.get('calculate') == '':
            in_year_score = ((num1+num2)*0.4 + (num5+num6)*0.5) / 2 + ((num4+num8)/2 * 0.6) + (num3+num7)*0.3
            if in_year_score < 60:
                return render(request, 'low_inyear.html')
            elif num9< 50:
                return render(request,'low_final.html', {'in_year_score':in_year_score})
            else:
                res_final = in_year_score * 0.6 + num9 * 0.4
                if res_final > 60:
                    return render(request, 'result.html', {'res_final': res_final})
                else:
                    return render(request, 'low_year_end.html')
    except ValueError:
        return render(request, 'error.html')




