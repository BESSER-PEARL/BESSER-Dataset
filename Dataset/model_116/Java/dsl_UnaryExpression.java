





import java.util.List;
import java.util.ArrayList;

public class dsl_UnaryExpression  {

    private String sign;





    private dsl_UnaryExpression dsl_unaryexpression;




    private dsl_MultiplicativeExpression dsl_multiplicativeexpression;


    public dsl_UnaryExpression(
        String sign    ) {
        this.sign = sign;
    }


    public String getSign() {
        return sign;
    }

    public void setSign(String sign) {
        this.sign = sign;
    }

    public dsl_UnaryExpression getDsl_unaryexpression() {
        return dsl_unaryexpression;
    }

    public void setDsl_unaryexpression(dsl_UnaryExpression dsl_unaryexpression) {
        this.dsl_unaryexpression = dsl_unaryexpression;
    }
    public dsl_MultiplicativeExpression getDsl_multiplicativeexpression() {
        return dsl_multiplicativeexpression;
    }

    public void setDsl_multiplicativeexpression(dsl_MultiplicativeExpression dsl_multiplicativeexpression) {
        this.dsl_multiplicativeexpression = dsl_multiplicativeexpression;
    }

}