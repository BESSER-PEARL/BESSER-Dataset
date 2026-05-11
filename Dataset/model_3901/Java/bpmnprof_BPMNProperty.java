





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_BPMNProperty extends ItemAwareElement {






    private bpmnprof_BPMNActivity bpmnprof_bpmnactivity;




    private bpmnprof_Property bpmnprof_property;




    private bpmnprof_BPMNEvent bpmnprof_bpmnevent;


    public bpmnprof_BPMNProperty(
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
    public bpmnprof_Property getBpmnprof_property() {
        return bpmnprof_property;
    }

    public void setBpmnprof_property(bpmnprof_Property bpmnprof_property) {
        this.bpmnprof_property = bpmnprof_property;
    }
    public bpmnprof_BPMNEvent getBpmnprof_bpmnevent() {
        return bpmnprof_bpmnevent;
    }

    public void setBpmnprof_bpmnevent(bpmnprof_BPMNEvent bpmnprof_bpmnevent) {
        this.bpmnprof_bpmnevent = bpmnprof_bpmnevent;
    }

}