





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_DataInputAssociation extends DataAssociation {






    private bpmnprof_ThrowEvent bpmnprof_throwevent;




    private bpmnprof_BPMNActivity bpmnprof_bpmnactivity;


    public bpmnprof_DataInputAssociation(
    ) {
        super(
        );
    }



    public bpmnprof_ThrowEvent getBpmnprof_throwevent() {
        return bpmnprof_throwevent;
    }

    public void setBpmnprof_throwevent(bpmnprof_ThrowEvent bpmnprof_throwevent) {
        this.bpmnprof_throwevent = bpmnprof_throwevent;
    }
    public bpmnprof_BPMNActivity getBpmnprof_bpmnactivity() {
        return bpmnprof_bpmnactivity;
    }

    public void setBpmnprof_bpmnactivity(bpmnprof_BPMNActivity bpmnprof_bpmnactivity) {
        this.bpmnprof_bpmnactivity = bpmnprof_bpmnactivity;
    }

}