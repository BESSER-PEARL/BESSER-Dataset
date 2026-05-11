





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_Policy extends NamedElement {






    private PolicyEngine_Room policyengine_room;




    private List<PolicyEngine_Room> policyengine_rooms;




    private List<PolicyEngine_Timer> policyengine_timers;




    private PolicyEngine_Model policyengine_model;


    public PolicyEngine_Policy(
    ) {
        super(
        );
        this.policyengine_rooms = new ArrayList<>();
        this.policyengine_timers = new ArrayList<>();
    }

    public PolicyEngine_Policy(
        ArrayList<PolicyEngine_Room> policyengine_rooms,        ArrayList<PolicyEngine_Timer> policyengine_timers    ) {
        this.policyengine_rooms = policyengine_rooms;
        this.policyengine_timers = policyengine_timers;
    }


    public PolicyEngine_Room getPolicyengine_room() {
        return policyengine_room;
    }

    public void setPolicyengine_room(PolicyEngine_Room policyengine_room) {
        this.policyengine_room = policyengine_room;
    }
    public List<PolicyEngine_Room> getPolicyengine_rooms() {
        return policyengine_rooms;
    }

    public void addPolicyengine_room(Policyengine_room policyengine_room) {
        this.policyengine_rooms.add(policyengine_room);
    }
    public List<PolicyEngine_Timer> getPolicyengine_timers() {
        return policyengine_timers;
    }

    public void addPolicyengine_timer(Policyengine_timer policyengine_timer) {
        this.policyengine_timers.add(policyengine_timer);
    }
    public PolicyEngine_Model getPolicyengine_model() {
        return policyengine_model;
    }

    public void setPolicyengine_model(PolicyEngine_Model policyengine_model) {
        this.policyengine_model = policyengine_model;
    }

}