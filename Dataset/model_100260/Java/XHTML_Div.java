





import java.util.List;
import java.util.ArrayList;

public class XHTML_Div extends Attrs, block, ButtonContent {






    private List<Flow> flows;


    public XHTML_Div(
    ) {
        super(
        );
        this.flows = new ArrayList<>();
    }

    public XHTML_Div(
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