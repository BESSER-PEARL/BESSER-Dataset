





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_ReceiveTask extends Task {

    private String instantiate;
    private String implementation;



    public bpmnprof_ReceiveTask(
        String instantiate,        String implementation    ) {
        super(
        );
        this.instantiate = instantiate;
        this.implementation = implementation;
    }


    public String getInstantiate() {
        return instantiate;
    }

    public void setInstantiate(String instantiate) {
        this.instantiate = instantiate;
    }
    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }


}