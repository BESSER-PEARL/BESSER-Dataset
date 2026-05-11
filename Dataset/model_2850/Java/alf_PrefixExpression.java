





import java.util.List;
import java.util.ArrayList;

public class alf_PrefixExpression extends NonPostfixNonCastUnaryExpression {

    private String operator;





    private alf_PrimaryExpression alf_primaryexpression;


    public alf_PrefixExpression(
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

    public alf_PrimaryExpression getAlf_primaryexpression() {
        return alf_primaryexpression;
    }

    public void setAlf_primaryexpression(alf_PrimaryExpression alf_primaryexpression) {
        this.alf_primaryexpression = alf_primaryexpression;
    }

}