





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_BoundaryEvent extends CatchEvent {

    private String cancelActivity;





    private bpmnprof_BPMNActivity bpmnprof_bpmnactivity;




    private bpmnprof_BPMNActivity bpmnprof_bpmnactivity;


    public bpmnprof_BoundaryEvent(
        String cancelActivity    ) {
        super(
        );
        this.cancelActivity = cancelActivity;
    }


    public String getCancelactivity() {
        return cancelActivity;
    }

    public void setCancelactivity(String cancelActivity) {
        this.cancelActivity = cancelActivity;
    }

    public bpmnprof_BPMNActivity getBpmnprof_bpmnactivity() {
        return bpmnprof_bpmnactivity;
    }

    public void setBpmnprof_bpmnactivity(bpmnprof_BPMNActivity bpmnprof_bpmnactivity) {
        this.bpmnprof_bpmnactivity = bpmnprof_bpmnactivity;
    }
    public bpmnprof_BPMNActivity getBpmnprof_bpmnactivity() {
        return bpmnprof_bpmnactivity;
    }

    public void setBpmnprof_bpmnactivity(bpmnprof_BPMNActivity bpmnprof_bpmnactivity) {
        this.bpmnprof_bpmnactivity = bpmnprof_bpmnactivity;
    }

}