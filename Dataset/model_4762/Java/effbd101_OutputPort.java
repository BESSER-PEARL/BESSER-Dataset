





import java.util.List;
import java.util.ArrayList;

public class effbd101_OutputPort extends Port {






    private List<effbd101_Flow> effbd101_flows;




    private effbd101_Function effbd101_function;


    public effbd101_OutputPort(
    ) {
        super(
        );
        this.effbd101_flows = new ArrayList<>();
    }

    public effbd101_OutputPort(
        ArrayList<effbd101_Flow> effbd101_flows    ) {
        this.effbd101_flows = effbd101_flows;
    }


    public List<effbd101_Flow> getEffbd101_flows() {
        return effbd101_flows;
    }

    public void addEffbd101_flow(Effbd101_flow effbd101_flow) {
        this.effbd101_flows.add(effbd101_flow);
    }
    public effbd101_Function getEffbd101_function() {
        return effbd101_function;
    }

    public void setEffbd101_function(effbd101_Function effbd101_function) {
        this.effbd101_function = effbd101_function;
    }

}