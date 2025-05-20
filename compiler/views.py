from django.shortcuts import render
import sys
import io

def run_code(code, user_input):
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    redirected_output = sys.stdout = io.StringIO()
    sys.stdin = io.StringIO(user_input)

    try:
        exec(code, {})
        output = redirected_output.getvalue().strip()
    except Exception as e:
        output = str(e)

    sys.stdout = old_stdout
    sys.stdin = old_stdin
    return output

def home(request):
    code = ''
    input1 = input2 = expected1 = expected2 = ''
    results = []

    if request.method == 'POST':
        code = request.POST.get('code')
        input1 = request.POST.get('input1')
        expected1 = request.POST.get('expected1').strip()
        input2 = request.POST.get('input2')
        expected2 = request.POST.get('expected2').strip()

        # Run test case 1
        output1 = run_code(code, input1)
        result1 = "PASS ✅" if output1 == expected1 else f"FAIL ❌ (Got: {output1})"
        results.append(result1)

        # Run test case 2
        output2 = run_code(code, input2)
        result2 = "PASS ✅" if output2 == expected2 else f"FAIL ❌ (Got: {output2})"
        results.append(result2)

    return render(request, 'compiler/home.html', {
        'code': code,
        'input1': input1,
        'expected1': expected1,
        'input2': input2,
        'expected2': expected2,
        'results': results
    })
