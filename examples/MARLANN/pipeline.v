`default_nettype none
module pipeline (
    input wire clk,
    input wire [7:0] inst
);

    `include "pipe_defs.vh"

    wire memory_1;
    wire memory_2;
    wire add;
    wire mult;
    wire write;

    wire mem_access = memory_1 | memory_2 | write;
    wire [2:0] sum_mem_access = memory_1 + memory_2 + write;
    wire collision = sum_mem_access > 1;

    reg [7:0] inst1 = 0;
    reg [7:0] inst2 = 0;
    reg [7:0] inst3 = 0;
    reg [7:0] inst4 = 0;
    reg [7:0] inst5 = 0;
   
    always @(posedge clk) begin
        inst1 <= inst;
        inst2 <= inst1;
        inst3 <= inst2;
        inst4 <= inst3;
        inst5 <= inst4;

    end

    assign memory_1 = inst1 == MEM1;
    assign memory_2 = inst2 == MEM2;
    assign add      = inst3 == ADD;
    assign mult     = inst4 == MULT;
    assign write    = inst5 == WRITE;

endmodule
