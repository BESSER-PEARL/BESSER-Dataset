





import java.util.List;
import java.util.ArrayList;

public class cal_ExpressionIndex extends AstExpression {






    private List<cal_AstExpression> cal_astexpressions;




    private cal_VariableReference cal_variablereference;


    public cal_ExpressionIndex(
    ) {
        super(
        );
        this.cal_astexpressions = new ArrayList<>();
    }

    public cal_ExpressionIndex(
        ArrayList<cal_AstExpression> cal_astexpressions    ) {
        this.cal_astexpressions = cal_astexpressions;
    }


    public List<cal_AstExpression> getCal_astexpressions() {
        return cal_astexpressions;
    }

    public void addCal_astexpression(Cal_astexpression cal_astexpression) {
        this.cal_astexpressions.add(cal_astexpression);
    }
    public cal_VariableReference getCal_variablereference() {
        return cal_variablereference;
    }

    public void setCal_variablereference(cal_VariableReference cal_variablereference) {
        this.cal_variablereference = cal_variablereference;
    }

}