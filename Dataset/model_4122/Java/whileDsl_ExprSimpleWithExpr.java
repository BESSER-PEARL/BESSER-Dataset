





import java.util.List;
import java.util.ArrayList;

public class whileDsl_ExprSimpleWithExpr  {

    private String operation;





    private whileDsl_Expr whiledsl_expr;


    public whileDsl_ExprSimpleWithExpr(
        String operation    ) {
        this.operation = operation;
    }


    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public whileDsl_Expr getWhiledsl_expr() {
        return whiledsl_expr;
    }

    public void setWhiledsl_expr(whileDsl_Expr whiledsl_expr) {
        this.whiledsl_expr = whiledsl_expr;
    }

}