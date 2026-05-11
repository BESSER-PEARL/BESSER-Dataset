





import java.util.List;
import java.util.ArrayList;

public class core_BinaryExpr extends Expression {

    private String binaryOp;





    private core_Expression core_expression;




    private core_Expression core_expression;


    public core_BinaryExpr(
        String binaryOp    ) {
        super(
        );
        this.binaryOp = binaryOp;
    }


    public String getBinaryop() {
        return binaryOp;
    }

    public void setBinaryop(String binaryOp) {
        this.binaryOp = binaryOp;
    }

    public core_Expression getCore_expression() {
        return core_expression;
    }

    public void setCore_expression(core_Expression core_expression) {
        this.core_expression = core_expression;
    }
    public core_Expression getCore_expression() {
        return core_expression;
    }

    public void setCore_expression(core_Expression core_expression) {
        this.core_expression = core_expression;
    }

}