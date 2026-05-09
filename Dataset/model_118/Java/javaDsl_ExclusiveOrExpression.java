





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ExclusiveOrExpression  {

    private String operators;





    private javaDsl_InclusiveOrExpression javadsl_inclusiveorexpression;


    public javaDsl_ExclusiveOrExpression(
        String operators    ) {
        this.operators = operators;
    }


    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public javaDsl_InclusiveOrExpression getJavadsl_inclusiveorexpression() {
        return javadsl_inclusiveorexpression;
    }

    public void setJavadsl_inclusiveorexpression(javaDsl_InclusiveOrExpression javadsl_inclusiveorexpression) {
        this.javadsl_inclusiveorexpression = javadsl_inclusiveorexpression;
    }

}