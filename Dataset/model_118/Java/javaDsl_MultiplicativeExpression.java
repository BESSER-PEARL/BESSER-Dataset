





import java.util.List;
import java.util.ArrayList;

public class javaDsl_MultiplicativeExpression  {

    private String operators;





    private javaDsl_AdditiveExpression javadsl_additiveexpression;


    public javaDsl_MultiplicativeExpression(
        String operators    ) {
        this.operators = operators;
    }


    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public javaDsl_AdditiveExpression getJavadsl_additiveexpression() {
        return javadsl_additiveexpression;
    }

    public void setJavadsl_additiveexpression(javaDsl_AdditiveExpression javadsl_additiveexpression) {
        this.javadsl_additiveexpression = javadsl_additiveexpression;
    }

}