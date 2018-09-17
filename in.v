`timescale 1ns/1ps
`celldefine
module V5ISO_AD2D2A (Z, A1, A2);
output Z;
input A1, A2;
`protect

  and (Z, A1, A2);

  specify
    specparam
      tplh$A1$Z = 1.0,
      tphl$A1$Z = 1.0,
      tplh$A2$Z = 1.0,
      tphl$A2$Z = 1.0;

    (A1 *> Z) = (tplh$A1$Z, tphl$A1$Z);
    (A2 *> Z) = (tplh$A2$Z, tphl$A2$Z);
  endspecify
`endprotect

endmodule
`endcelldefine


`timescale 1ns/1ps 
 `celldefine 

module V5ISO_CKXO2D4A (Z, A, B);
output Z;
input A, B;
`protect
  
  xor I0(Z, A, B);
  
  specify
    specparam
      tplh$A$Z = 1.0,
      tphl$A$Z = 1.0,
      tplh$B$Z = 1.0,
      tphl$B$Z = 1.0;

     if (B == 1'b1)
        (A *> Z) = (tplh$A$Z, tphl$A$Z);
     if (B == 1'b0)
        (A *> Z) = (tplh$A$Z, tphl$A$Z);
     if (A == 1'b1)
        (B *> Z) = (tplh$B$Z, tphl$B$Z);
     if (A == 1'b0)
        (B *> Z) = (tplh$B$Z, tphl$B$Z);
  endspecify
`endprotect

endmodule
`endcelldefine


/// Filler Cell ///

`celldefine
module V5ISO_FILL01A();
endmodule
`endcelldefine

`celldefine
module V5ISO_FILL03A();
endmodule
`endcelldefine

`celldefine
module V5ISO_FILL04A();
endmodule
`endcelldefine

`celldefine
module V5ISO_FILL08A();
endmodule
`endcelldefine

`celldefine
module V5ISO_FILL16A();
endmodule
`endcelldefine

`celldefine
module V5ISO_FILL20A();
endmodule
`endcelldefine

`celldefine
module V5ISO_FILL24A();
endmodule
`endcelldefine


/// Decoupling Cap ///
`celldefine
module V5ISO_DCAP04A();
endmodule
`endcelldefine

`celldefine
module V5ISO_DCAP06A();
endmodule
`endcelldefine

`celldefine
module V5ISO_DCAP09A();
endmodule
`endcelldefine

/// Antenna ///

`celldefine
module V5ISO_ANT02A(I);
input I;
endmodule
`endcelldefine


// 
// User Define Primitives 
// 

primitive udp_mux2 (out, in0, in1, sel);
   output out;  
   input  in0, in1, sel;
`protect

   table

// in0 in1  sel :  out
   1  ?   0  :  1 ;
   0  ?   0  :  0 ;
   ?  1   1  :  1 ;
   ?  0   1  :  0 ;
   0  0   ?  :  0 ;  
   1  1   ?  :  1 ;

   endtable
`endprotect
endprimitive




// 
// User Define Primitives 
// 

primitive udp_mux4 (out, in0, in1, in2, in3, sel_0, sel_1);
   output out;  
   input  in0, in1, in2, in3, sel_0, sel_1;
`protect

   table

// in0 in1 in2 in3 sel_0 sel_1 :  out
   0  ?  ?  ?  0  0  :  0;
   1  ?  ?  ?  0  0  :  1;
   ?  0  ?  ?  1  0  :  0;
   ?  1  ?  ?  1  0  :  1;
   ?  ?  0  ?  0  1  :  0;
   ?  ?  1  ?  0  1  :  1;
   ?  ?  ?  0  1  1  :  0;
   ?  ?  ?  1  1  1  :  1;
   0  0  ?  ?  ?  0  :  0;
   1  1  ?  ?  ?  0  :  1;
   ?  ?  0  0  ?  1  :  0;
   ?  ?  1  1  ?  1  :  1;
   0  ?  0  ?  0  ?  :  0;
   1  ?  1  ?  0  ?  :  1;
   ?  0  ?  0  1  ?  :  0;
   ?  1  ?  1  1  ?  :  1;
   1  1  1  1  ?  ?  :  1;  
   0  0  0  0  ?  ?  :  0;

   endtable
`endprotect
endprimitive


