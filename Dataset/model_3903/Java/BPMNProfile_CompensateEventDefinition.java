





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_CompensateEventDefinition extends EventDefinition {

    private String waitForCompletion;



    public BPMNProfile_CompensateEventDefinition(
        String waitForCompletion    ) {
        super(
        );
        this.waitForCompletion = waitForCompletion;
    }


    public String getWaitforcompletion() {
        return waitForCompletion;
    }

    public void setWaitforcompletion(String waitForCompletion) {
        this.waitForCompletion = waitForCompletion;
    }


}