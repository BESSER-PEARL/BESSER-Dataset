





import java.util.List;
import java.util.ArrayList;

public class cal_AstExpressionCall extends AstExpression {






    private cal_AstFunction cal_astfunction;




    private List<cal_AstExpression> cal_astexpressions;


    public cal_AstExpressionCall(
    ) {
        super(
        );
        this.cal_astexpressions = new ArrayList<>();
    }

    public cal_AstExpressionCall(
        ArrayList<cal_AstExpression> cal_astexpressions    ) {
        this.cal_astexpressions = cal_astexpressions;
    }


    public cal_AstFunction getCal_astfunction() {
        return cal_astfunction;
    }

    public void setCal_astfunction(cal_AstFunction cal_astfunction) {
        this.cal_astfunction = cal_astfunction;
    }
    public List<cal_AstExpression> getCal_astexpressions() {
        return cal_astexpressions;
    }

    public void addCal_astexpression(Cal_astexpression cal_astexpression) {
        this.cal_astexpressions.add(cal_astexpression);
    }

}