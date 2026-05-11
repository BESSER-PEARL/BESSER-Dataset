





import java.util.List;
import java.util.ArrayList;

public class cal_AstMemberAccess  {

    private String name;





    private cal_AstStatementAssign cal_aststatementassign;




    private List<cal_AstExpression> cal_astexpressions;


    public cal_AstMemberAccess(
        String name    ) {
        this.name = name;
        this.cal_astexpressions = new ArrayList<>();
    }

    public cal_AstMemberAccess(
        String name        ArrayList<cal_AstExpression> cal_astexpressions    ) {
        this.name = name;
        this.cal_astexpressions = cal_astexpressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cal_AstStatementAssign getCal_aststatementassign() {
        return cal_aststatementassign;
    }

    public void setCal_aststatementassign(cal_AstStatementAssign cal_aststatementassign) {
        this.cal_aststatementassign = cal_aststatementassign;
    }
    public List<cal_AstExpression> getCal_astexpressions() {
        return cal_astexpressions;
    }

    public void addCal_astexpression(Cal_astexpression cal_astexpression) {
        this.cal_astexpressions.add(cal_astexpression);
    }

}