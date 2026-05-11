





import java.util.List;
import java.util.ArrayList;

public class myDsl_PostStmt  {






    private myDsl_SimpleStmt mydsl_simplestmt;




    private myDsl_ForStmtLinha mydsl_forstmtlinha;




    private myDsl_ForStmt mydsl_forstmt;


    public myDsl_PostStmt(
    ) {
    }



    public myDsl_SimpleStmt getMydsl_simplestmt() {
        return mydsl_simplestmt;
    }

    public void setMydsl_simplestmt(myDsl_SimpleStmt mydsl_simplestmt) {
        this.mydsl_simplestmt = mydsl_simplestmt;
    }
    public myDsl_ForStmtLinha getMydsl_forstmtlinha() {
        return mydsl_forstmtlinha;
    }

    public void setMydsl_forstmtlinha(myDsl_ForStmtLinha mydsl_forstmtlinha) {
        this.mydsl_forstmtlinha = mydsl_forstmtlinha;
    }
    public myDsl_ForStmt getMydsl_forstmt() {
        return mydsl_forstmt;
    }

    public void setMydsl_forstmt(myDsl_ForStmt mydsl_forstmt) {
        this.mydsl_forstmt = mydsl_forstmt;
    }

}