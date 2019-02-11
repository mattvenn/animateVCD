`default_nettype none
module pipeline (
    input wire clk,
    input wire [7:0] inst
);

    `include "pipe_defs.vh"

    wire load_data;
    wire load_coeff;
    wire add;
    wire mult;
    wire write;

    wire mem_access = load_data | load_coeff | write;
    wire [2:0] sum_mem_access = load_data + load_coeff + write;
    wire collision = sum_mem_access > 1;

    reg [7:0] count = 0;

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
    
        count <= count + 1;
    end

    assign load_data  = inst1[LD_DATA];
    assign load_coeff = inst2[LD_COEFF];
    assign mult       = inst3[MULT];
    assign add        = inst4[ADD];
    assign write      = inst5[WRITE];

endmodule
