





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_DataOutputAssociation extends DataAssociation {






    private bpmnprof_BPMNActivity bpmnprof_bpmnactivity;




    private bpmnprof_CatchEvent bpmnprof_catchevent;


    public bpmnprof_DataOutputAssociation(
    ) {
        super(
        );
    }



    public bpmnprof_BPMNActivity getBpmnprof_bpmnactivity() {
        return bpmnprof_bpmnactivity;
    }

    public void setBpmnprof_bpmnactivity(bpmnprof_BPMNActivity bpmnprof_bpmnactivity) {
        this.bpmnprof_bpmnactivity = bpmnprof_bpmnactivity;
    }
    public bpmnprof_CatchEvent getBpmnprof_catchevent() {
        return bpmnprof_catchevent;
    }

    public void setBpmnprof_catchevent(bpmnprof_CatchEvent bpmnprof_catchevent) {
        this.bpmnprof_catchevent = bpmnprof_catchevent;
    }

}