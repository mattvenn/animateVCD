//  (ai × bi × ci) + di.
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
     a = 1;
     b = 2;
     c = 3;
     d = 4;
     start = 1;
     wait(busy);
     start = 0;
     wait(busy == 0)
     $display("a * b * c + d = %d", a * b * c + d);

     a = 2;
     b = 3;
     c = 4;
     d = 5;
     start = 1;
     wait(busy);
     start = 0;
     wait(busy == 0)
     $display("a * b * c + d = %d", a * b * c + d);

     a = 3;
     b = 4;
     c = 5;
     d = 6;
     start = 1;
     wait(busy);
     start = 0;
     wait(busy == 0)
     $display("a * b * c + d = %d", a * b * c + d);

     # 100;
     $finish;
  end

  non_pipeline non_pipeline_inst_0 (.clk(clk), .a(a), .b(b), .c(c), .d(d), .start(start), .busy(busy));

endmodule

module non_pipeline(
    input clk,
    input [7:0] a,
    input [7:0] b,
    input [7:0] c,
    input [7:0] d,
    input start,
    output busy,
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
    end

    reg [1:0] process = 0; // keep track of where we are in the calculation
    reg run = 0;
    assign busy = run;

    always @(posedge clk) begin
        // always capture the inputs, controller mustn't change till busy goes low
        ra <= a;
        rb <= b;
        rc <= c;
        rd <= d;

        if(run) begin
            case(process)
                0: stage1 <= ra * rb;
                1: stage2 <= stage1 * rc;
                2: begin out <= stage2 + rd; run <= 0; end
            endcase
            process <= process + 1;
        end else if (start) begin
            process <= 0;
            run <= 1;
        end
    end
endmodule
