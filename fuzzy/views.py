from django.shortcuts import render
from django.contrib import messages
from .models import TriangularMembership, TrapezoidalMembership, GaussianMembership
import math

def triangular_membership(x, a, b, c):
    """
    Calculate the triangular membership value for a given input x and parameters a, b, c.
    a: left endpoint of the triangle.
    b: peak of the triangle.
    c: right endpoint of the triangle.
    """
    if x <= a or x >= c:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return (c - x) / (c - b)
    else:
        return 0

def trapezoidal_membership(x, a, b, c, d):
    """
    Calculate the trapezoidal membership value for a given input x and parameters a, b, c, d.
    a: left endpoint of the trapezoid.
    b: left shoulder of the trapezoid.
    c: right shoulder of the trapezoid.
    d: right endpoint of the trapezoid.
    """
    if x <= a or x >= d:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1
    elif c < x < d:
        return (d - x) / (d - c)
    else:
        return 0

def gaussian_membership(x, mu, sigma):
    """
    Calculate the Gaussian membership value for a given input x and parameters mean and sigma.
    mean: the center of the Gaussian curve.
    sigma: the standard deviation of the Gaussian curve.
    """
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def home(request):
    return render(request, 'fuzzy/home.html')


def fuzzy_triangular(request):
    tests = TriangularMembership.objects.all()
    context = {
        'tests': tests,
        'membership_function': 'Triangular'
    }

    if request.method == 'POST':
        if all(request.POST.values()):
            new_entry_count = int(request.POST.get('new_entry_count'))
            for i in range(new_entry_count):
                x, a, b, c = (
                    float(request.POST.get(f'entries[{i}][x]')),
                    float(request.POST.get(f'entries[{i}][a]')),
                    float(request.POST.get(f'entries[{i}][b]')),
                    float(request.POST.get(f'entries[{i}][c]'))
                )
                if tests.filter(x=x, a=a, b=b, c=c).exists():
                    messages.warning(request, f'Set of values x={x}, a={a}, b={b}, c={c} already exists.')
                else:
                    membership = triangular_membership(x, a, b, c)
                    triangular = TriangularMembership(x=x, a=a, b=b, c=c, membership=membership)
                    triangular.save()
            else:
                messages.success(request, f'All {new_entry_count} new entries added.')
                return render(request, 'fuzzy/fuzzy_estimator.html', context)
        
        else:
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'fuzzy/fuzzy_estimator.html', context)
    
    return render(request, 'fuzzy/fuzzy_estimator.html', context)


def fuzzy_trapezoidal(request):
    tests = TrapezoidalMembership.objects.all()
    context = {
        'tests': tests,
        'membership_function': 'Trapezoidal'
    }

    if request.method == 'POST':
        if all(request.POST.values()):
            new_entry_count = int(request.POST.get('new_entry_count'))
            for i in range(new_entry_count):
                x, a, b, c, d = (
                    float(request.POST.get(f'entries[{i}][x]')),
                    float(request.POST.get(f'entries[{i}][a]')),
                    float(request.POST.get(f'entries[{i}][b]')),
                    float(request.POST.get(f'entries[{i}][c]')),
                    float(request.POST.get(f'entries[{i}][d]'))
                )
                if tests.filter(x=x, a=a, b=b, c=c).exists():
                    messages.warning(request, f'Set of values x={x}, a={a}, b={b}, c={c}, d={d} already exists.')
                else:
                    membership = trapezoidal_membership(x, a, b, c, d)
                    trapezoidal = TrapezoidalMembership(x=x, a=a, b=b, c=c, d=d, membership=membership)
                    trapezoidal.save()
            else:
                messages.success(request, f'All {new_entry_count} new entries added.')
                return render(request, 'fuzzy/fuzzy_estimator.html', context)
        
        else:
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'fuzzy/fuzzy_estimator.html', context)
            
    return render(request, 'fuzzy/fuzzy_estimator.html', context)


def fuzzy_gaussian(request):
    tests = GaussianMembership.objects.all()
    context = {
        'tests': tests,
        'membership_function': 'Gaussian'
    }

    if request.method == 'POST':
        if all(request.POST.values()):
            new_entry_count = int(request.POST.get('new_entry_count'))
            for i in range(new_entry_count):
                x, mu, sigma = (
                    float(request.POST.get(f'entries[{i}][x]')),
                    float(request.POST.get(f'entries[{i}][mu]')),
                    float(request.POST.get(f'entries[{i}][sigma]')),
                )
                if tests.filter(x=x, mu=mu, sigma=sigma).exists():
                    messages.warning(request, f'Set of values x={x}, a={mu}, sigma={sigma} already exists.')
                else:
                    membership = gaussian_membership(x, mu, sigma)
                    gaussian = GaussianMembership(x=x, mu=mu, sigma=sigma, membership=membership)
                    gaussian.save()
            else:
                messages.success(request, f'All {new_entry_count} new entries added.')
                return render(request, 'fuzzy/fuzzy_estimator.html', context)
        
        else:
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'fuzzy/fuzzy_estimator.html', context)
    
    return render(request, 'fuzzy/fuzzy_estimator.html', context)


def delete_test(request):
    context = {}
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'delete_target_test':
            if not all(request.POST.values()):
                messages.error(request, "Please provide all the required information.")
                return render(request, 'fuzzy/delete_test.html')
            
            membership_function = request.POST.get('membership_function')
            test_value = request.POST.get('test_value')
            if membership_function == 'triangular':
                x = float(test_value)
                target_test = TriangularMembership.objects.filter(x=x).first()
            
            elif membership_function == 'trapezoidal':
                x = float(test_value)
                target_test = TrapezoidalMembership.objects.filter(x=x).first()
            
            elif membership_function == 'gaussian':
                x = float(test_value)
                target_test = GaussianMembership.objects.filter(x=x).first()

            if target_test:
                context['test_exists'] = True
                context['test_to_delete'] = target_test
                context['membership_function'] = membership_function
                return render(request, 'fuzzy/delete_test.html', context)
            else:
                messages.error(request, f"Test with value '{test_value}' not found.")
                return render(request, 'fuzzy/delete_test.html', context)
        
        elif form_type == 'confirm_delete_test':
            target_test = request.POST.get('target_test')
            membership_function = request.POST.get('membership_function')
            if membership_function == 'triangular':
                TriangularMembership.objects.filter(x=target_test).delete()
            elif membership_function == 'trapezoidal':
                TrapezoidalMembership.objects.filter(x=target_test).delete()
            elif membership_function == 'gaussian':
                GaussianMembership.objects.filter(x=target_test).delete()

            messages.success(request, f"Test '{target_test}' has been deleted.")
            return render(request, 'fuzzy/delete_test.html')
            

    return render(request, 'fuzzy/delete_test.html', context)