





import java.util.List;
import java.util.ArrayList;

public class javaDsl_AdditiveExpression  {

    private String operators;





    private javaDsl_ShiftExpression javadsl_shiftexpression;


    public javaDsl_AdditiveExpression(
        String operators    ) {
        this.operators = operators;
    }


    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public javaDsl_ShiftExpression getJavadsl_shiftexpression() {
        return javadsl_shiftexpression;
    }

    public void setJavadsl_shiftexpression(javaDsl_ShiftExpression javadsl_shiftexpression) {
        this.javadsl_shiftexpression = javadsl_shiftexpression;
    }

}