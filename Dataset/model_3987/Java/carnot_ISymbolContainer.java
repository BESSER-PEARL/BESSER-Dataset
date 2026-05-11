





import java.util.List;
import java.util.ArrayList;

public class carnot_ISymbolContainer extends IExtensibleElement {

    private String connections;
    private String nodes;



    public carnot_ISymbolContainer(
        String connections,        String nodes    ) {
        super(
        );
        this.connections = connections;
        this.nodes = nodes;
    }


    public String getConnections() {
        return connections;
    }

    public void setConnections(String connections) {
        this.connections = connections;
    }
    public String getNodes() {
        return nodes;
    }

    public void setNodes(String nodes) {
        this.nodes = nodes;
    }


}