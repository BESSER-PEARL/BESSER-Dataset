





import java.util.List;
import java.util.ArrayList;

public class syswbeff1065ok_Flow extends ProcessNode {






    private List<syswbeff1065ok_InputPort> syswbeff1065ok_inputports;




    private syswbeff1065ok_Function syswbeff1065ok_function;


    public syswbeff1065ok_Flow(
    ) {
        super(
        );
        this.syswbeff1065ok_inputports = new ArrayList<>();
    }

    public syswbeff1065ok_Flow(
        ArrayList<syswbeff1065ok_InputPort> syswbeff1065ok_inputports    ) {
        this.syswbeff1065ok_inputports = syswbeff1065ok_inputports;
    }


    public List<syswbeff1065ok_InputPort> getSyswbeff1065ok_inputports() {
        return syswbeff1065ok_inputports;
    }

    public void addSyswbeff1065ok_inputport(Syswbeff1065ok_inputport syswbeff1065ok_inputport) {
        this.syswbeff1065ok_inputports.add(syswbeff1065ok_inputport);
    }
    public syswbeff1065ok_Function getSyswbeff1065ok_function() {
        return syswbeff1065ok_function;
    }

    public void setSyswbeff1065ok_function(syswbeff1065ok_Function syswbeff1065ok_function) {
        this.syswbeff1065ok_function = syswbeff1065ok_function;
    }

}