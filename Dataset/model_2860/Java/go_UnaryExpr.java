





import java.util.List;
import java.util.ArrayList;

public class go_UnaryExpr  {

    private String unary_op;





    private go_Expression go_expression;




    private go_UnaryExpr go_unaryexpr;




    private go_PrimaryExpr go_primaryexpr;


    public go_UnaryExpr(
        String unary_op    ) {
        this.unary_op = unary_op;
    }


    public String getUnary_op() {
        return unary_op;
    }

    public void setUnary_op(String unary_op) {
        this.unary_op = unary_op;
    }

    public go_Expression getGo_expression() {
        return go_expression;
    }

    public void setGo_expression(go_Expression go_expression) {
        this.go_expression = go_expression;
    }
    public go_UnaryExpr getGo_unaryexpr() {
        return go_unaryexpr;
    }

    public void setGo_unaryexpr(go_UnaryExpr go_unaryexpr) {
        this.go_unaryexpr = go_unaryexpr;
    }
    public go_PrimaryExpr getGo_primaryexpr() {
        return go_primaryexpr;
    }

    public void setGo_primaryexpr(go_PrimaryExpr go_primaryexpr) {
        this.go_primaryexpr = go_primaryexpr;
    }

}