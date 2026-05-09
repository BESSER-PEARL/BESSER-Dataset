





import java.util.List;
import java.util.ArrayList;

public class javaDsl_AndExpression  {

    private String operators;





    private javaDsl_ExclusiveOrExpression javadsl_exclusiveorexpression;


    public javaDsl_AndExpression(
        String operators    ) {
        this.operators = operators;
    }


    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public javaDsl_ExclusiveOrExpression getJavadsl_exclusiveorexpression() {
        return javadsl_exclusiveorexpression;
    }

    public void setJavadsl_exclusiveorexpression(javaDsl_ExclusiveOrExpression javadsl_exclusiveorexpression) {
        this.javadsl_exclusiveorexpression = javadsl_exclusiveorexpression;
    }

}