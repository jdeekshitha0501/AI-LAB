import math 
def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta): 
    if depth == 0 or node_index >= len(values): 
        return values[node_index] 
    if maximizing_player: 
        max_eval = -math.inf 
        for i in range(2):   
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, False, values, alpha, beta) 
            max_eval = max(max_eval, eval) 
            alpha = max(alpha, eval) 
            if beta <= alpha: 
                break  
        return max_eval 
    else: 
        min_eval = math.inf 
        for i in range(2):  
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, True, values, alpha, beta) 
            min_eval = min(min_eval, eval) 
            beta = min(beta, eval) 
            if beta <= alpha: 
                break 
        return min_eval 
if __name__ == "__main__": 
    values = [3, 5, 6, 9, 1, 2, 0, -1] 
    depth = 3 
    optimal_value = alpha_beta_pruning(depth, 0, True, values, -math.inf, math.inf) 
    print(f"The optimal value is: {optimal_value}")