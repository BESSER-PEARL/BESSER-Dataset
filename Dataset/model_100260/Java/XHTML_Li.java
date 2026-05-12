





import java.util.List;
import java.util.ArrayList;

public class XHTML_Li extends Attrs {






    private List<Flow> flows;


    public XHTML_Li(
    ) {
        super(
        );
        this.flows = new ArrayList<>();
    }

    public XHTML_Li(
        ArrayList<Flow> flows    ) {
        this.flows = flows;
    }


    public List<Flow> getFlows() {
        return flows;
    }

    public void addFlow(Flow flow) {
        this.flows.add(flow);
    }

}