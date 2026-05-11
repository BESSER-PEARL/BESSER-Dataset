





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_CatchEvent extends BPMNEvent {

    private String parallelMultiple;



    public bpmnprof_CatchEvent(
        String parallelMultiple    ) {
        super(
        );
        this.parallelMultiple = parallelMultiple;
    }


    public String getParallelmultiple() {
        return parallelMultiple;
    }

    public void setParallelmultiple(String parallelMultiple) {
        this.parallelMultiple = parallelMultiple;
    }


}