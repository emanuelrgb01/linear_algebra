function back_substitution(A::Array{Float64,2}, b::Array{Float64,1})
  n = length(b)

  for line = n:-1:1
    if abs(A[line, line]) <= 1e-12
      error("Matriz singular")
    end
    S = 0.0
    for column = line+1:1:n
      S = S + A[line, column] * b[column]
    end
    b[line] = (b[line] - S) / A[line, line]
  end
  return b
end

# Example
A = [2 1 1; 0 1 1; 0 0 2.0]
b = [1; 0; 2.0]
x = back_substitution(A, b)
display(x)