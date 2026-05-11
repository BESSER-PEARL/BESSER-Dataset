





import java.util.List;
import java.util.ArrayList;

public class go_VarCall  {

    private String id;





    private go_ReturnStmt go_returnstmt;




    private go_BINARY_EXP go_binary_exp;


    public go_VarCall(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public go_ReturnStmt getGo_returnstmt() {
        return go_returnstmt;
    }

    public void setGo_returnstmt(go_ReturnStmt go_returnstmt) {
        this.go_returnstmt = go_returnstmt;
    }
    public go_BINARY_EXP getGo_binary_exp() {
        return go_binary_exp;
    }

    public void setGo_binary_exp(go_BINARY_EXP go_binary_exp) {
        this.go_binary_exp = go_binary_exp;
    }

}