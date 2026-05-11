





import java.util.List;
import java.util.ArrayList;

public class myDsl_Label  {

    private String id;





    private myDsl_LabeledStmt mydsl_labeledstmt;




    private myDsl_GotoStmt mydsl_gotostmt;




    private myDsl_BreakStmt mydsl_breakstmt;




    private myDsl_ContinueStmt mydsl_continuestmt;


    public myDsl_Label(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myDsl_LabeledStmt getMydsl_labeledstmt() {
        return mydsl_labeledstmt;
    }

    public void setMydsl_labeledstmt(myDsl_LabeledStmt mydsl_labeledstmt) {
        this.mydsl_labeledstmt = mydsl_labeledstmt;
    }
    public myDsl_GotoStmt getMydsl_gotostmt() {
        return mydsl_gotostmt;
    }

    public void setMydsl_gotostmt(myDsl_GotoStmt mydsl_gotostmt) {
        this.mydsl_gotostmt = mydsl_gotostmt;
    }
    public myDsl_BreakStmt getMydsl_breakstmt() {
        return mydsl_breakstmt;
    }

    public void setMydsl_breakstmt(myDsl_BreakStmt mydsl_breakstmt) {
        this.mydsl_breakstmt = mydsl_breakstmt;
    }
    public myDsl_ContinueStmt getMydsl_continuestmt() {
        return mydsl_continuestmt;
    }

    public void setMydsl_continuestmt(myDsl_ContinueStmt mydsl_continuestmt) {
        this.mydsl_continuestmt = mydsl_continuestmt;
    }

}