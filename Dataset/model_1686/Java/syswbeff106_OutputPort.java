





import java.util.List;
import java.util.ArrayList;

public class syswbeff106_OutputPort extends Port {






    private List<syswbeff106_Flow> syswbeff106_flows;




    private syswbeff106_Function syswbeff106_function;


    public syswbeff106_OutputPort(
    ) {
        super(
        );
        this.syswbeff106_flows = new ArrayList<>();
    }

    public syswbeff106_OutputPort(
        ArrayList<syswbeff106_Flow> syswbeff106_flows    ) {
        this.syswbeff106_flows = syswbeff106_flows;
    }


    public List<syswbeff106_Flow> getSyswbeff106_flows() {
        return syswbeff106_flows;
    }

    public void addSyswbeff106_flow(Syswbeff106_flow syswbeff106_flow) {
        this.syswbeff106_flows.add(syswbeff106_flow);
    }
    public syswbeff106_Function getSyswbeff106_function() {
        return syswbeff106_function;
    }

    public void setSyswbeff106_function(syswbeff106_Function syswbeff106_function) {
        this.syswbeff106_function = syswbeff106_function;
    }

}