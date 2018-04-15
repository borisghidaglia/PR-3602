def null_heuristic(a_star, node):
    return 0


def weighted_min(a_star, node):
    available_agents = a_star.agents - node.attributed_agents
    if not available_agents:
        return 0
    node_job = node.job
    val_min = float('inf')
    for job in range(node_job+1, a_star.cost_matrix.shape[0]):
        for agent in available_agents:
            val_min = min(val_min, a_star.cost_matrix[job][agent])
    return val_min*len(available_agents)


def sum_min_by_rows(a_star, node):
    available_agents = a_star.agents - node.attributed_agents
    if not available_agents:
        return 0
    node_job = node.job
    val_heuristic = 0
    for job in range(node_job+1, a_star.cost_matrix.shape[0]):
        val_min = float('inf')
        for agent in available_agents:
            val_min = min(val_min, a_star.cost_matrix[job][agent])
        val_heuristic += val_min
    return val_heuristic


def sum_min_by_cols(a_star, node):
    available_agents = a_star.agents - node.attributed_agents
    if not available_agents:
        return 0
    node_job = node.job
    val_heuristic = 0
    for agent in available_agents:
        val_min = float('inf')
        for job in range(node_job+1, a_star.cost_matrix.shape[0]):
            val_min = min(val_min, a_star.cost_matrix[job][agent])
        val_heuristic += val_min
    return val_heuristic


def max_sum_min_by_r_and_c(a_star, node):
    return max(
        sum_min_by_rows(a_star, node),
        sum_min_by_cols(a_star, node)
        )
