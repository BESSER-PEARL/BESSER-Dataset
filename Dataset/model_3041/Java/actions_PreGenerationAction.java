





import java.util.List;
import java.util.ArrayList;

public class actions_PreGenerationAction extends Action {






    private actions_PreGenerationSequence actions_pregenerationsequence;




    private actions_StandAloneAction actions_standaloneaction;




    private actions_TimedConditionAction actions_timedconditionaction;


    public actions_PreGenerationAction(
    ) {
        super(
        );
    }



    public actions_PreGenerationSequence getActions_pregenerationsequence() {
        return actions_pregenerationsequence;
    }

    public void setActions_pregenerationsequence(actions_PreGenerationSequence actions_pregenerationsequence) {
        this.actions_pregenerationsequence = actions_pregenerationsequence;
    }
    public actions_StandAloneAction getActions_standaloneaction() {
        return actions_standaloneaction;
    }

    public void setActions_standaloneaction(actions_StandAloneAction actions_standaloneaction) {
        this.actions_standaloneaction = actions_standaloneaction;
    }
    public actions_TimedConditionAction getActions_timedconditionaction() {
        return actions_timedconditionaction;
    }

    public void setActions_timedconditionaction(actions_TimedConditionAction actions_timedconditionaction) {
        this.actions_timedconditionaction = actions_timedconditionaction;
    }

}