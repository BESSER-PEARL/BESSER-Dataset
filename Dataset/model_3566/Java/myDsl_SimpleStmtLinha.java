





import java.util.List;
import java.util.ArrayList;

public class myDsl_SimpleStmtLinha  {

    private String aNY_OTHER;





    private myDsl_SimpleStmt mydsl_simplestmt;




    private myDsl_ExpressionList mydsl_expressionlist;




    private List<myDsl_Expression> mydsl_expressions;




    private myDsl_Expression mydsl_expression;


    public myDsl_SimpleStmtLinha(
        String aNY_OTHER    ) {
        this.aNY_OTHER = aNY_OTHER;
        this.mydsl_expressions = new ArrayList<>();
    }

    public myDsl_SimpleStmtLinha(
        String aNY_OTHER        ArrayList<myDsl_Expression> mydsl_expressions    ) {
        this.aNY_OTHER = aNY_OTHER;
        this.mydsl_expressions = mydsl_expressions;
    }

    public String getAny_other() {
        return aNY_OTHER;
    }

    public void setAny_other(String aNY_OTHER) {
        this.aNY_OTHER = aNY_OTHER;
    }

    public myDsl_SimpleStmt getMydsl_simplestmt() {
        return mydsl_simplestmt;
    }

    public void setMydsl_simplestmt(myDsl_SimpleStmt mydsl_simplestmt) {
        this.mydsl_simplestmt = mydsl_simplestmt;
    }
    public myDsl_ExpressionList getMydsl_expressionlist() {
        return mydsl_expressionlist;
    }

    public void setMydsl_expressionlist(myDsl_ExpressionList mydsl_expressionlist) {
        this.mydsl_expressionlist = mydsl_expressionlist;
    }
    public List<myDsl_Expression> getMydsl_expressions() {
        return mydsl_expressions;
    }

    public void addMydsl_expression(Mydsl_expression mydsl_expression) {
        this.mydsl_expressions.add(mydsl_expression);
    }
    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }

}