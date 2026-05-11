





import java.util.List;
import java.util.ArrayList;

public class cal_AstStatementAssign extends AstStatement {






    private cal_AstExpression cal_astexpression;




    private List<cal_AstExpression> cal_astexpressions;


    public cal_AstStatementAssign(
    ) {
        super(
        );
        this.cal_astexpressions = new ArrayList<>();
    }

    public cal_AstStatementAssign(
        ArrayList<cal_AstExpression> cal_astexpressions    ) {
        this.cal_astexpressions = cal_astexpressions;
    }


    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }
    public List<cal_AstExpression> getCal_astexpressions() {
        return cal_astexpressions;
    }

    public void addCal_astexpression(Cal_astexpression cal_astexpression) {
        this.cal_astexpressions.add(cal_astexpression);
    }

}