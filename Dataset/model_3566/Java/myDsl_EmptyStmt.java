





import java.util.List;
import java.util.ArrayList;

public class myDsl_EmptyStmt  {

    private String aNY_OTHER;





    private myDsl_IfStmt mydsl_ifstmt;




    private myDsl_SimpleStmt mydsl_simplestmt;




    private myDsl_ForStmt mydsl_forstmt;


    public myDsl_EmptyStmt(
        String aNY_OTHER    ) {
        this.aNY_OTHER = aNY_OTHER;
    }


    public String getAny_other() {
        return aNY_OTHER;
    }

    public void setAny_other(String aNY_OTHER) {
        this.aNY_OTHER = aNY_OTHER;
    }

    public myDsl_IfStmt getMydsl_ifstmt() {
        return mydsl_ifstmt;
    }

    public void setMydsl_ifstmt(myDsl_IfStmt mydsl_ifstmt) {
        this.mydsl_ifstmt = mydsl_ifstmt;
    }
    public myDsl_SimpleStmt getMydsl_simplestmt() {
        return mydsl_simplestmt;
    }

    public void setMydsl_simplestmt(myDsl_SimpleStmt mydsl_simplestmt) {
        this.mydsl_simplestmt = mydsl_simplestmt;
    }
    public myDsl_ForStmt getMydsl_forstmt() {
        return mydsl_forstmt;
    }

    public void setMydsl_forstmt(myDsl_ForStmt mydsl_forstmt) {
        this.mydsl_forstmt = mydsl_forstmt;
    }

}