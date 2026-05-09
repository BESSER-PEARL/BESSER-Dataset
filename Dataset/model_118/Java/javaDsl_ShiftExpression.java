





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ShiftExpression  {

    private String operators;





    private javaDsl_RelationalExpression javadsl_relationalexpression;


    public javaDsl_ShiftExpression(
        String operators    ) {
        this.operators = operators;
    }


    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public javaDsl_RelationalExpression getJavadsl_relationalexpression() {
        return javadsl_relationalexpression;
    }

    public void setJavadsl_relationalexpression(javaDsl_RelationalExpression javadsl_relationalexpression) {
        this.javadsl_relationalexpression = javadsl_relationalexpression;
    }

}