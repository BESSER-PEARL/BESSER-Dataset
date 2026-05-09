





import java.util.List;
import java.util.ArrayList;

public class javaDsl_EqualityExpression  {

    private String operators;





    private javaDsl_AndExpression javadsl_andexpression;


    public javaDsl_EqualityExpression(
        String operators    ) {
        this.operators = operators;
    }


    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public javaDsl_AndExpression getJavadsl_andexpression() {
        return javadsl_andexpression;
    }

    public void setJavadsl_andexpression(javaDsl_AndExpression javadsl_andexpression) {
        this.javadsl_andexpression = javadsl_andexpression;
    }

}