





import java.util.List;
import java.util.ArrayList;

public class XHTML_Dd extends DlElement {






    private List<Flow> flows;


    public XHTML_Dd(
    ) {
        super(
        );
        this.flows = new ArrayList<>();
    }

    public XHTML_Dd(
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