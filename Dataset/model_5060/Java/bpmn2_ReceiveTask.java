





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ReceiveTask extends Task {

    private boolean instantiate;
    private String implementation;



    public bpmn2_ReceiveTask(
        boolean instantiate,        String implementation    ) {
        super(
        );
        this.instantiate = instantiate;
        this.implementation = implementation;
    }


    public boolean getInstantiate() {
        return instantiate;
    }

    public void setInstantiate(boolean instantiate) {
        this.instantiate = instantiate;
    }
    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }


}