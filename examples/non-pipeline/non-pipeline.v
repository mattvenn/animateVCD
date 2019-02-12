//  (ai × bi × ci) + di.
`default_nettype none
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
    reg [15:0] stage1;
    reg [15:0] stage2;

    always @(posedge clk) begin
        count <= count + 1;
    end

    reg [1:0] process = 0; // keep track of where we are in the calculation

    // controller mustn't change inputs till busy goes low
    assign busy = (process > 0);

    always @(posedge clk) begin
        if(start | busy) begin
            case(process)
                0: begin stage1 <= a * b; process <= process + 1; end
                1: begin stage2 <= stage1 * c; process <= process + 1; end
                2: begin out <= stage2 + d; process <= 0; end
            endcase
        end
    end
endmodule
