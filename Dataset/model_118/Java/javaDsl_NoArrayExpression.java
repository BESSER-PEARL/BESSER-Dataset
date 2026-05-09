





import java.util.List;
import java.util.ArrayList;

public class javaDsl_NoArrayExpression  {

    private String operator;





    private javaDsl_NoArrayExpression javadsl_noarrayexpression;




    private javaDsl_MultiplicativeExpression javadsl_multiplicativeexpression;


    public javaDsl_NoArrayExpression(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public javaDsl_NoArrayExpression getJavadsl_noarrayexpression() {
        return javadsl_noarrayexpression;
    }

    public void setJavadsl_noarrayexpression(javaDsl_NoArrayExpression javadsl_noarrayexpression) {
        this.javadsl_noarrayexpression = javadsl_noarrayexpression;
    }
    public javaDsl_MultiplicativeExpression getJavadsl_multiplicativeexpression() {
        return javadsl_multiplicativeexpression;
    }

    public void setJavadsl_multiplicativeexpression(javaDsl_MultiplicativeExpression javadsl_multiplicativeexpression) {
        this.javadsl_multiplicativeexpression = javadsl_multiplicativeexpression;
    }

}