





import java.util.List;
import java.util.ArrayList;

public class cal_AstExpressionUnary extends AstExpression {

    private String unaryOperator;





    private cal_AstExpression cal_astexpression;


    public cal_AstExpressionUnary(
        String unaryOperator    ) {
        super(
        );
        this.unaryOperator = unaryOperator;
    }


    public String getUnaryoperator() {
        return unaryOperator;
    }

    public void setUnaryoperator(String unaryOperator) {
        this.unaryOperator = unaryOperator;
    }

    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }

}