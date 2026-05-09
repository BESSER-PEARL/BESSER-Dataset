





import java.util.List;
import java.util.ArrayList;

public class DAG_Node  {

    private int level;
    private int ID;
    private String name;





    private List<DAG_Node> dag_nodes;




    private List<DAG_Node> dag_nodes;




    private DAG_Revision dag_revision;




    private DAG_Graph dag_graph;


    public DAG_Node(
        int level,        int ID,        String name    ) {
        this.level = level;
        this.ID = ID;
        this.name = name;
        this.dag_nodes = new ArrayList<>();
        this.dag_nodes = new ArrayList<>();
    }

    public DAG_Node(
        int level,        int ID,        String name        ArrayList<DAG_Node> dag_nodes,        ArrayList<DAG_Node> dag_nodes    ) {
        this.level = level;
        this.ID = ID;
        this.name = name;
        this.dag_nodes = dag_nodes;
        this.dag_nodes = dag_nodes;
    }

    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<DAG_Node> getDag_nodes() {
        return dag_nodes;
    }

    public void addDag_node(Dag_node dag_node) {
        this.dag_nodes.add(dag_node);
    }
    public List<DAG_Node> getDag_nodes() {
        return dag_nodes;
    }

    public void addDag_node(Dag_node dag_node) {
        this.dag_nodes.add(dag_node);
    }
    public DAG_Revision getDag_revision() {
        return dag_revision;
    }

    public void setDag_revision(DAG_Revision dag_revision) {
        this.dag_revision = dag_revision;
    }
    public DAG_Graph getDag_graph() {
        return dag_graph;
    }

    public void setDag_graph(DAG_Graph dag_graph) {
        this.dag_graph = dag_graph;
    }

}