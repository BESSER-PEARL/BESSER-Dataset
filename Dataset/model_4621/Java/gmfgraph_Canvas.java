





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Canvas extends Identity {






    private List<gmfgraph_Node> gmfgraph_nodes;




    private List<gmfgraph_DiagramLabel> gmfgraph_diagramlabels;




    private List<gmfgraph_Compartment> gmfgraph_compartments;




    private List<gmfgraph_Connection> gmfgraph_connections;


    public gmfgraph_Canvas(
    ) {
        super(
        );
        this.gmfgraph_nodes = new ArrayList<>();
        this.gmfgraph_diagramlabels = new ArrayList<>();
        this.gmfgraph_compartments = new ArrayList<>();
        this.gmfgraph_connections = new ArrayList<>();
    }

    public gmfgraph_Canvas(
        ArrayList<gmfgraph_Node> gmfgraph_nodes,        ArrayList<gmfgraph_DiagramLabel> gmfgraph_diagramlabels,        ArrayList<gmfgraph_Compartment> gmfgraph_compartments,        ArrayList<gmfgraph_Connection> gmfgraph_connections    ) {
        this.gmfgraph_nodes = gmfgraph_nodes;
        this.gmfgraph_diagramlabels = gmfgraph_diagramlabels;
        this.gmfgraph_compartments = gmfgraph_compartments;
        this.gmfgraph_connections = gmfgraph_connections;
    }


    public List<gmfgraph_Node> getGmfgraph_nodes() {
        return gmfgraph_nodes;
    }

    public void addGmfgraph_node(Gmfgraph_node gmfgraph_node) {
        this.gmfgraph_nodes.add(gmfgraph_node);
    }
    public List<gmfgraph_DiagramLabel> getGmfgraph_diagramlabels() {
        return gmfgraph_diagramlabels;
    }

    public void addGmfgraph_diagramlabel(Gmfgraph_diagramlabel gmfgraph_diagramlabel) {
        this.gmfgraph_diagramlabels.add(gmfgraph_diagramlabel);
    }
    public List<gmfgraph_Compartment> getGmfgraph_compartments() {
        return gmfgraph_compartments;
    }

    public void addGmfgraph_compartment(Gmfgraph_compartment gmfgraph_compartment) {
        this.gmfgraph_compartments.add(gmfgraph_compartment);
    }
    public List<gmfgraph_Connection> getGmfgraph_connections() {
        return gmfgraph_connections;
    }

    public void addGmfgraph_connection(Gmfgraph_connection gmfgraph_connection) {
        this.gmfgraph_connections.add(gmfgraph_connection);
    }

}