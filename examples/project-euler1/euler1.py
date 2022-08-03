import sys
from amaranth import *
from amaranth.sim import *
from amaranth.back import verilog


class Euler1(Elaboratable):
    def __init__(self):
        self.result = Signal(19)

    def elaborate(self, platform):
        m = Module()

        shift5 = Signal(5,reset=1)
        c3 = Signal(17)
        c5 = Signal(18)
        c3_lt_1000 = Signal()
        c5_lt_1000 = Signal()
        v5 = Signal()

        m.d.comb += [c3_lt_1000.eq(c3<1000), c5_lt_1000.eq(c5<1000)]
        m.d.comb += v5.eq((shift5&0b110) != 0)

        with m.If((c5_lt_1000) & ((shift5&0b00111) != 0)): 
            m.d.sync+=c5.eq(c5 + 5)

        with m.If(c3_lt_1000):
            m.d.sync += c3.eq(c3 + 3)
            m.d.sync += shift5.eq(Cat(shift5[-1], shift5[:-1]))
            m.d.sync += self.result.eq(self.result + c3 + Mux(v5 & c5_lt_1000, c5, 0))

        return m


def sim():
    d = Euler1()
    sim = Simulator(d)

    def proc():
        for i in range(1000):
            yield
            result = yield d.result
            print(i, result)

    with sim.write_vcd("euler1.vcd", "euler1.gtkw"):
        #sim.add_clock(5e-5)
        sim.add_clock(5e-12)
        sim.add_sync_process(proc)
        sim.run()


def gen():
    d = Euler1()
    ports = [d.result]
    print(verilog.convert(d, name="euler1", ports=ports, strip_internal_attrs=True))


if __name__ == "__main__":
    if len(sys.argv) < 2 or not(sys.argv[1] in ["sim", "gen"]):
        print("usage %s <sim|gen>" % sys.argv[0])
    else:
        if sys.argv[1] == "sim":
            sim()
        if sys.argv[1] == "gen":
            gen()
