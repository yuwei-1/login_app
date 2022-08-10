
class SHA2:

    def __init__(self, password=None):
        self.password = password
        self.final_bin = None
        self.w_values = None
        self.working_variables = ['6a09e667',
                                  'bb67ae85',
                                  '3c6ef372',
                                  'a54ff53a',
                                  '510e527f',
                                  '9b05688c',
                                  '1f83d9ab',
                                  '5be0cd19']

        self.k_values = "428a2f98 71374491 b5c0fbcf e9b5dba5\
 3956c25b 59f111f1 923f82a4 ab1c5ed5\
 d807aa98 12835b01 243185be 550c7dc3\
 72be5d74 80deb1fe 9bdc06a7 c19bf174\
 e49b69c1 efbe4786 0fc19dc6 240ca1cc\
 2de92c6f 4a7484aa 5cb0a9dc 76f988da\
 983e5152 a831c66d b00327c8 bf597fc7\
 c6e00bf3 d5a79147 06ca6351 14292967\
 27b70a85 2e1b2138 4d2c6dfc 53380d13\
 650a7354 766a0abb 81c2c92e 92722c85\
 a2bfe8a1 a81a664b c24b8b70 c76c51a3\
 d192e819 d6990624 f40e3585 106aa070\
 19a4c116 1e376c08 2748774c 34b0bcb5\
 391c0cb3 4ed8aa4a 5b9cca4f 682e6ff3\
 748f82ee 78a5636f 84c87814 8cc70208\
 90befffa a4506ceb bef9a3f7 c67178f2".split(" ")

        self.bit_limit = 4294967296

    def encrypt(self):

        self.binary_conversion()
        self.create_w_values()
        self.initialize_w_values()

        return self.SHA2_rounds()

    def binary_conversion(self):

        pw = [bin(ord(char))[2:] for char in list(self.password)]
        pw = ''.join([(8 - len(b)) * '0' + b for b in pw])

        bin_len = len(pw)
        msg_len = bin(bin_len)[2:]
        bin_len += len(msg_len)

        padding_len = 511 - bin_len

        final_bin = pw + '1' + padding_len * '0' + msg_len

        self.final_bin = final_bin

    def SHA2_rounds(self):

        iwv = wv = [self.hex_to_bin(hex) for hex in self.working_variables]

        for round in range(64):

            maj_result = self.maj(wv[0], wv[1], wv[2])
            sigma0_result = self.Sigma_0(wv[0])
            sigma1_result = self.Sigma_1(wv[4])
            condition_result = self.conditional_func(wv[4], wv[5], wv[6])

            right_operation = self.modular_addition(self.modular_addition(condition_result, wv[-1]), sigma1_result)
            right_operation = self.modular_addition(self.modular_addition(right_operation, self.w_values[round]), self.hex_to_bin(self.k_values[round]))
            mid_operation = self.modular_addition(wv[3], right_operation)
            left_operation = self.modular_addition(self.modular_addition(sigma0_result, maj_result), right_operation)

            wv = [left_operation, wv[0], wv[1], wv[2], mid_operation, wv[4], wv[5], wv[6]]

        final_H_values = [self.bin_to_hex(self.modular_addition(wv[i], iwv[i])) for i in range(8)]

        return ''.join(final_H_values)

    def create_w_values(self):

        w_values = []

        for i in range(16):

            w_values.append(self.final_bin[32*i:32*i + 32])

        self.w_values = w_values

    def initialize_w_values(self):

        for w in range(16, 64):

            W_1 = self.sigma_1(self.w_values[w - 2])
            W_2 = self.w_values[w - 7]
            W_3 = self.sigma_0(self.w_values[w - 15])
            W_4 = self.w_values[w - 16]

            W = self.modular_addition(self.modular_addition(self.modular_addition(W_1, W_2), W_3), W_4)

            self.w_values.append(W)

    @staticmethod
    def padding(binary):
        padding_len = 32 - len(binary)
        return '0' * padding_len + binary

    def hex_to_bin(self, hexadecimal):

        return self.padding(bin(int(hexadecimal, 16))[2:])

    def bin_to_hex(self, binary):

        hexa = hex(int(binary, 2))[2:]
        return (8 - len(hexa)) * '0' + hexa

    @staticmethod
    def ROTR(binary, shift):
        return binary[-shift:] + binary[:-shift]

    @staticmethod
    def SHR(binary, shift):
        return ('0' * shift + binary)[:32]

    @staticmethod
    def XOR(b1, b2):

        b3 = ''
        for b in range(32):
            if b1[b] == b2[b]:
                b3 += '0'
            else:
                b3 += '1'

        return b3

    def modular_addition(self, b1, b2):

        b1 = int(b1, 2)
        b2 = int(b2, 2)

        return self.padding(bin((b1 + b2) % self.bit_limit)[2:])

    @staticmethod
    def AND(b1, b2):

        b3 = ''
        for b in range(32):
            if b1[b] == b2[b] and b1[b] == '1':
                b3 += '1'
            else:
                b3 += '0'

        return b3

    @staticmethod
    def NOT(binary):
        b1 = ''
        for b in range(32):
            if binary[b] == '1':
                b1 += '0'
            else:
                b1 += '1'
        return b1

    def sigma_1(self, binary):

        first_component = self.ROTR(binary, 17)
        second_component = self.ROTR(binary, 19)
        third_component = self.SHR(binary, 10)

        return self.XOR(self.XOR(first_component, second_component), third_component)

    def sigma_0(self, binary):

        first_component = self.ROTR(binary, 7)
        second_component = self.ROTR(binary, 18)
        third_component = self.SHR(binary, 3)

        return self.XOR(self.XOR(first_component, second_component), third_component)

    def maj(self, a, b, c):

        first_component = self.AND(a, b)
        second_component = self.AND(a, c)
        third_component = self.AND(b, c)

        return self.XOR(self.XOR(first_component, second_component), third_component)

    def Sigma_0(self, binary):

        first_component = self.ROTR(binary, 2)
        second_component = self.ROTR(binary, 13)
        third_component = self.ROTR(binary, 22)

        return self.XOR(self.XOR(first_component, second_component), third_component)

    def Sigma_1(self, binary):

        first_component = self.ROTR(binary, 6)
        second_component = self.ROTR(binary, 11)
        third_component = self.ROTR(binary, 25)

        return self.XOR(self.XOR(first_component, second_component), third_component)

    def conditional_func(self, e, f, g):

        first_component = self.AND(e, f)
        second_component = self.AND(self.NOT(e), g)

        return self.XOR(first_component, second_component)
