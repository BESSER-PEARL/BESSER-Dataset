





import java.util.List;
import java.util.ArrayList;

public class rsgf_bundle_Process  {

    private String ID;





    private List<Node> nodes;


    public rsgf_bundle_Process(
        String ID    ) {
        this.ID = ID;
        this.nodes = new ArrayList<>();
    }

    public rsgf_bundle_Process(
        String ID        ArrayList<Node> nodes    ) {
        this.ID = ID;
        this.nodes = nodes;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public List<Node> getNodes() {
        return nodes;
    }

    public void addNode(Node node) {
        this.nodes.add(node);
    }

}