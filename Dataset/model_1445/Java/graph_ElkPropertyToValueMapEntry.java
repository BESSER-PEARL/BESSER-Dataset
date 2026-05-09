





import java.util.List;
import java.util.ArrayList;

public class graph_ElkPropertyToValueMapEntry  {

    private String value;
    private String key;





    private graph_EMapPropertyHolder graph_emappropertyholder;


    public graph_ElkPropertyToValueMapEntry(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public graph_EMapPropertyHolder getGraph_emappropertyholder() {
        return graph_emappropertyholder;
    }

    public void setGraph_emappropertyholder(graph_EMapPropertyHolder graph_emappropertyholder) {
        this.graph_emappropertyholder = graph_emappropertyholder;
    }

}