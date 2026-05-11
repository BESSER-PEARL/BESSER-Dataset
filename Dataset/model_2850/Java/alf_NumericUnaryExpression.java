





import java.util.List;
import java.util.ArrayList;

public class alf_NumericUnaryExpression extends NonPostfixNonCastUnaryExpression {

    private String operator;





    private alf_UnaryExpression alf_unaryexpression;


    public alf_NumericUnaryExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public alf_UnaryExpression getAlf_unaryexpression() {
        return alf_unaryexpression;
    }

    public void setAlf_unaryexpression(alf_UnaryExpression alf_unaryexpression) {
        this.alf_unaryexpression = alf_unaryexpression;
    }

}