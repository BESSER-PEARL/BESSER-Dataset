





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_Building extends NamedElement {






    private PolicyEngine_CalendarSystem policyengine_calendarsystem;




    private PolicyEngine_MeetingScheduleSystem policyengine_meetingschedulesystem;




    private List<PolicyEngine_Floor> policyengine_floors;




    private PolicyEngine_Model policyengine_model;




    private List<PolicyEngine_Timer> policyengine_timers;


    public PolicyEngine_Building(
    ) {
        super(
        );
        this.policyengine_floors = new ArrayList<>();
        this.policyengine_timers = new ArrayList<>();
    }

    public PolicyEngine_Building(
        ArrayList<PolicyEngine_Floor> policyengine_floors,        ArrayList<PolicyEngine_Timer> policyengine_timers    ) {
        this.policyengine_floors = policyengine_floors;
        this.policyengine_timers = policyengine_timers;
    }


    public PolicyEngine_CalendarSystem getPolicyengine_calendarsystem() {
        return policyengine_calendarsystem;
    }

    public void setPolicyengine_calendarsystem(PolicyEngine_CalendarSystem policyengine_calendarsystem) {
        this.policyengine_calendarsystem = policyengine_calendarsystem;
    }
    public PolicyEngine_MeetingScheduleSystem getPolicyengine_meetingschedulesystem() {
        return policyengine_meetingschedulesystem;
    }

    public void setPolicyengine_meetingschedulesystem(PolicyEngine_MeetingScheduleSystem policyengine_meetingschedulesystem) {
        this.policyengine_meetingschedulesystem = policyengine_meetingschedulesystem;
    }
    public List<PolicyEngine_Floor> getPolicyengine_floors() {
        return policyengine_floors;
    }

    public void addPolicyengine_floor(Policyengine_floor policyengine_floor) {
        this.policyengine_floors.add(policyengine_floor);
    }
    public PolicyEngine_Model getPolicyengine_model() {
        return policyengine_model;
    }

    public void setPolicyengine_model(PolicyEngine_Model policyengine_model) {
        this.policyengine_model = policyengine_model;
    }
    public List<PolicyEngine_Timer> getPolicyengine_timers() {
        return policyengine_timers;
    }

    public void addPolicyengine_timer(Policyengine_timer policyengine_timer) {
        this.policyengine_timers.add(policyengine_timer);
    }

}