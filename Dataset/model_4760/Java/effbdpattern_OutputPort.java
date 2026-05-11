





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_OutputPort extends Port {






    private effbdpattern_Function effbdpattern_function;




    private List<effbdpattern_Flow> effbdpattern_flows;


    public effbdpattern_OutputPort(
    ) {
        super(
        );
        this.effbdpattern_flows = new ArrayList<>();
    }

    public effbdpattern_OutputPort(
        ArrayList<effbdpattern_Flow> effbdpattern_flows    ) {
        this.effbdpattern_flows = effbdpattern_flows;
    }


    public effbdpattern_Function getEffbdpattern_function() {
        return effbdpattern_function;
    }

    public void setEffbdpattern_function(effbdpattern_Function effbdpattern_function) {
        this.effbdpattern_function = effbdpattern_function;
    }
    public List<effbdpattern_Flow> getEffbdpattern_flows() {
        return effbdpattern_flows;
    }

    public void addEffbdpattern_flow(Effbdpattern_flow effbdpattern_flow) {
        this.effbdpattern_flows.add(effbdpattern_flow);
    }

}