





import java.util.List;
import java.util.ArrayList;

public class dot_node_id  {

    private String name;





    private dot_edge_stmt_node dot_edge_stmt_node;


    public dot_node_id(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dot_edge_stmt_node getDot_edge_stmt_node() {
        return dot_edge_stmt_node;
    }

    public void setDot_edge_stmt_node(dot_edge_stmt_node dot_edge_stmt_node) {
        this.dot_edge_stmt_node = dot_edge_stmt_node;
    }

}