





import java.util.List;
import java.util.ArrayList;

public class iec61131_il_Il_Expression extends il_Simple_Instr, il_Il_Operations {






    private Il_Expr_Operator il_expr_operator;


    public iec61131_il_Il_Expression(
    ) {
        super(
        );
    }



    public Il_Expr_Operator getIl_expr_operator() {
        return il_expr_operator;
    }

    public void setIl_expr_operator(Il_Expr_Operator il_expr_operator) {
        this.il_expr_operator = il_expr_operator;
    }

}