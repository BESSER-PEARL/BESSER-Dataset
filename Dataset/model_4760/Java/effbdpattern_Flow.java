





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_Flow  {

    private String flowName;





    private effbdpattern_Function effbdpattern_function;


    public effbdpattern_Flow(
        String flowName    ) {
        this.flowName = flowName;
    }


    public String getFlowname() {
        return flowName;
    }

    public void setFlowname(String flowName) {
        this.flowName = flowName;
    }

    public effbdpattern_Function getEffbdpattern_function() {
        return effbdpattern_function;
    }

    public void setEffbdpattern_function(effbdpattern_Function effbdpattern_function) {
        this.effbdpattern_function = effbdpattern_function;
    }

}