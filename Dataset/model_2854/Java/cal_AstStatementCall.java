





import java.util.List;
import java.util.ArrayList;

public class cal_AstStatementCall extends AstStatement {






    private cal_AstProcedure cal_astprocedure;




    private List<cal_AstExpression> cal_astexpressions;


    public cal_AstStatementCall(
    ) {
        super(
        );
        this.cal_astexpressions = new ArrayList<>();
    }

    public cal_AstStatementCall(
        ArrayList<cal_AstExpression> cal_astexpressions    ) {
        this.cal_astexpressions = cal_astexpressions;
    }


    public cal_AstProcedure getCal_astprocedure() {
        return cal_astprocedure;
    }

    public void setCal_astprocedure(cal_AstProcedure cal_astprocedure) {
        this.cal_astprocedure = cal_astprocedure;
    }
    public List<cal_AstExpression> getCal_astexpressions() {
        return cal_astexpressions;
    }

    public void addCal_astexpression(Cal_astexpression cal_astexpression) {
        this.cal_astexpressions.add(cal_astexpression);
    }

}