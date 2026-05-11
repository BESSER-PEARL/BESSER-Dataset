





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ReceiveTask extends Task {

    private String implementation;
    private boolean instantiate;



    public bpmn2_ReceiveTask(
        String implementation,        boolean instantiate    ) {
        super(
        );
        this.implementation = implementation;
        this.instantiate = instantiate;
    }


    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }
    public boolean getInstantiate() {
        return instantiate;
    }

    public void setInstantiate(boolean instantiate) {
        this.instantiate = instantiate;
    }


}