npr <- function(n, r) {
    factorial(n) / factorial(n-r)
}

multiply <- function(a,b,c,d,e) {
    a*b*c*d*e
}

case1 <- prod(5,26,10, 9, 8, 20)
case2 <- prod(5,26, 25, 10, 9, 30)
case3 <- prod(5,26, 25, 24,10,20)
case4 <- prod(5,4, 26,25, 10, 30)
case5 <- prod(5,4,3, 26, 10, 20)
case6 <- prod(5,4, 26, 10^2, 30)

total <- sum(case1, case2, case3, case4, case5, case6)
