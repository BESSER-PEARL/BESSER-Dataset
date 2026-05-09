





import java.util.List;
import java.util.ArrayList;

public class smach_SMACHState  {

    private String goal_type;
    private String goal;
    private String remap_overwrite;





    private smach_SMACHStateMachine smach_smachstatemachine;


    public smach_SMACHState(
        String goal_type,        String goal,        String remap_overwrite    ) {
        this.goal_type = goal_type;
        this.goal = goal;
        this.remap_overwrite = remap_overwrite;
    }


    public String getGoal_type() {
        return goal_type;
    }

    public void setGoal_type(String goal_type) {
        this.goal_type = goal_type;
    }
    public String getGoal() {
        return goal;
    }

    public void setGoal(String goal) {
        this.goal = goal;
    }
    public String getRemap_overwrite() {
        return remap_overwrite;
    }

    public void setRemap_overwrite(String remap_overwrite) {
        this.remap_overwrite = remap_overwrite;
    }

    public smach_SMACHStateMachine getSmach_smachstatemachine() {
        return smach_smachstatemachine;
    }

    public void setSmach_smachstatemachine(smach_SMACHStateMachine smach_smachstatemachine) {
        this.smach_smachstatemachine = smach_smachstatemachine;
    }

}