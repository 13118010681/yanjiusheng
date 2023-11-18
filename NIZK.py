# realize fig1
# -*- coding: utf-8 -*-
from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, GT, pair
from newsecretutils import SecretUtil



groupObj = PairingGroup("SS512")
from config import config


def random_scalar():
    return groupObj.random(ZR)


class NIZK():
    # 设置公共参数，群，生成元，要证明的私钥组
    def __init__(self, N):
        self.util = SecretUtil(groupObj, verbose=False)
        self.group = groupObj
        self.g = groupObj.random(G1)
        self.sks = [None] * N
        self.pks = [None] * N
        self.pk = random_scalar()
        self.N=N

    def setPK(self, i, pk):
        self.pks[i] = pk

    def setSK(self, i, sk):
        self.sks[i] = sk

    def hash(self, obj):
        return self.group.hash(str(obj), ZR)

    # 承诺部分
    def prove(self, N):
        self.N = N
        _xs = [None] * N
        for i in range(0, N):
            _xs[i] = random_scalar()
        # print(_xs)
        b = self.g ** _xs[0]
        for i in range(1, N):
            b = b*(self.g ** _xs[i])

        c = self.group.hash(str(self.pk) + str(b), ZR)
        w = [None] * N
        for i in range(0, self.N):
            w[i] = _xs[i] + c * self.sks[i]
        NIZK_proof = {"b": b, "c": c, "w": w}
        return NIZK_proof
    # 验证部分
    def verify(self, proofs):
        left = self.g ** proofs["w"][0]
        for i in range(1, self.N):
            left = left * self.g ** proofs["w"][i]
        right = proofs["b"]*(self.pk ** proofs["c"])
        assert (left == right)
        return True



if __name__ == "__main__":
    N = int(input("输入证明参数个数："))
    nizk = NIZK(N)
    nizk.N = N
    # 随机生成需要验证的N个私钥
    for i in range(0, N):
        nizk.sks[i] = random_scalar()

    for i in range(0, N):
        nizk.pks[i] = nizk.g ** nizk.sks[i]
    # 计算私钥对应的N个公钥
    Y = nizk.pks[0]
    for i in range(1, N):
        Y = Y*nizk.pks[i]
    nizk.pk = Y
    # 生成对应的承诺
    ver_proof = nizk.prove(N)
    # 验证承诺是否正确
    ver_result = nizk.verify(ver_proof)
    if not ver_result:
        print("the verify is false")
    else:
        print("the verify is true")
