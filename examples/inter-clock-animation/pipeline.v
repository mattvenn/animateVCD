//  (ai × bi × ci) + di.
`default_nettype none
module test;
  reg clk = 0;
  reg clk2 = 0;
    reg [7:0] count = 0;
  reg [7:0] inst = 1;
  always #1 clk = !clk;
  always #2 clk2 = !clk2;

  initial begin
     $dumpfile("test.vcd");
     $dumpvars(0,test);
     inst = 1;
     # 4;
     inst <= 2;
     # 4;
     inst <= 4;
     # 4;
     inst <= 8;
     # 4;
     inst <= 16;

     # 100;
     $finish;
  end
    always @(posedge clk2)
        count <= count + 1;

  pipeline pipeline_inst_0 (.clk(clk), .clk2(clk2), .inst(inst));

endmodule

module pipeline(
    input clk,
    input clk2,
    input [7:0] inst
    );

    reg [7:0] stage0;
    reg [7:0] stage0_1;
    reg [7:0] stage1;
    reg [7:0] stage1_2;
    reg [7:0] stage2;
    reg [7:0] stage2_3;
    reg [7:0] stage3;
    reg [7:0] stage3_4;

    wire stage0_show = (stage0 > 0) & !clk2;
    wire stage0_arrow = (stage0 > 0) & clk & !clk2;

    wire stage1_show = (stage0 > 0) & clk2;
    wire stage1_arrow = (stage1 > 0) & clk & clk2;

    wire stage1_2_show = (stage1 >0) & !clk2;
    wire stage1_2_arrow = (stage1 >0) & clk & !clk2;



    always @(posedge clk) begin

        stage0 <= inst;

        stage1 <= stage0;

        stage1_2 <= stage1;

        stage2 <= stage1_2;

        stage2_3 <= stage2;

        stage3 <= stage2_3;

        stage3_4 <= stage3;


    end
endmodule
