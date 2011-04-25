"""
Problem Statement:
    http://code.google.com/codejam/contest/dashboard?c=837485#

Tip - During the first read of the problem statement, it is helpful to
understand the problem using the TestCases which are provided.

"""
N = int(raw_input())
for tc in range(1,N+1):
    S = int(raw_input())
    segments = raw_input().split()
    R = []
    B = []
    for segment in segments:
        if segment.endswith('B'):
            B.append(int(segment[:-1]))
        if segment.endswith('R'):
            R.append(int(segment[:-1]))

    if (S == 1) or (not R or not B):
        print 'Case #%d: %d' %(tc, 0)
        continue
    R.sort(reverse=True)
    B.sort(reverse=True)
    if len(R) < len(B):
        R = R
        B = B[:len(R)]
    if len(B) < len(R):
        B = B
        R = R[:len(B)]

    result = sum(R+B) - len(R+B)
    print 'Case #%d: %d' % (tc, result)
