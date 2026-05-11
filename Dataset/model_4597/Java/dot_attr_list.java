





import java.util.List;
import java.util.ArrayList;

public class dot_attr_list  {






    private dot_node_stmt dot_node_stmt;




    private dot_edge_stmt_node dot_edge_stmt_node;




    private dot_edge_stmt_subgraph dot_edge_stmt_subgraph;




    private dot_attr_stmt dot_attr_stmt;


    public dot_attr_list(
    ) {
    }



    public dot_node_stmt getDot_node_stmt() {
        return dot_node_stmt;
    }

    public void setDot_node_stmt(dot_node_stmt dot_node_stmt) {
        this.dot_node_stmt = dot_node_stmt;
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
    public dot_attr_stmt getDot_attr_stmt() {
        return dot_attr_stmt;
    }

    public void setDot_attr_stmt(dot_attr_stmt dot_attr_stmt) {
        this.dot_attr_stmt = dot_attr_stmt;
    }

}