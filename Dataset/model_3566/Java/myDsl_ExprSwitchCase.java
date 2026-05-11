





import java.util.List;
import java.util.ArrayList;

public class myDsl_ExprSwitchCase  {

    private String default;
    private String case;





    private myDsl_ExprCaseClause mydsl_exprcaseclause;




    private myDsl_ExpressionList mydsl_expressionlist;


    public myDsl_ExprSwitchCase(
        String default,        String case    ) {
        this.default = default;
        this.case = case;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getCase() {
        return case;
    }

    public void setCase(String case) {
        this.case = case;
    }

    public myDsl_ExprCaseClause getMydsl_exprcaseclause() {
        return mydsl_exprcaseclause;
    }

    public void setMydsl_exprcaseclause(myDsl_ExprCaseClause mydsl_exprcaseclause) {
        this.mydsl_exprcaseclause = mydsl_exprcaseclause;
    }
    public myDsl_ExpressionList getMydsl_expressionlist() {
        return mydsl_expressionlist;
    }

    public void setMydsl_expressionlist(myDsl_ExpressionList mydsl_expressionlist) {
        this.mydsl_expressionlist = mydsl_expressionlist;
    }

}