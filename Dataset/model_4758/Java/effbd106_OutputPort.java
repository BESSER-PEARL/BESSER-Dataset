





import java.util.List;
import java.util.ArrayList;

public class effbd106_OutputPort extends Port {






    private List<effbd106_Flow> effbd106_flows;


    public effbd106_OutputPort(
    ) {
        super(
        );
        this.effbd106_flows = new ArrayList<>();
    }

    public effbd106_OutputPort(
        ArrayList<effbd106_Flow> effbd106_flows    ) {
        this.effbd106_flows = effbd106_flows;
    }


    public List<effbd106_Flow> getEffbd106_flows() {
        return effbd106_flows;
    }

    public void addEffbd106_flow(Effbd106_flow effbd106_flow) {
        this.effbd106_flows.add(effbd106_flow);
    }

}