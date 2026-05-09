





import java.util.List;
import java.util.ArrayList;

public class dsl_StatementExpression  {

    private String assignOp;
    private String minOp;
    private String plusOp;





    private dsl_Statement dsl_statement;




    private dsl_PreIncrementExpression dsl_preincrementexpression;




    private dsl_PreDecrementExpression dsl_predecrementexpression;




    private dsl_Expression dsl_expression;




    private dsl_PrimaryExpression dsl_primaryexpression;


    public dsl_StatementExpression(
        String assignOp,        String minOp,        String plusOp    ) {
        this.assignOp = assignOp;
        this.minOp = minOp;
        this.plusOp = plusOp;
    }


    public String getAssignop() {
        return assignOp;
    }

    public void setAssignop(String assignOp) {
        this.assignOp = assignOp;
    }
    public String getMinop() {
        return minOp;
    }

    public void setMinop(String minOp) {
        this.minOp = minOp;
    }
    public String getPlusop() {
        return plusOp;
    }

    public void setPlusop(String plusOp) {
        this.plusOp = plusOp;
    }

    public dsl_Statement getDsl_statement() {
        return dsl_statement;
    }

    public void setDsl_statement(dsl_Statement dsl_statement) {
        this.dsl_statement = dsl_statement;
    }
    public dsl_PreIncrementExpression getDsl_preincrementexpression() {
        return dsl_preincrementexpression;
    }

    public void setDsl_preincrementexpression(dsl_PreIncrementExpression dsl_preincrementexpression) {
        this.dsl_preincrementexpression = dsl_preincrementexpression;
    }
    public dsl_PreDecrementExpression getDsl_predecrementexpression() {
        return dsl_predecrementexpression;
    }

    public void setDsl_predecrementexpression(dsl_PreDecrementExpression dsl_predecrementexpression) {
        this.dsl_predecrementexpression = dsl_predecrementexpression;
    }
    public dsl_Expression getDsl_expression() {
        return dsl_expression;
    }

    public void setDsl_expression(dsl_Expression dsl_expression) {
        this.dsl_expression = dsl_expression;
    }
    public dsl_PrimaryExpression getDsl_primaryexpression() {
        return dsl_primaryexpression;
    }

    public void setDsl_primaryexpression(dsl_PrimaryExpression dsl_primaryexpression) {
        this.dsl_primaryexpression = dsl_primaryexpression;
    }

}