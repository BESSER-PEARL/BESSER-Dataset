





import java.util.List;
import java.util.ArrayList;

public class flowgraph_Label extends Stmt {






    private flowgraph_JumpStmt flowgraph_jumpstmt;




    private flowgraph_Stmt flowgraph_stmt;




    private List<flowgraph_JumpStmt> flowgraph_jumpstmts;


    public flowgraph_Label(
    ) {
        super(
        );
        this.flowgraph_jumpstmts = new ArrayList<>();
    }

    public flowgraph_Label(
        ArrayList<flowgraph_JumpStmt> flowgraph_jumpstmts    ) {
        this.flowgraph_jumpstmts = flowgraph_jumpstmts;
    }


    public flowgraph_JumpStmt getFlowgraph_jumpstmt() {
        return flowgraph_jumpstmt;
    }

    public void setFlowgraph_jumpstmt(flowgraph_JumpStmt flowgraph_jumpstmt) {
        this.flowgraph_jumpstmt = flowgraph_jumpstmt;
    }
    public flowgraph_Stmt getFlowgraph_stmt() {
        return flowgraph_stmt;
    }

    public void setFlowgraph_stmt(flowgraph_Stmt flowgraph_stmt) {
        this.flowgraph_stmt = flowgraph_stmt;
    }
    public List<flowgraph_JumpStmt> getFlowgraph_jumpstmts() {
        return flowgraph_jumpstmts;
    }

    public void addFlowgraph_jumpstmt(Flowgraph_jumpstmt flowgraph_jumpstmt) {
        this.flowgraph_jumpstmts.add(flowgraph_jumpstmt);
    }

}