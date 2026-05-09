





import java.util.List;
import java.util.ArrayList;

public class graph_Node extends Identifiable {

    private boolean visited;
    private boolean Attacker;
    private String name;
    private int AttackerObservation;





    private graph_Edge graph_edge;




    private List<graph_NodeResponsibility> graph_noderesponsibilitys;




    private graph_Subgraphs graph_subgraphs;




    private List<graph_Edge> graph_edges;




    private List<graph_Edge> graph_edges;




    private graph_GraphAsset graph_graphasset;




    private graph_GraphAsset graph_graphasset;




    private graph_Edge graph_edge;


    public graph_Node(
        boolean visited,        boolean Attacker,        String name,        int AttackerObservation    ) {
        super(
        );
        this.visited = visited;
        this.Attacker = Attacker;
        this.name = name;
        this.AttackerObservation = AttackerObservation;
        this.graph_noderesponsibilitys = new ArrayList<>();
        this.graph_edges = new ArrayList<>();
        this.graph_edges = new ArrayList<>();
    }

    public graph_Node(
        boolean visited,        boolean Attacker,        String name,        int AttackerObservation        ArrayList<graph_NodeResponsibility> graph_noderesponsibilitys,        ArrayList<graph_Edge> graph_edges,        ArrayList<graph_Edge> graph_edges    ) {
        this.visited = visited;
        this.Attacker = Attacker;
        this.name = name;
        this.AttackerObservation = AttackerObservation;
        this.graph_noderesponsibilitys = graph_noderesponsibilitys;
        this.graph_edges = graph_edges;
        this.graph_edges = graph_edges;
    }

    public boolean getVisited() {
        return visited;
    }

    public void setVisited(boolean visited) {
        this.visited = visited;
    }
    public boolean getAttacker() {
        return Attacker;
    }

    public void setAttacker(boolean Attacker) {
        this.Attacker = Attacker;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAttackerobservation() {
        return AttackerObservation;
    }

    public void setAttackerobservation(int AttackerObservation) {
        this.AttackerObservation = AttackerObservation;
    }

    public graph_Edge getGraph_edge() {
        return graph_edge;
    }

    public void setGraph_edge(graph_Edge graph_edge) {
        this.graph_edge = graph_edge;
    }
    public List<graph_NodeResponsibility> getGraph_noderesponsibilitys() {
        return graph_noderesponsibilitys;
    }

    public void addGraph_noderesponsibility(Graph_noderesponsibility graph_noderesponsibility) {
        this.graph_noderesponsibilitys.add(graph_noderesponsibility);
    }
    public graph_Subgraphs getGraph_subgraphs() {
        return graph_subgraphs;
    }

    public void setGraph_subgraphs(graph_Subgraphs graph_subgraphs) {
        this.graph_subgraphs = graph_subgraphs;
    }
    public List<graph_Edge> getGraph_edges() {
        return graph_edges;
    }

    public void addGraph_edge(Graph_edge graph_edge) {
        this.graph_edges.add(graph_edge);
    }
    public List<graph_Edge> getGraph_edges() {
        return graph_edges;
    }

    public void addGraph_edge(Graph_edge graph_edge) {
        this.graph_edges.add(graph_edge);
    }
    public graph_GraphAsset getGraph_graphasset() {
        return graph_graphasset;
    }

    public void setGraph_graphasset(graph_GraphAsset graph_graphasset) {
        this.graph_graphasset = graph_graphasset;
    }
    public graph_GraphAsset getGraph_graphasset() {
        return graph_graphasset;
    }

    public void setGraph_graphasset(graph_GraphAsset graph_graphasset) {
        this.graph_graphasset = graph_graphasset;
    }
    public graph_Edge getGraph_edge() {
        return graph_edge;
    }

    public void setGraph_edge(graph_Edge graph_edge) {
        this.graph_edge = graph_edge;
    }

}