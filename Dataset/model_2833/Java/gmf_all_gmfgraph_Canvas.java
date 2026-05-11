





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_Canvas extends Identity {






    private List<Compartment> compartments;




    private List<DiagramLabel> diagramlabels;




    private List<Connection> connections;


    public gmf_all_gmfgraph_Canvas(
    ) {
        super(
        );
        this.compartments = new ArrayList<>();
        this.diagramlabels = new ArrayList<>();
        this.connections = new ArrayList<>();
    }

    public gmf_all_gmfgraph_Canvas(
        ArrayList<Compartment> compartments,        ArrayList<DiagramLabel> diagramlabels,        ArrayList<Connection> connections    ) {
        this.compartments = compartments;
        this.diagramlabels = diagramlabels;
        this.connections = connections;
    }


    public List<Compartment> getCompartments() {
        return compartments;
    }

    public void addCompartment(Compartment compartment) {
        this.compartments.add(compartment);
    }
    public List<DiagramLabel> getDiagramlabels() {
        return diagramlabels;
    }

    public void addDiagramlabel(Diagramlabel diagramlabel) {
        this.diagramlabels.add(diagramlabel);
    }
    public List<Connection> getConnections() {
        return connections;
    }

    public void addConnection(Connection connection) {
        this.connections.add(connection);
    }

}