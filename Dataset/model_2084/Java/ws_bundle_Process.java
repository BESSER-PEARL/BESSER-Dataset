





import java.util.List;
import java.util.ArrayList;

public class ws_bundle_Process  {

    private String ID;





    private Middleware middleware;




    private List<Node> nodes;


    public ws_bundle_Process(
        String ID    ) {
        this.ID = ID;
        this.nodes = new ArrayList<>();
    }

    public ws_bundle_Process(
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

    public Middleware getMiddleware() {
        return middleware;
    }

    public void setMiddleware(Middleware middleware) {
        this.middleware = middleware;
    }
    public List<Node> getNodes() {
        return nodes;
    }

    public void addNode(Node node) {
        this.nodes.add(node);
    }

}