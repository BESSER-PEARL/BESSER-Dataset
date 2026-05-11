





import java.util.List;
import java.util.ArrayList;

public class bpmn2_MultiInstanceLoopCharacteristics extends LoopCharacteristics {

    private boolean isSequential;
    private String behavior;



    public bpmn2_MultiInstanceLoopCharacteristics(
        boolean isSequential,        String behavior    ) {
        super(
        );
        this.isSequential = isSequential;
        this.behavior = behavior;
    }


    public boolean getIssequential() {
        return isSequential;
    }

    public void setIssequential(boolean isSequential) {
        this.isSequential = isSequential;
    }
    public String getBehavior() {
        return behavior;
    }

    public void setBehavior(String behavior) {
        this.behavior = behavior;
    }


}