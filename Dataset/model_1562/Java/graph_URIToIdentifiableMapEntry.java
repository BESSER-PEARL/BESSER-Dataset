





import java.util.List;
import java.util.ArrayList;

public class graph_URIToIdentifiableMapEntry  {

    private String key;





    private graph_Identifiable graph_identifiable;


    public graph_URIToIdentifiableMapEntry(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public graph_Identifiable getGraph_identifiable() {
        return graph_identifiable;
    }

    public void setGraph_identifiable(graph_Identifiable graph_identifiable) {
        this.graph_identifiable = graph_identifiable;
    }

}