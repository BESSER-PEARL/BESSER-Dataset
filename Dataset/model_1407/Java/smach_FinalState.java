





import java.util.List;
import java.util.ArrayList;

public class smach_FinalState extends SMACHState {

    private String type;





    private smach_SMACHStateMachine smach_smachstatemachine;


    public smach_FinalState(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public smach_SMACHStateMachine getSmach_smachstatemachine() {
        return smach_smachstatemachine;
    }

    public void setSmach_smachstatemachine(smach_SMACHStateMachine smach_smachstatemachine) {
        this.smach_smachstatemachine = smach_smachstatemachine;
    }

}