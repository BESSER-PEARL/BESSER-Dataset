





import java.util.List;
import java.util.ArrayList;

public class dfs_DFSGraph  {






    private dfs_Edge dfs_edge;




    private List<dfs_Edge> dfs_edges;




    private dfs_Node dfs_node;




    private List<dfs_Node> dfs_nodes;


    public dfs_DFSGraph(
    ) {
        this.dfs_edges = new ArrayList<>();
        this.dfs_nodes = new ArrayList<>();
    }

    public dfs_DFSGraph(
        ArrayList<dfs_Edge> dfs_edges,        ArrayList<dfs_Node> dfs_nodes    ) {
        this.dfs_edges = dfs_edges;
        this.dfs_nodes = dfs_nodes;
    }


    public dfs_Edge getDfs_edge() {
        return dfs_edge;
    }

    public void setDfs_edge(dfs_Edge dfs_edge) {
        this.dfs_edge = dfs_edge;
    }
    public List<dfs_Edge> getDfs_edges() {
        return dfs_edges;
    }

    public void addDfs_edge(Dfs_edge dfs_edge) {
        this.dfs_edges.add(dfs_edge);
    }
    public dfs_Node getDfs_node() {
        return dfs_node;
    }

    public void setDfs_node(dfs_Node dfs_node) {
        this.dfs_node = dfs_node;
    }
    public List<dfs_Node> getDfs_nodes() {
        return dfs_nodes;
    }

    public void addDfs_node(Dfs_node dfs_node) {
        this.dfs_nodes.add(dfs_node);
    }

}