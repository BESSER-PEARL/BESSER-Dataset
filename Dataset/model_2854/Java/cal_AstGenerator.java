





import java.util.List;
import java.util.ArrayList;

public class cal_AstGenerator  {






    private cal_AstExpressionList cal_astexpressionlist;




    private cal_AstExpression cal_astexpression;




    private cal_AstVariable cal_astvariable;


    public cal_AstGenerator(
    ) {
    }



    public cal_AstExpressionList getCal_astexpressionlist() {
        return cal_astexpressionlist;
    }

    public void setCal_astexpressionlist(cal_AstExpressionList cal_astexpressionlist) {
        this.cal_astexpressionlist = cal_astexpressionlist;
    }
    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }
    public cal_AstVariable getCal_astvariable() {
        return cal_astvariable;
    }

    public void setCal_astvariable(cal_AstVariable cal_astvariable) {
        this.cal_astvariable = cal_astvariable;
    }

}