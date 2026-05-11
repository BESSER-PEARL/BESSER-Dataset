





import java.util.List;
import java.util.ArrayList;

public class go_Assignment  {

    private String assign_op;





    private go_SimpleStmt go_simplestmt;




    private List<go_ExpressionList> go_expressionlists;


    public go_Assignment(
        String assign_op    ) {
        this.assign_op = assign_op;
        this.go_expressionlists = new ArrayList<>();
    }

    public go_Assignment(
        String assign_op        ArrayList<go_ExpressionList> go_expressionlists    ) {
        this.assign_op = assign_op;
        this.go_expressionlists = go_expressionlists;
    }

    public String getAssign_op() {
        return assign_op;
    }

    public void setAssign_op(String assign_op) {
        this.assign_op = assign_op;
    }

    public go_SimpleStmt getGo_simplestmt() {
        return go_simplestmt;
    }

    public void setGo_simplestmt(go_SimpleStmt go_simplestmt) {
        this.go_simplestmt = go_simplestmt;
    }
    public List<go_ExpressionList> getGo_expressionlists() {
        return go_expressionlists;
    }

    public void addGo_expressionlist(Go_expressionlist go_expressionlist) {
        this.go_expressionlists.add(go_expressionlist);
    }

}