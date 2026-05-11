





import java.util.List;
import java.util.ArrayList;

public class fault_tree_FaultTree extends IDBase {






    private fault_tree_FailureType fault_tree_failuretype;




    private fault_tree_ErrorType fault_tree_errortype;




    private List<fault_tree_ErrorType> fault_tree_errortypes;




    private fault_tree_Event fault_tree_event;




    private List<fault_tree_Event> fault_tree_events;




    private List<fault_tree_FailureType> fault_tree_failuretypes;




    private fault_tree_Gate fault_tree_gate;




    private List<fault_tree_Gate> fault_tree_gates;


    public fault_tree_FaultTree(
    ) {
        super(
        );
        this.fault_tree_errortypes = new ArrayList<>();
        this.fault_tree_events = new ArrayList<>();
        this.fault_tree_failuretypes = new ArrayList<>();
        this.fault_tree_gates = new ArrayList<>();
    }

    public fault_tree_FaultTree(
        ArrayList<fault_tree_ErrorType> fault_tree_errortypes,        ArrayList<fault_tree_Event> fault_tree_events,        ArrayList<fault_tree_FailureType> fault_tree_failuretypes,        ArrayList<fault_tree_Gate> fault_tree_gates    ) {
        this.fault_tree_errortypes = fault_tree_errortypes;
        this.fault_tree_events = fault_tree_events;
        this.fault_tree_failuretypes = fault_tree_failuretypes;
        this.fault_tree_gates = fault_tree_gates;
    }


    public fault_tree_FailureType getFault_tree_failuretype() {
        return fault_tree_failuretype;
    }

    public void setFault_tree_failuretype(fault_tree_FailureType fault_tree_failuretype) {
        this.fault_tree_failuretype = fault_tree_failuretype;
    }
    public fault_tree_ErrorType getFault_tree_errortype() {
        return fault_tree_errortype;
    }

    public void setFault_tree_errortype(fault_tree_ErrorType fault_tree_errortype) {
        this.fault_tree_errortype = fault_tree_errortype;
    }
    public List<fault_tree_ErrorType> getFault_tree_errortypes() {
        return fault_tree_errortypes;
    }

    public void addFault_tree_errortype(Fault_tree_errortype fault_tree_errortype) {
        this.fault_tree_errortypes.add(fault_tree_errortype);
    }
    public fault_tree_Event getFault_tree_event() {
        return fault_tree_event;
    }

    public void setFault_tree_event(fault_tree_Event fault_tree_event) {
        this.fault_tree_event = fault_tree_event;
    }
    public List<fault_tree_Event> getFault_tree_events() {
        return fault_tree_events;
    }

    public void addFault_tree_event(Fault_tree_event fault_tree_event) {
        this.fault_tree_events.add(fault_tree_event);
    }
    public List<fault_tree_FailureType> getFault_tree_failuretypes() {
        return fault_tree_failuretypes;
    }

    public void addFault_tree_failuretype(Fault_tree_failuretype fault_tree_failuretype) {
        this.fault_tree_failuretypes.add(fault_tree_failuretype);
    }
    public fault_tree_Gate getFault_tree_gate() {
        return fault_tree_gate;
    }

    public void setFault_tree_gate(fault_tree_Gate fault_tree_gate) {
        this.fault_tree_gate = fault_tree_gate;
    }
    public List<fault_tree_Gate> getFault_tree_gates() {
        return fault_tree_gates;
    }

    public void addFault_tree_gate(Fault_tree_gate fault_tree_gate) {
        this.fault_tree_gates.add(fault_tree_gate);
    }

}