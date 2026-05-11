





import java.util.List;
import java.util.ArrayList;

public class cal_AstExpressionVariable extends AstExpression {






    private List<cal_AstExpression> cal_astexpressions;




    private cal_AstVariableReference cal_astvariablereference;




    private List<cal_AstMemberAccess> cal_astmemberaccesss;


    public cal_AstExpressionVariable(
    ) {
        super(
        );
        this.cal_astexpressions = new ArrayList<>();
        this.cal_astmemberaccesss = new ArrayList<>();
    }

    public cal_AstExpressionVariable(
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
    public cal_AstVariableReference getCal_astvariablereference() {
        return cal_astvariablereference;
    }

    public void setCal_astvariablereference(cal_AstVariableReference cal_astvariablereference) {
        this.cal_astvariablereference = cal_astvariablereference;
    }
    public List<cal_AstMemberAccess> getCal_astmemberaccesss() {
        return cal_astmemberaccesss;
    }

    public void addCal_astmemberaccess(Cal_astmemberaccess cal_astmemberaccess) {
        this.cal_astmemberaccesss.add(cal_astmemberaccess);
    }

}