





import java.util.List;
import java.util.ArrayList;

public class cal_AstStatementAssign extends AstStatement {






    private List<cal_AstExpression> cal_astexpressions;




    private List<cal_AstMemberAccess> cal_astmemberaccesss;




    private cal_AstExpression cal_astexpression;


    public cal_AstStatementAssign(
    ) {
        super(
        );
        this.cal_astexpressions = new ArrayList<>();
        this.cal_astmemberaccesss = new ArrayList<>();
    }

    public cal_AstStatementAssign(
        ArrayList<cal_AstExpression> cal_astexpressions,        ArrayList<cal_AstMemberAccess> cal_astmemberaccesss    ) {
        this.cal_astexpressions = cal_astexpressions;
        this.cal_astmemberaccesss = cal_astmemberaccesss;
    }


    public List<cal_AstExpression> getCal_astexpressions() {
        return cal_astexpressions;
    }

    public void addCal_astexpression(Cal_astexpression cal_astexpression) {
        this.cal_astexpressions.add(cal_astexpression);
    }
    public List<cal_AstMemberAccess> getCal_astmemberaccesss() {
        return cal_astmemberaccesss;
    }

    public void addCal_astmemberaccess(Cal_astmemberaccess cal_astmemberaccess) {
        this.cal_astmemberaccesss.add(cal_astmemberaccess);
    }
    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }

}