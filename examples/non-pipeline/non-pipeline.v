//  (ai × bi × ci) + di.
`default_nettype none
module test;
  reg clk = 0;
  reg [7:0] a,b,c,d;
  always #1 clk = !clk;

  initial begin
     $dumpfile("test.vcd");
     $dumpvars(0,test);
     # 1;
     a = 1;
     b = 2;
     c = 3;
     d = 4;
     $display("a * b * c + d = %d", a * b * c + d);

     # 8;
     a = 2;
     b = 3;
     c = 4;
     d = 5;
     $display("a * b * c + d = %d", a * b * c + d);

     # 8;
     a = 3;
     b = 4;
     c = 5;
     d = 6;
     $display("a * b * c + d = %d", a * b * c + d);

     # 100;
     $finish;
  end

  non_pipeline non_pipeline_inst_0 (.clk(clk), .a(a), .b(b), .c(c), .d(d));

endmodule

module non_pipeline(
    input clk,
    input [7:0] a,
    input [7:0] b,
    input [7:0] c,
    input [7:0] d,
    output reg [15:0] out
    );

    reg [7:0] count = 0;
    reg [7:0] ra, rb, rc, rd;
    reg [15:0] stage1;
    reg [15:0] stage2;
    reg [7:0] stage1_c;
    reg [7:0] stage1_d;
    reg [7:0] stage2_d;

    always @(posedge clk) begin
        count <= count + 1;
        ra <= a;
        rb <= b;
        rc <= c;
        rd <= d;
        stage1 <= ra * rb;
        stage1_c <= rc;
        stage1_d <= rd;

        stage2 <= stage1 * stage1_c;
        stage2_d <= stage1_d;

        out <= stage2 + stage2_d;
    end
endmodule
