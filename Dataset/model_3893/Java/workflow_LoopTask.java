





import java.util.List;
import java.util.ArrayList;

public class workflow_LoopTask extends CompoundTask {

    private String whileCondition;



    public workflow_LoopTask(
        String whileCondition    ) {
        super(
        );
        this.whileCondition = whileCondition;
    }


    public String getWhilecondition() {
        return whileCondition;
    }

    public void setWhilecondition(String whileCondition) {
        this.whileCondition = whileCondition;
    }


}