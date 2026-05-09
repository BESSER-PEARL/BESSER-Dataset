





import java.util.List;
import java.util.ArrayList;

public class syswbeff1065ok_OutputPort extends Port {






    private List<syswbeff1065ok_Flow> syswbeff1065ok_flows;




    private syswbeff1065ok_Function syswbeff1065ok_function;


    public syswbeff1065ok_OutputPort(
    ) {
        super(
        );
        this.syswbeff1065ok_flows = new ArrayList<>();
    }

    public syswbeff1065ok_OutputPort(
        ArrayList<syswbeff1065ok_Flow> syswbeff1065ok_flows    ) {
        this.syswbeff1065ok_flows = syswbeff1065ok_flows;
    }


    public List<syswbeff1065ok_Flow> getSyswbeff1065ok_flows() {
        return syswbeff1065ok_flows;
    }

    public void addSyswbeff1065ok_flow(Syswbeff1065ok_flow syswbeff1065ok_flow) {
        this.syswbeff1065ok_flows.add(syswbeff1065ok_flow);
    }
    public syswbeff1065ok_Function getSyswbeff1065ok_function() {
        return syswbeff1065ok_function;
    }

    public void setSyswbeff1065ok_function(syswbeff1065ok_Function syswbeff1065ok_function) {
        this.syswbeff1065ok_function = syswbeff1065ok_function;
    }

}