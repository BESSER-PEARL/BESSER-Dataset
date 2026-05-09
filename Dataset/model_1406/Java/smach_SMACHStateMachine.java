





import java.util.List;
import java.util.ArrayList;

public class smach_SMACHStateMachine extends Node {

    private boolean SkillInterface;



    public smach_SMACHStateMachine(
        boolean SkillInterface    ) {
        super(
        );
        this.SkillInterface = SkillInterface;
    }


    public boolean getSkillinterface() {
        return SkillInterface;
    }

    public void setSkillinterface(boolean SkillInterface) {
        this.SkillInterface = SkillInterface;
    }


}