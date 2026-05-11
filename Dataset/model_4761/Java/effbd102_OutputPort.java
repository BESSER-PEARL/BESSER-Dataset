





import java.util.List;
import java.util.ArrayList;

public class effbd102_OutputPort extends Port {






    private List<effbd102_Flow> effbd102_flows;


    public effbd102_OutputPort(
    ) {
        super(
        );
        this.effbd102_flows = new ArrayList<>();
    }

    public effbd102_OutputPort(
        ArrayList<effbd102_Flow> effbd102_flows    ) {
        this.effbd102_flows = effbd102_flows;
    }


    public List<effbd102_Flow> getEffbd102_flows() {
        return effbd102_flows;
    }

    public void addEffbd102_flow(Effbd102_flow effbd102_flow) {
        this.effbd102_flows.add(effbd102_flow);
    }

}