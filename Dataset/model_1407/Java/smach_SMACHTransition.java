





import java.util.List;
import java.util.ArrayList;

public class smach_SMACHTransition  {

    private String name;





    private smach_SMACHStateMachine smach_smachstatemachine;




    private smach_SMACHState smach_smachstate;




    private smach_SMACHState smach_smachstate;


    public smach_SMACHTransition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smach_SMACHStateMachine getSmach_smachstatemachine() {
        return smach_smachstatemachine;
    }

    public void setSmach_smachstatemachine(smach_SMACHStateMachine smach_smachstatemachine) {
        this.smach_smachstatemachine = smach_smachstatemachine;
    }
    public smach_SMACHState getSmach_smachstate() {
        return smach_smachstate;
    }

    public void setSmach_smachstate(smach_SMACHState smach_smachstate) {
        this.smach_smachstate = smach_smachstate;
    }
    public smach_SMACHState getSmach_smachstate() {
        return smach_smachstate;
    }

    public void setSmach_smachstate(smach_SMACHState smach_smachstate) {
        this.smach_smachstate = smach_smachstate;
    }

}