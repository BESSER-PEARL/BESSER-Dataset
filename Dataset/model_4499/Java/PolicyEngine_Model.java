





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_Model extends NamedElement {






    private List<PolicyEngine_Timer> policyengine_timers;


    public PolicyEngine_Model(
    ) {
        super(
        );
        this.policyengine_timers = new ArrayList<>();
    }

    public PolicyEngine_Model(
        ArrayList<PolicyEngine_Timer> policyengine_timers    ) {
        this.policyengine_timers = policyengine_timers;
    }


    public List<PolicyEngine_Timer> getPolicyengine_timers() {
        return policyengine_timers;
    }

    public void addPolicyengine_timer(Policyengine_timer policyengine_timer) {
        this.policyengine_timers.add(policyengine_timer);
    }

}