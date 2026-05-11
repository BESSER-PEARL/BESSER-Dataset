





import java.util.List;
import java.util.ArrayList;

public class effbd902_OutputPort extends Port {






    private List<effbd902_Flow> effbd902_flows;




    private effbd902_Function effbd902_function;


    public effbd902_OutputPort(
    ) {
        super(
        );
        this.effbd902_flows = new ArrayList<>();
    }

    public effbd902_OutputPort(
        ArrayList<effbd902_Flow> effbd902_flows    ) {
        this.effbd902_flows = effbd902_flows;
    }


    public List<effbd902_Flow> getEffbd902_flows() {
        return effbd902_flows;
    }

    public void addEffbd902_flow(Effbd902_flow effbd902_flow) {
        this.effbd902_flows.add(effbd902_flow);
    }
    public effbd902_Function getEffbd902_function() {
        return effbd902_function;
    }

    public void setEffbd902_function(effbd902_Function effbd902_function) {
        this.effbd902_function = effbd902_function;
    }

}