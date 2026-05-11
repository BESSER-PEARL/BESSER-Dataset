





import java.util.List;
import java.util.ArrayList;

public class fault_tree_IntermediateEvent extends Event {






    private fault_tree_Event fault_tree_event;




    private fault_tree_Event fault_tree_event;




    private fault_tree_FailureInstance fault_tree_failureinstance;




    private fault_tree_BasicEvent fault_tree_basicevent;




    private List<fault_tree_FailureInstance> fault_tree_failureinstances;




    private fault_tree_Hazard fault_tree_hazard;


    public fault_tree_IntermediateEvent(
    ) {
        super(
        );
        this.fault_tree_failureinstances = new ArrayList<>();
    }

    public fault_tree_IntermediateEvent(
        ArrayList<fault_tree_FailureInstance> fault_tree_failureinstances    ) {
        this.fault_tree_failureinstances = fault_tree_failureinstances;
    }


    public fault_tree_Event getFault_tree_event() {
        return fault_tree_event;
    }

    public void setFault_tree_event(fault_tree_Event fault_tree_event) {
        this.fault_tree_event = fault_tree_event;
    }
    public fault_tree_Event getFault_tree_event() {
        return fault_tree_event;
    }

    public void setFault_tree_event(fault_tree_Event fault_tree_event) {
        this.fault_tree_event = fault_tree_event;
    }
    public fault_tree_FailureInstance getFault_tree_failureinstance() {
        return fault_tree_failureinstance;
    }

    public void setFault_tree_failureinstance(fault_tree_FailureInstance fault_tree_failureinstance) {
        this.fault_tree_failureinstance = fault_tree_failureinstance;
    }
    public fault_tree_BasicEvent getFault_tree_basicevent() {
        return fault_tree_basicevent;
    }

    public void setFault_tree_basicevent(fault_tree_BasicEvent fault_tree_basicevent) {
        this.fault_tree_basicevent = fault_tree_basicevent;
    }
    public List<fault_tree_FailureInstance> getFault_tree_failureinstances() {
        return fault_tree_failureinstances;
    }

    public void addFault_tree_failureinstance(Fault_tree_failureinstance fault_tree_failureinstance) {
        this.fault_tree_failureinstances.add(fault_tree_failureinstance);
    }
    public fault_tree_Hazard getFault_tree_hazard() {
        return fault_tree_hazard;
    }

    public void setFault_tree_hazard(fault_tree_Hazard fault_tree_hazard) {
        this.fault_tree_hazard = fault_tree_hazard;
    }

}