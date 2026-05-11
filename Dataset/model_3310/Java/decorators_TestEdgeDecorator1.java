





import java.util.List;
import java.util.ArrayList;

public class decorators_TestEdgeDecorator1 extends EdgeDecorator {

    private String edgeURI;
    private String nodeBURI;
    private String nodeAURI;



    public decorators_TestEdgeDecorator1(
        String edgeURI,        String nodeBURI,        String nodeAURI    ) {
        super(
        );
        this.edgeURI = edgeURI;
        this.nodeBURI = nodeBURI;
        this.nodeAURI = nodeAURI;
    }


    public String getEdgeuri() {
        return edgeURI;
    }

    public void setEdgeuri(String edgeURI) {
        this.edgeURI = edgeURI;
    }
    public String getNodeburi() {
        return nodeBURI;
    }

    public void setNodeburi(String nodeBURI) {
        this.nodeBURI = nodeBURI;
    }
    public String getNodeauri() {
        return nodeAURI;
    }

    public void setNodeauri(String nodeAURI) {
        this.nodeAURI = nodeAURI;
    }


}