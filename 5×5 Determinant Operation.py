#Determinant Operation

#Matrix A
print(' Matrix A')
print('A =' + '(a11  a12  a13  a14  a15)')
print('   ' + '(a21  a22  a23  a24  a25)')
print('   ' + '(a31  a32  a33  a34  a35)')
print('   ' + '(a41  a42  a43  a44  a45)')
print('   ' + '(a51  a52  a53  a54  a55)')
print('')

print(' Enter the Variables for Matrix A.')
a11 = float(input('a11: '))
a12 = float(input('a12: '))
a13 = float(input('a13: '))
a14 = float(input('a14: '))
a15 = float(input('a15: '))
a21 = float(input('a21: '))
a22 = float(input('a22: '))
a23 = float(input('a23: '))
a24 = float(input('a24: '))
a25 = float(input('a25: '))
a31 = float(input('a31: '))
a32 = float(input('a32: '))
a33 = float(input('a33: '))
a34 = float(input('a34: '))
a35 = float(input('a35: '))
a41 = float(input('a41: '))
a42 = float(input('a42: '))
a43 = float(input('a43: '))
a44 = float(input('a44: '))
a45 = float(input('a45: '))
a51 = float(input('a51: '))
a52 = float(input('a52: '))
a53 = float(input('a53: '))
a54 = float(input('a54: '))
a55 = float(input('a55: '))
print('')

#Calculations
#Positive Side
A1a = a11 * a22 * a33 * a44 * a53
A5a = a11 * a22 * a35 * a43 * a54
A3b = a11 * a23 * a34 * a42 * a55
A1c = a11 * a24 * a33 * a43 * a55
A5c = a11 * a24 * a35 * a42 * a54
A3d = a11 * a25 * a33 * a42 * a54
A4a = a11 * a22 * a34 * a45 * a53
A2b = a11 * a23 * a32 * a45 * a54
A6b = a11 * a23 * a35 * a44 * a52
A4c = a11 * a24 * a33 * a45 * a52
A2d = a11 * a25 * a32 * a44 * a53
A6d = a11 * a25 * a34 * a43 * a52
B2a = a12 * a21 * a33 * a45 * a54
B6a = a12 * a21 * a35 * a44 * a53
B4b = a12 * a23 * a34 * a45 * a51
B2c = a12 * a24 * a31 * a45 * a53
B6c = a12 * a24 * a35 * a43 * a51
B4d = a12 * a25 * a33 * a44 * a51
B3a = a12 * a21 * a34 * a45 * a55
B1b = a12 * a23 * a31 * a44 * a55
B5b = a12 * a23 * a35 * a41 * a54
B3c = a12 * a24 * a33 * a41 * a53
B1d = a12 * a25 * a31 * a43 * a54
B5d = a12 * a25 * a34 * a41 * a53
C1a = a13 * a21 * a32 * a44 * a55
C5a = a13 * a21 * a35 * a42 * a54
C3b = a13 * a22 * a34 * a41 * a55
C1c = a13 * a24 * a31 * a42 * a55
C5c = a13 * a24 * a35 * a41 * a52
C3d = a13 * a25 * a32 * a41 * a54
C4a = a13 * a21 * a34 * a45 * a52
C2b = a13 * a22 * a35 * a44 * a54
C6b = a13 * a22 * a35 * a44 * a51
C4c = a13 * a24 * a32 * a45 * a51
C2d = a13 * a25 * a31 * a44 * a55
C6d = a13 * a25 * a34 * a42 * a51
D2a = a14 * a21 * a32 * a45 * a53
D6a = a14 * a21 * a35 * a43 * a52
D4b = a14 * a22 * a33 * a45 * a51
D2c = a14 * a23 * a31 * a45 * a52
D6c = a14 * a23 * a35 * a42 * a51
D4d = a14 * a25 * a32 * a43 * a51
D3a = a14 * a21 * a33 * a42 * a55
D1b = a14 * a22 * a31 * a43 * a55
D5b = a14 * a22 * a35 * a41 * a53
D3c = a14 * a23 * a32 * a41 * a55
D1d = a14 * a25 * a31 * a42 * a53
D5d = a14 * a25 * a33 * a41 * a52
E1a = a15 * a21 * a32 * a43 * a54
E5a = a15 * a21 * a34 * a42 * a53
E3b = a15 * a22 * a33 * a41 * a54
E1c = a15 * a23 * a31 * a42 * a54
E5c = a15 * a23 * a34 * a41 * a52
E3d = a15 * a24 * a32 * a41 * a53
E4a = a15 * a21 * a33 * a44 * a52
E2b = a15 * a22 * a31 * a44 * a53
E6b = a15 * a22 * a34 * a43 * a53
E4c = a15 * a23 * a32 * a44 * a51
E2d = a15 * a24 * a31 * a45 * a52
E6d = a15 * a24 * a33 * a42 * a51

