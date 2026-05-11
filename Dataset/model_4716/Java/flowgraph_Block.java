





import java.util.List;
import java.util.ArrayList;

public class flowgraph_Block extends Stmt {






    private List<flowgraph_Stmt> flowgraph_stmts;


    public flowgraph_Block(
    ) {
        super(
        );
        this.flowgraph_stmts = new ArrayList<>();
    }

    public flowgraph_Block(
        ArrayList<flowgraph_Stmt> flowgraph_stmts    ) {
        this.flowgraph_stmts = flowgraph_stmts;
    }


    public List<flowgraph_Stmt> getFlowgraph_stmts() {
        return flowgraph_stmts;
    }

    public void addFlowgraph_stmt(Flowgraph_stmt flowgraph_stmt) {
        this.flowgraph_stmts.add(flowgraph_stmt);
    }

}