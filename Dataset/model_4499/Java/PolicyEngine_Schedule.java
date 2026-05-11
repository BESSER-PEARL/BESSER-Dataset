





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_Schedule extends NamedElement {

    private String weekdays;





    private PolicyEngine_Model policyengine_model;




    private PolicyEngine_Policy policyengine_policy;




    private PolicyEngine_Room policyengine_room;


    public PolicyEngine_Schedule(
        String weekdays    ) {
        super(
        );
        this.weekdays = weekdays;
    }


    public String getWeekdays() {
        return weekdays;
    }

    public void setWeekdays(String weekdays) {
        this.weekdays = weekdays;
    }

    public PolicyEngine_Model getPolicyengine_model() {
        return policyengine_model;
    }

    public void setPolicyengine_model(PolicyEngine_Model policyengine_model) {
        this.policyengine_model = policyengine_model;
    }
    public PolicyEngine_Policy getPolicyengine_policy() {
        return policyengine_policy;
    }

    public void setPolicyengine_policy(PolicyEngine_Policy policyengine_policy) {
        this.policyengine_policy = policyengine_policy;
    }
    public PolicyEngine_Room getPolicyengine_room() {
        return policyengine_room;
    }

    public void setPolicyengine_room(PolicyEngine_Room policyengine_room) {
        this.policyengine_room = policyengine_room;
    }

}