#Negative Side
A2a = a11 * a22 * a33 * a45 * a54
A6a = a11 * a22 * a35 * a44 * a53
A4b = a11 * a23 * a34 * a45 * a52
A2c = a11 * a24 * a32 * a45 * a53
A6c = a11 * a24 * a35 * a43 * a52
A4d = a11 * a25 * a33 * a44 * a52
A3a = a11 * a22 * a34 * a43 * a55
A1b = a11 * a23 * a32 * a44 * a53
A5b = a11 * a23 * a35 * a42 * a54
A3c = a11 * a24 * a33 * a42 * a55
A1d = a11 * a25 * a32 * a43 * a54
A5d = a11 * a25 * a34 * a42 * a53
B1a = a12 * a21 * a33 * a44 * a55
B5a = a12 * a21 * a35 * a43 * a54
B3b = a12 * a23 * a34 * a43 * a55
B1c = a12 * a24 * a31 * a43 * a55
B5c = a12 * a24 * a35 * a41 * a53
B3d = a12 * a25 * a33 * a41 * a54
B4a = a12 * a21 * a34 * a45 * a53
B2b = a12 * a23 * a31 * a45 * a54
B6b = a12 * a23 * a35 * a44 * a51
B4c = a12 * a24 * a33 * a45 * a51
B2d = a12 * a25 * a31 * a44 * a53
B6d = a12 * a25 * a34 * a43 * a51
C2a = a13 * a21 * a32 * a45 * a54
C6a = a13 * a21 * a35 * a44 * a52
C4b = a13 * a22 * a34 * a45 * a51
C2c = a13 * a24 * a31 * a45 * a52
C6c = a13 * a24 * a35 * a42 * a51
C4d = a13 * a25 * a32 * a44 * a51
C3a = a13 * a21 * a34 * a42 * a55
C1b = a13 * a22 * a31 * a44 * a55
C5b = a13 * a22 * a31 * a44 * a55
C3c = a13 * a24 * a32 * a41 * a55
C1d = a13 * a25 * a31 * a42 * a54
C5d = a13 * a25 * a34 * a41 * a55
D1a = a14 * a21 * a32 * a43 * a55
D5a = a14 * a21 * a35 * a42 * a52
D3b = a14 * a22 * a33 * a41 * a52
D1c = a14 * a23 * a31 * a42 * a55
D5c = a14 * a23 * a35 * a41 * a52
D3d = a14 * a25 * a32 * a41 * a53
D4a = a14 * a21 * a33 * a45 * a52
D2b = a14 * a22 * a31 * a45 * a53
D6b = a14 * a22 * a35 * a43 * a51
D4c = a14 * a23 * a32 * a45 * a51
D2d = a14 * a25 * a31 * a43 * a52
D6d = a14 * a25 * a33 * a42 * a51
E2a = a15 * a21 * a32 * a44 * a53
E6a = a15 * a21 * a34 * a43 * a52
E4b = a15 * a22 * a33 * a44 * a51
E2c = a15 * a23 * a31 * a44 * a52
E6c = a15 * a23 * a34 * a42 * a51
E4d = a15 * a24 * a32 * a43 * a51
E3a = a15 * a21 * a33 * a42 * a54
E1b = a15 * a22 * a31 * a43 * a54
E5b = a15 * a22 * a34 * a41 * a52
E3c = a15 * a23 * a32 * a41 * a54
E1d = a15 * a24 * a31 * a42 * a53
E5d = a15 * a24 * a33 * a41 * a52

Y = A1a + A5a + A3b + A1c + A5c + A3d + A4a + A2b + A6b + A4c + A2d + A6d + B2a + B6a + B4b + B2c + B6c + B4d + B3a + B1b + B5b + B3c + B1d + B5d + C1a + C5a + C3b + C1c + C5c + C3d + C4a + C2b + C6b + C4c + C2d + C6d + D2a + D6a + D4b + D2c + D6c + D4d + D3a + D1b + D5b + D3c + D1d + D5d + E1a + E5a + E3b + E1c + E5c + E3d + E4a + E2b + E6b + E4c + E2d + E6d
Z = A2a + A6a + A4b + A2c + A6c + A4d + A3a + A1b + A5b + A3c + A1d + A5d + B1a + B5a + B3b + B1c + B5c + B3d + B4a + B2b + B6b + B4c + B2d + B6d + C2a + C6a + C4b + C2c + C6c + C4d + C3a + C1b + C5b + C3c + C1d + C5d + D1a + D5a + D3b + D1c + D5c + D3d + D4a + D2b + D6b + D4c + D2d + D6d + E2a + E6a + E4b + E2c + E6c + E4d + E3a + E1b + E5b + E3c + E1d + E5d
D = Y - Z

print(' The Determinant of the Matrix A is ' + str(D))
print('')
