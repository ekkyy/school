print(1)

for i in range(2):
	print(f'kapik papik i {i}')

# aa = []
# # aa = list()
# for i in range(10):
# 	aa.append(i ** 2)

# print(aa)
# # for a in aa:
# # 	print(a)


bb = dict()
for i in range(10):
	bb[i ** 2] = (str(i), str(float(i)))

# print(bb)
# print(bb.items())
# for k, v in bb.items():
# 	print(k, '-', v)





s = 'fDDDbh iv  sjs wr   '
print(s.replace('D', '?').strip().split(' '))



class A:
	w = 1
	q = 0

	def set_q(self, q):
		self.q = q



aa = A()
print(aa.w, aa.q)

aa.set_q(4)
print(aa.w, aa.q)








