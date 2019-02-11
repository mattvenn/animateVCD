module test;

    reg clk = 0;
    reg [7:0] inst = NOP;

    `include "pipe_defs.vh"

    initial begin
        $dumpfile("test.vcd");
        $dumpvars(0,test);
        # 1
        inst <= MEM1;
        # 2
        inst <= MEM2;
        # 2
        inst <= ADD;
        # 2
        inst <= MULT;
        # 2
        inst <= WRITE;
        # 2
        inst <= NOP;
        # 2
        inst <= NOP;
        # 2
        inst <= NOP;
        # 2
        inst <= MEM1;
        # 2
        inst <= MEM1;
        # 2
        inst <= NOP;
        # 40
        $finish;
    end

    pipeline pipe_0(.clk(clk), .inst(inst));

    /* Make a regular pulsing clock. */
    always #1 clk = !clk;

endmodule // test
