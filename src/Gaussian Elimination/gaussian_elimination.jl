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


function gaussian_elimination(A::Array{Float64,2}, b::Array{Float64,1})
  n = length(b)
  for step = 1:1:n-1
    if abs(A[step, step]) <= 1e-12
      error("Erro")
    end
    for line = step+1:1:n
      m = A[line, step]/A[step, step]
      A[line, step] = 0
      b[line] = b[line] - m*b[step]
      for column = step+1:1:n
        A[line, column] = A[line, column] - m*A[step, column]
      end
    end
  end
  return back_substitution(A, b)
end

# Example
A = [2 1 1; 4 3 3; 8 7 9.0]
b = [1; 2; 6.0]
x = gaussian_elimination(A, b)

display(x)