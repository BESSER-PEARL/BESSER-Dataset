





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_MultiInstanceLoopCharacteristics extends LoopCharacteristics {

    private String behavior;
    private String isSequential;



    public bpmnprof_MultiInstanceLoopCharacteristics(
        String behavior,        String isSequential    ) {
        super(
        );
        this.behavior = behavior;
        this.isSequential = isSequential;
    }


    public String getBehavior() {
        return behavior;
    }

    public void setBehavior(String behavior) {
        this.behavior = behavior;
    }
    public String getIssequential() {
        return isSequential;
    }

    public void setIssequential(String isSequential) {
        this.isSequential = isSequential;
    }


}