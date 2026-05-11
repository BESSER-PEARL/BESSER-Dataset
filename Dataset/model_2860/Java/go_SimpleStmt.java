





import java.util.List;
import java.util.ArrayList;

public class go_SimpleStmt extends SwitchStmt {

    private String EmptyStmt;





    private go_ShortVarDecl go_shortvardecl;




    private go_IfStmt go_ifstmt;




    private go_Statement go_statement;


    public go_SimpleStmt(
        String EmptyStmt    ) {
        super(
        );
        this.EmptyStmt = EmptyStmt;
    }


    public String getEmptystmt() {
        return EmptyStmt;
    }

    public void setEmptystmt(String EmptyStmt) {
        this.EmptyStmt = EmptyStmt;
    }

    public go_ShortVarDecl getGo_shortvardecl() {
        return go_shortvardecl;
    }

    public void setGo_shortvardecl(go_ShortVarDecl go_shortvardecl) {
        this.go_shortvardecl = go_shortvardecl;
    }
    public go_IfStmt getGo_ifstmt() {
        return go_ifstmt;
    }

    public void setGo_ifstmt(go_IfStmt go_ifstmt) {
        this.go_ifstmt = go_ifstmt;
    }
    public go_Statement getGo_statement() {
        return go_statement;
    }

    public void setGo_statement(go_Statement go_statement) {
        this.go_statement = go_statement;
    }

}