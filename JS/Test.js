let a = ['a', 'b', 'c', ' ', 'D']

for (i = 0; i < a.length; i++) {
    console.log(/[A-Za-z]/.test(a[i]))
}