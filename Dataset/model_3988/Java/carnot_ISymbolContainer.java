





import java.util.List;
import java.util.ArrayList;

public class carnot_ISymbolContainer extends IExtensibleElement {

    private String nodes;
    private String connections;



    public carnot_ISymbolContainer(
        String nodes,        String connections    ) {
        super(
        );
        this.nodes = nodes;
        this.connections = connections;
    }


    public String getNodes() {
        return nodes;
    }

    public void setNodes(String nodes) {
        this.nodes = nodes;
    }
    public String getConnections() {
        return connections;
    }

    public void setConnections(String connections) {
        this.connections = connections;
    }


}