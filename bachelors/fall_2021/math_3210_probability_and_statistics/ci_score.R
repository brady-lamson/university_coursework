n <- 143
p_hat <- 10/143
q_hat <- 1 - p_hat
z <- 1.64
p_tilde <- (p_hat + (z^2/(2*n))) / (1+(z^2/n))

score <- p_tilde - (z * sqrt((p_hat*q_hat/n) + z/(4*(n^2))) / (1 + (z/n)))
print(score)
