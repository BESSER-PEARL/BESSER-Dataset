





import java.util.List;
import java.util.ArrayList;

public class graph_Edge extends Identifiable, Modifiable {

    private String nodeAURI;
    private boolean directed;
    private String nodeBURI;



    public graph_Edge(
        String nodeAURI,        boolean directed,        String nodeBURI    ) {
        super(
        );
        this.nodeAURI = nodeAURI;
        this.directed = directed;
        this.nodeBURI = nodeBURI;
    }


    public String getNodeauri() {
        return nodeAURI;
    }

    public void setNodeauri(String nodeAURI) {
        this.nodeAURI = nodeAURI;
    }
    public boolean getDirected() {
        return directed;
    }

    public void setDirected(boolean directed) {
        this.directed = directed;
    }
    public String getNodeburi() {
        return nodeBURI;
    }

    public void setNodeburi(String nodeBURI) {
        this.nodeBURI = nodeBURI;
    }


}