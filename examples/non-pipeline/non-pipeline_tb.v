`default_nettype none
module test;
  reg clk = 0;
  reg start = 0;
  wire busy;
  reg [7:0] a,b,c,d;
  always #1 clk = !clk;

  initial begin
     $dumpfile("test.vcd");
     $dumpvars(0,test);
     # 1;
     a <= 1;
     b <= 2;
     c <= 3;
     d <= 4;
     start <= 1;
     wait(busy);
     start <= 0;
     wait(busy == 0);
     $display("a * b * c + d = %d", a * b * c + d);

     a <= 2;
     b <= 3;
     c <= 4;
     d <= 5;
     start <= 1;
     wait(busy);
     start <= 0;
     wait(busy == 0);
     $display("a * b * c + d = %d", a * b * c + d);

     a <= 3;
     b <= 4;
     c <= 5;
     d <= 6;
     start <= 1;
     wait(busy);
     start <= 0;
     wait(busy == 0);
     $display("a * b * c + d = %d", a * b * c + d);

     # 100;
     $finish;
  end

  non_pipeline non_pipeline_inst_0 (.clk(clk), .a(a), .b(b), .c(c), .d(d), .start(start), .busy(busy));

endmodule

