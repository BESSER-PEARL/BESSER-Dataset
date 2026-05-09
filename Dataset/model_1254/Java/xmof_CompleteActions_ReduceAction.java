





import java.util.List;
import java.util.ArrayList;

public class xmof_CompleteActions_ReduceAction extends Action {

    private boolean ordered;





    private BasicActions_OutputPin basicactions_outputpin;




    private BasicActions_InputPin basicactions_inputpin;




    private BasicBehaviors_Behavior basicbehaviors_behavior;


    public xmof_CompleteActions_ReduceAction(
        boolean ordered    ) {
        super(
        );
        this.ordered = ordered;
    }


    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }

    public BasicActions_OutputPin getBasicactions_outputpin() {
        return basicactions_outputpin;
    }

    public void setBasicactions_outputpin(BasicActions_OutputPin basicactions_outputpin) {
        this.basicactions_outputpin = basicactions_outputpin;
    }
    public BasicActions_InputPin getBasicactions_inputpin() {
        return basicactions_inputpin;
    }

    public void setBasicactions_inputpin(BasicActions_InputPin basicactions_inputpin) {
        this.basicactions_inputpin = basicactions_inputpin;
    }
    public BasicBehaviors_Behavior getBasicbehaviors_behavior() {
        return basicbehaviors_behavior;
    }

    public void setBasicbehaviors_behavior(BasicBehaviors_Behavior basicbehaviors_behavior) {
        this.basicbehaviors_behavior = basicbehaviors_behavior;
    }

}