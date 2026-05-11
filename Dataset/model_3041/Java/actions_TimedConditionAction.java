





import java.util.List;
import java.util.ArrayList;

public class actions_TimedConditionAction extends rules_IRealTimeConsumer, core_AbstractModelElement, core_ITopLevelElement {

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