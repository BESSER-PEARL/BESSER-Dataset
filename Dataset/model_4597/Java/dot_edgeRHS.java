





import java.util.List;
import java.util.ArrayList;

public class dot_edgeRHS  {

    private String op;





    private dot_edge_stmt_node dot_edge_stmt_node;




    private dot_edge_stmt_subgraph dot_edge_stmt_subgraph;


    public dot_edgeRHS(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public dot_edge_stmt_node getDot_edge_stmt_node() {
        return dot_edge_stmt_node;
    }

    public void setDot_edge_stmt_node(dot_edge_stmt_node dot_edge_stmt_node) {
        this.dot_edge_stmt_node = dot_edge_stmt_node;
    }
    public dot_edge_stmt_subgraph getDot_edge_stmt_subgraph() {
        return dot_edge_stmt_subgraph;
    }

    public void setDot_edge_stmt_subgraph(dot_edge_stmt_subgraph dot_edge_stmt_subgraph) {
        this.dot_edge_stmt_subgraph = dot_edge_stmt_subgraph;
    }

}