`define NORMAL // normal pipeline operation
//`define COLLIDE_1 // normal pipeline operation
//`define COLLIDE_2 // normal pipeline operation
`default_nettype none
module test;

    reg clk = 0;
    reg [7:0] inst = 1 << NOP;

    `include "pipe_defs.vh"

    initial begin
        $dumpfile("test.vcd");
        $dumpvars(0,test);
    `ifdef NORMAL
        # 2
        inst = 1 << LD_DATA;
        # 2
        inst = 1 << LD_COEFF;
        # 2
        inst = 1 << ADD | 1 << MULT;
        # 2
        inst = 1 << ADD | 1 << MULT;
        # 2
        inst = 1 << ADD | 1 << MULT;
        # 2
        inst = 1 << ADD | 1 << MULT;
        # 2
        inst = 1 << WRITE;
        # 2
        inst = 1 << NOP;
        # 2
    `endif

    `ifdef COLLIDE_1
        # 2
        inst = 1 << LD_COEFF;
        # 2
        inst = 1 << LD_DATA;
        # 2
        inst = 1 << ADD | 1 << MULT;
        # 2
        inst = 1 << NOP;
        # 2
    `endif

    `ifdef COLLIDE_2
        # 2
        inst = 1 << LD_COEFF;
        # 2
        inst = 1 << NOP;
        # 2
        inst = 1 << LD_DATA;
        # 2
        inst = 1 << ADD | 1 << MULT;
        # 2
        inst = 1 << ADD | 1 << MULT;
        # 2
        inst = 1 << WRITE;
        # 2
        inst = 1 << ADD | 1 << MULT;
        # 2
        inst = 1 << ADD | 1 << MULT;
        # 2
        inst = 1 << LD_COEFF;
        # 2
        inst = 1 << NOP;
        # 2
    `endif

        # 40
        $finish;
    end
    pipeline pipe_0(.clk(clk), .inst(inst));

    /* Make a regular pulsing clock. */
    always #1 clk = !clk;

endmodule // test
