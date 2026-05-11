





import java.util.List;
import java.util.ArrayList;

public class actions_TimedConditionAction extends core_AbstractModelElement, core_ITopLevelElement, rules_IRealTimeConsumer {

    private int frequency;



    public actions_TimedConditionAction(
        int frequency    ) {
        super(
        );
        this.frequency = frequency;
    }


    public int getFrequency() {
        return frequency;
    }

    public void setFrequency(int frequency) {
        this.frequency = frequency;
    }


}