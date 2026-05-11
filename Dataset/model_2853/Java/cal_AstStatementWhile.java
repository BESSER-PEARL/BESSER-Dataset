





import java.util.List;
import java.util.ArrayList;

public class cal_AstStatementWhile extends AstStatement {






    private List<cal_AstStatement> cal_aststatements;




    private cal_AstExpression cal_astexpression;


    public cal_AstStatementWhile(
    ) {
        super(
        );
        this.cal_aststatements = new ArrayList<>();
    }

    public cal_AstStatementWhile(
        ArrayList<cal_AstStatement> cal_aststatements    ) {
        this.cal_aststatements = cal_aststatements;
    }


    public List<cal_AstStatement> getCal_aststatements() {
        return cal_aststatements;
    }

    public void addCal_aststatement(Cal_aststatement cal_aststatement) {
        this.cal_aststatements.add(cal_aststatement);
    }
    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }

}