





import java.util.List;
import java.util.ArrayList;

public class dsl_PostfixExpression  {

    private String op;





    private dsl_PrimaryExpression dsl_primaryexpression;




    private dsl_UnaryExpressionNotPlusMinus dsl_unaryexpressionnotplusminus;


    public dsl_PostfixExpression(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public dsl_PrimaryExpression getDsl_primaryexpression() {
        return dsl_primaryexpression;
    }

    public void setDsl_primaryexpression(dsl_PrimaryExpression dsl_primaryexpression) {
        this.dsl_primaryexpression = dsl_primaryexpression;
    }
    public dsl_UnaryExpressionNotPlusMinus getDsl_unaryexpressionnotplusminus() {
        return dsl_unaryexpressionnotplusminus;
    }

    public void setDsl_unaryexpressionnotplusminus(dsl_UnaryExpressionNotPlusMinus dsl_unaryexpressionnotplusminus) {
        this.dsl_unaryexpressionnotplusminus = dsl_unaryexpressionnotplusminus;
    }

}