





import java.util.List;
import java.util.ArrayList;

public class XHTML_Del extends Attrs, Miscinline {






    private List<Flow> flows;




    private URI uri;


    public XHTML_Del(
    ) {
        super(
        );
        this.flows = new ArrayList<>();
    }

    public XHTML_Del(
        ArrayList<Flow> flows    ) {
        this.flows = flows;
    }


    public List<Flow> getFlows() {
        return flows;
    }

    public void addFlow(Flow flow) {
        this.flows.add(flow);
    }
    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }

}