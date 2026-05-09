





import java.util.List;
import java.util.ArrayList;

public class graph_StringToObjectMapEntry  {

    private String key;
    private String value;





    private graph_GGraph graph_ggraph;


    public graph_StringToObjectMapEntry(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public graph_GGraph getGraph_ggraph() {
        return graph_ggraph;
    }

    public void setGraph_ggraph(graph_GGraph graph_ggraph) {
        this.graph_ggraph = graph_ggraph;
    }

}