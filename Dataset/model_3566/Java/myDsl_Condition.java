





import java.util.List;
import java.util.ArrayList;

public class myDsl_Condition  {






    private myDsl_ForStmtLinha mydsl_forstmtlinha;




    private myDsl_Expression mydsl_expression;




    private myDsl_ForStmt mydsl_forstmt;


    public myDsl_Condition(
    ) {
    }



    public myDsl_ForStmtLinha getMydsl_forstmtlinha() {
        return mydsl_forstmtlinha;
    }

    public void setMydsl_forstmtlinha(myDsl_ForStmtLinha mydsl_forstmtlinha) {
        this.mydsl_forstmtlinha = mydsl_forstmtlinha;
    }
    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_ForStmt getMydsl_forstmt() {
        return mydsl_forstmt;
    }

    public void setMydsl_forstmt(myDsl_ForStmt mydsl_forstmt) {
        this.mydsl_forstmt = mydsl_forstmt;
    }

}