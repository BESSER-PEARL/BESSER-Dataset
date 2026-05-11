





import java.util.List;
import java.util.ArrayList;

public class cal_AstExpressionList extends AstExpression {






    private List<cal_AstExpression> cal_astexpressions;


    public cal_AstExpressionList(
    ) {
        super(
        );
        this.cal_astexpressions = new ArrayList<>();
    }

    public cal_AstExpressionList(
        ArrayList<cal_AstExpression> cal_astexpressions    ) {
        this.cal_astexpressions = cal_astexpressions;
    }


    public List<cal_AstExpression> getCal_astexpressions() {
        return cal_astexpressions;
    }

    public void addCal_astexpression(Cal_astexpression cal_astexpression) {
        this.cal_astexpressions.add(cal_astexpression);
    }

}