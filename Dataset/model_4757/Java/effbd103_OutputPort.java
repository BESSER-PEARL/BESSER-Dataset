





import java.util.List;
import java.util.ArrayList;

public class effbd103_OutputPort extends Port {






    private List<effbd103_Flow> effbd103_flows;


    public effbd103_OutputPort(
    ) {
        super(
        );
        this.effbd103_flows = new ArrayList<>();
    }

    public effbd103_OutputPort(
        ArrayList<effbd103_Flow> effbd103_flows    ) {
        this.effbd103_flows = effbd103_flows;
    }


    public List<effbd103_Flow> getEffbd103_flows() {
        return effbd103_flows;
    }

    public void addEffbd103_flow(Effbd103_flow effbd103_flow) {
        this.effbd103_flows.add(effbd103_flow);
    }

}