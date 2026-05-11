





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_Room extends NamedElement {






    private PolicyEngine_Model policyengine_model;




    private PolicyEngine_Room policyengine_room;




    private List<PolicyEngine_Timer> policyengine_timers;




    private PolicyEngine_Floor policyengine_floor;


    public PolicyEngine_Room(
    ) {
        super(
        );
        this.policyengine_timers = new ArrayList<>();
    }

    public PolicyEngine_Room(
        ArrayList<PolicyEngine_Timer> policyengine_timers    ) {
        this.policyengine_timers = policyengine_timers;
    }


    public PolicyEngine_Model getPolicyengine_model() {
        return policyengine_model;
    }

    public void setPolicyengine_model(PolicyEngine_Model policyengine_model) {
        this.policyengine_model = policyengine_model;
    }
    public PolicyEngine_Room getPolicyengine_room() {
        return policyengine_room;
    }

    public void setPolicyengine_room(PolicyEngine_Room policyengine_room) {
        this.policyengine_room = policyengine_room;
    }
    public List<PolicyEngine_Timer> getPolicyengine_timers() {
        return policyengine_timers;
    }

    public void addPolicyengine_timer(Policyengine_timer policyengine_timer) {
        this.policyengine_timers.add(policyengine_timer);
    }
    public PolicyEngine_Floor getPolicyengine_floor() {
        return policyengine_floor;
    }

    public void setPolicyengine_floor(PolicyEngine_Floor policyengine_floor) {
        this.policyengine_floor = policyengine_floor;
    }

}