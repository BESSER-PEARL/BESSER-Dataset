





import java.util.List;
import java.util.ArrayList;

public class go_Label  {






    private go_GotoStmt go_gotostmt;




    private go_ContinueStmt go_continuestmt;




    private go_identifier go_identifier;




    private go_BreakStmt go_breakstmt;




    private go_LabeledStmt go_labeledstmt;


    public go_Label(
    ) {
    }



    public go_GotoStmt getGo_gotostmt() {
        return go_gotostmt;
    }

    public void setGo_gotostmt(go_GotoStmt go_gotostmt) {
        this.go_gotostmt = go_gotostmt;
    }
    public go_ContinueStmt getGo_continuestmt() {
        return go_continuestmt;
    }

    public void setGo_continuestmt(go_ContinueStmt go_continuestmt) {
        this.go_continuestmt = go_continuestmt;
    }
    public go_identifier getGo_identifier() {
        return go_identifier;
    }

    public void setGo_identifier(go_identifier go_identifier) {
        this.go_identifier = go_identifier;
    }
    public go_BreakStmt getGo_breakstmt() {
        return go_breakstmt;
    }

    public void setGo_breakstmt(go_BreakStmt go_breakstmt) {
        this.go_breakstmt = go_breakstmt;
    }
    public go_LabeledStmt getGo_labeledstmt() {
        return go_labeledstmt;
    }

    public void setGo_labeledstmt(go_LabeledStmt go_labeledstmt) {
        this.go_labeledstmt = go_labeledstmt;
    }

}