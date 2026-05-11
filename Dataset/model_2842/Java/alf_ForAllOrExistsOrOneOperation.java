





import java.util.List;
import java.util.ArrayList;

public class alf_ForAllOrExistsOrOneOperation extends SequenceExpansionExpression {

    private String expr3;
    private String expr2;
    private String op;
    private String expr1;
    private String expr4;



    public alf_ForAllOrExistsOrOneOperation(
        String expr3,        String expr2,        String op,        String expr1,        String expr4    ) {
        super(
        );
        this.expr3 = expr3;
        this.expr2 = expr2;
        this.op = op;
        this.expr1 = expr1;
        this.expr4 = expr4;
    }


    public String getExpr3() {
        return expr3;
    }

    public void setExpr3(String expr3) {
        this.expr3 = expr3;
    }
    public String getExpr2() {
        return expr2;
    }

    public void setExpr2(String expr2) {
        this.expr2 = expr2;
    }
    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public String getExpr1() {
        return expr1;
    }

    public void setExpr1(String expr1) {
        this.expr1 = expr1;
    }
    public String getExpr4() {
        return expr4;
    }

    public void setExpr4(String expr4) {
        this.expr4 = expr4;
    }


}