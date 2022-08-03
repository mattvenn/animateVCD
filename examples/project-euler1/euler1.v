/* Generated by Yosys 0.17+72 (git sha1 1eb1bc441, clang 10.0.0-4ubuntu1 -fPIC -Os) */

module euler1(clk, rst, result);
  reg \$auto$verilog_backend.cc:2083:dump_module$1  = 0;
  wire \$1 ;
  wire \$11 ;
  wire \$13 ;
  wire [18:0] \$15 ;
  wire [18:0] \$16 ;
  wire [17:0] \$18 ;
  wire [17:0] \$19 ;
  wire [20:0] \$21 ;
  wire [19:0] \$22 ;
  wire [17:0] \$24 ;
  wire \$25 ;
  wire [20:0] \$28 ;
  wire \$3 ;
  wire [4:0] \$5 ;
  wire \$7 ;
  wire [4:0] \$9 ;
  reg [16:0] c3 = 17'h00000;
  reg [16:0] \c3$next ;
  wire c3_lt_1000;
  reg [17:0] c5 = 18'h00000;
  reg [17:0] \c5$next ;
  wire c5_lt_1000;
  input clk;
  wire clk;
  output [18:0] result;
  reg [18:0] result = 19'h00000;
  reg [18:0] \result$next ;
  input rst;
  wire rst;
  reg [4:0] shift5 = 5'h01;
  reg [4:0] \shift5$next ;
  wire v5;
  assign \$9  = shift5 & 3'h7;
  assign \$11  = | \$9 ;
  assign \$13  = c5_lt_1000 & \$11 ;
  assign \$16  = c5 + 3'h5;
  assign \$1  = c3 < 10'h3e8;
  assign \$19  = c3 + 2'h3;
  assign \$22  = result + c3;
  assign \$25  = v5 & c5_lt_1000;
  assign \$24  = \$25  ? c5 : 18'h00000;
  assign \$28  = \$22  + \$24 ;
  always @(posedge clk)
    c5 <= \c5$next ;
  always @(posedge clk)
    c3 <= \c3$next ;
  always @(posedge clk)
    shift5 <= \shift5$next ;
  always @(posedge clk)
    result <= \result$next ;
  assign \$3  = c5 < 10'h3e8;
  assign \$5  = shift5 & 3'h6;
  assign \$7  = | \$5 ;
  always @* begin
    if (\$auto$verilog_backend.cc:2083:dump_module$1 ) begin end
    \c5$next  = c5;
    casez (\$13 )
      1'h1:
          \c5$next  = \$16 [17:0];
    endcase
    casez (rst)
      1'h1:
          \c5$next  = 18'h00000;
    endcase
  end
  always @* begin
    if (\$auto$verilog_backend.cc:2083:dump_module$1 ) begin end
    \c3$next  = c3;
    casez (c3_lt_1000)
      1'h1:
          \c3$next  = \$19 [16:0];
    endcase
    casez (rst)
      1'h1:
          \c3$next  = 17'h00000;
    endcase
  end
  always @* begin
    if (\$auto$verilog_backend.cc:2083:dump_module$1 ) begin end
    \shift5$next  = shift5;
    casez (c3_lt_1000)
      1'h1:
          \shift5$next  = { shift5[3:0], shift5[4] };
    endcase
    casez (rst)
      1'h1:
          \shift5$next  = 5'h01;
    endcase
  end
  always @* begin
    if (\$auto$verilog_backend.cc:2083:dump_module$1 ) begin end
    \result$next  = result;
    casez (c3_lt_1000)
      1'h1:
          \result$next  = \$28 [18:0];
    endcase
    casez (rst)
      1'h1:
          \result$next  = 19'h00000;
    endcase
  end
  assign \$15  = \$16 ;
  assign \$18  = \$19 ;
  assign \$21  = \$28 ;
  assign v5 = \$7 ;
  assign c5_lt_1000 = \$3 ;
  assign c3_lt_1000 = \$1 ;
endmodule
