import numpy as np


global N
N = 8

def printSolution(board):
	for i in range(N):
		for j in range(N):
			print (board[i][j],end=' ')
		print()


def isSafe(board, row, col):

	# Kiểm tra hàng này ở phía bên trái
	for i in range(col):
		if board[row][i] == 1:
			return False

	# Kiểm tra đường chéo trên ở phía bên trái
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	# Kiểm tra đường chéo dưới bên trái
	for i, j in zip(range(row, N, 1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	return True

def solveNQUtil(board, col):
	# Nếu tất cả các quân hậu được đặt thì trả về true
	if col >= N:
		return True

	# Xem xét cột này và thử đặt quân hậu này vào tất cả các hàng từng hàng một
	for i in range(N):

		if isSafe(board, i, col):
			# Nếu đặt quân hậu tại vị trí [i][col] khả dụng thì thì vị trí [i][col] = 1
			board[i][col] = 1

			# Thử đặt tiếp các con hậu còn lại
			if solveNQUtil(board, col + 1) == True:
				return True

			# Nếu đặt quân hậu tại vị trí [i][col] không được thì thì vị trí [i][col] = 0
			board[i][col] = 0

	# nếu quân hậu không thể được đặt ở bất kỳ hàng nào trong cột này thì trả về false
	return False

# Nó chủ yếu sử dụng giải quyếtNQUtil () để giải quyết vấn đề.
# Nó trả về false nếu không thể đặt các quân hậu, ngược lại trả về true và vị trí các quân hậu ở dạng 1.
# lưu ý rằng có thể có nhiều hơn một giải pháp, hàm này in ra một trong những giải pháp khả thi.
def solveNQ():
	board = np.zeros((N, N), int)

	if solveNQUtil(board, 0) == False:
		print ("Solution does not exist")
		return False

	printSolution(board)
	return True

def main():
	solveNQ()

if __name__ == '__main__':
	main()
