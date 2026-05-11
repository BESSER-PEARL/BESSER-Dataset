





import java.util.List;
import java.util.ArrayList;

public class effbd104_OutputPort extends Port {






    private List<effbd104_Flow> effbd104_flows;




    private effbd104_Function effbd104_function;


    public effbd104_OutputPort(
    ) {
        super(
        );
        this.effbd104_flows = new ArrayList<>();
    }

    public effbd104_OutputPort(
        ArrayList<effbd104_Flow> effbd104_flows    ) {
        this.effbd104_flows = effbd104_flows;
    }


    public List<effbd104_Flow> getEffbd104_flows() {
        return effbd104_flows;
    }

    public void addEffbd104_flow(Effbd104_flow effbd104_flow) {
        this.effbd104_flows.add(effbd104_flow);
    }
    public effbd104_Function getEffbd104_function() {
        return effbd104_function;
    }

    public void setEffbd104_function(effbd104_Function effbd104_function) {
        this.effbd104_function = effbd104_function;
    }

}