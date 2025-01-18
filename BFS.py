def bfs(board, tile1_i, tile1_j, tile2_i, tile2_j):
	def backtrace(parent, tile1_i, tile1_j, tile2_i, tile2_j):
		start = (tile1_i, tile1_j, 0, 'noDirection')
		end = None
		for node in parent:
			if node[:2] == (tile2_i, tile2_j): end = node
		path = [end]
		while path[-1] != start:
			path.append(parent[path[-1]])
		path.reverse()
		for p in path:
			p = p[:2]
		return path

	if board[tile1_i][tile1_j] != board[tile2_i][tile2_j]: return []
	n = len(board)
	m = len(board[0])

	import queue
	visited = set()
	visited.add((tile1_i, tile1_j, 0, 'noDirection'))
	parent = {}
	q = queue.Queue()
	q.put((tile1_i, tile1_j, 0, 'noDirection')) # indexI, indexJ, number of turns, direction

	while not q.empty():
		i, j, numTurn, direction = q.get()
		if (i, j) != (tile1_i, tile1_j) and (i, j) == (tile2_i, tile2_j): # founded the way
			return backtrace(parent, tile1_i, tile1_j, tile2_i, tile2_j)
			
		directions = {(i - 1, j) : 'up', (i + 1, j) : 'down', (i, j + 1) : 'right', (i, j - 1) : 'left'}
		for idxI, idxJ in directions:
			nextDirection = directions[(idxI, idxJ)]
			if idxI >= 0 and idxI < n and idxJ >= 0 and idxJ < m and (board[idxI][idxJ] == 0 or (idxI, idxJ) == (tile2_i, tile2_j)):
				if direction == 'noDirection' or (direction == nextDirection and (idxI, idxJ, numTurn, nextDirection) not in visited):
					q.put((idxI, idxJ, numTurn, nextDirection))
					visited.add((idxI, idxJ, numTurn, nextDirection))
					parent[(idxI, idxJ, numTurn, nextDirection)] = (i, j, numTurn, direction)
				elif direction != nextDirection and numTurn < 2 and (idxI, idxJ, numTurn + 1, nextDirection) not in visited:
					q.put((idxI, idxJ, numTurn + 1, nextDirection))
					visited.add((idxI, idxJ, numTurn + 1, nextDirection))
					parent[(idxI, idxJ, numTurn + 1, nextDirection)] = (i, j, numTurn, direction)
	return []