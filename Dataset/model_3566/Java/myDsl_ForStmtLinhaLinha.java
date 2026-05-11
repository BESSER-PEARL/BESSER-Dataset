





import java.util.List;
import java.util.ArrayList;

public class myDsl_ForStmtLinhaLinha  {

    private String range;





    private myDsl_assign_op mydsl_assign_op;




    private myDsl_ExpressionList mydsl_expressionlist;




    private myDsl_PostStmt mydsl_poststmt;




    private myDsl_Condition mydsl_condition;




    private myDsl_Expression mydsl_expression;




    private myDsl_ForStmtLinha mydsl_forstmtlinha;


    public myDsl_ForStmtLinhaLinha(
        String range    ) {
        this.range = range;
    }


    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }

    public myDsl_assign_op getMydsl_assign_op() {
        return mydsl_assign_op;
    }

    public void setMydsl_assign_op(myDsl_assign_op mydsl_assign_op) {
        this.mydsl_assign_op = mydsl_assign_op;
    }
    public myDsl_ExpressionList getMydsl_expressionlist() {
        return mydsl_expressionlist;
    }

    public void setMydsl_expressionlist(myDsl_ExpressionList mydsl_expressionlist) {
        this.mydsl_expressionlist = mydsl_expressionlist;
    }
    public myDsl_PostStmt getMydsl_poststmt() {
        return mydsl_poststmt;
    }

    public void setMydsl_poststmt(myDsl_PostStmt mydsl_poststmt) {
        this.mydsl_poststmt = mydsl_poststmt;
    }
    public myDsl_Condition getMydsl_condition() {
        return mydsl_condition;
    }

    public void setMydsl_condition(myDsl_Condition mydsl_condition) {
        this.mydsl_condition = mydsl_condition;
    }
    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_ForStmtLinha getMydsl_forstmtlinha() {
        return mydsl_forstmtlinha;
    }

    public void setMydsl_forstmtlinha(myDsl_ForStmtLinha mydsl_forstmtlinha) {
        this.mydsl_forstmtlinha = mydsl_forstmtlinha;
    }

}