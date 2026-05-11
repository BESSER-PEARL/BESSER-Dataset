





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_Anchor extends PictogramElement {






    private AnchorContainer anchorcontainer;




    private GraphicsAlgorithm graphicsalgorithm;




    private List<Connection> connections;




    private List<Connection> connections;


    public mm_pictograms_Anchor(
    ) {
        super(
        );
        this.connections = new ArrayList<>();
        this.connections = new ArrayList<>();
    }

    public mm_pictograms_Anchor(
        ArrayList<Connection> connections,        ArrayList<Connection> connections    ) {
        this.connections = connections;
        this.connections = connections;
    }


    public AnchorContainer getAnchorcontainer() {
        return anchorcontainer;
    }

    public void setAnchorcontainer(AnchorContainer anchorcontainer) {
        this.anchorcontainer = anchorcontainer;
    }
    public GraphicsAlgorithm getGraphicsalgorithm() {
        return graphicsalgorithm;
    }

    public void setGraphicsalgorithm(GraphicsAlgorithm graphicsalgorithm) {
        this.graphicsalgorithm = graphicsalgorithm;
    }
    public List<Connection> getConnections() {
        return connections;
    }

    public void addConnection(Connection connection) {
        this.connections.add(connection);
    }
    public List<Connection> getConnections() {
        return connections;
    }

    public void addConnection(Connection connection) {
        this.connections.add(connection);
    }

}