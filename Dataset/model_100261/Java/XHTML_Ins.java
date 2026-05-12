





import java.util.List;
import java.util.ArrayList;

public class XHTML_Ins extends Miscinline, Attrs {






    private URI uri;




    private List<Flow> flows;


    public XHTML_Ins(
    ) {
        super(
        );
        this.flows = new ArrayList<>();
    }

    public XHTML_Ins(
        ArrayList<Flow> flows    ) {
        this.flows = flows;
    }


    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }
    public List<Flow> getFlows() {
        return flows;
    }

    public void addFlow(Flow flow) {
        this.flows.add(flow);
    }

}