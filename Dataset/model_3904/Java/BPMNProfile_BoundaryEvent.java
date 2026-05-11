





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BoundaryEvent extends CatchEvent {

    private String cancelActivity;





    private BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity;




    private BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity;


    public BPMNProfile_BoundaryEvent(
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

    public BPMNProfile_BPMNActivity getBpmnprofile_bpmnactivity() {
        return bpmnprofile_bpmnactivity;
    }

    public void setBpmnprofile_bpmnactivity(BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity) {
        this.bpmnprofile_bpmnactivity = bpmnprofile_bpmnactivity;
    }
    public BPMNProfile_BPMNActivity getBpmnprofile_bpmnactivity() {
        return bpmnprofile_bpmnactivity;
    }

    public void setBpmnprofile_bpmnactivity(BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity) {
        this.bpmnprofile_bpmnactivity = bpmnprofile_bpmnactivity;
    }

}