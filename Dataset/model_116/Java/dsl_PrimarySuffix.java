





import java.util.List;
import java.util.ArrayList;

public class dsl_PrimarySuffix  {

    private boolean thisOp;
    private String id;





    private dsl_Arguments dsl_arguments;




    private dsl_Expression dsl_expression;




    private dsl_AllocationExpression dsl_allocationexpression;


    public dsl_PrimarySuffix(
        boolean thisOp,        String id    ) {
        this.thisOp = thisOp;
        this.id = id;
    }


    public boolean getThisop() {
        return thisOp;
    }

    public void setThisop(boolean thisOp) {
        this.thisOp = thisOp;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dsl_Arguments getDsl_arguments() {
        return dsl_arguments;
    }

    public void setDsl_arguments(dsl_Arguments dsl_arguments) {
        this.dsl_arguments = dsl_arguments;
    }
    public dsl_Expression getDsl_expression() {
        return dsl_expression;
    }

    public void setDsl_expression(dsl_Expression dsl_expression) {
        this.dsl_expression = dsl_expression;
    }
    public dsl_AllocationExpression getDsl_allocationexpression() {
        return dsl_allocationexpression;
    }

    public void setDsl_allocationexpression(dsl_AllocationExpression dsl_allocationexpression) {
        this.dsl_allocationexpression = dsl_allocationexpression;
    }

}