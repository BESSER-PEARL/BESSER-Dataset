





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNProperty extends ItemAwareElement {






    private BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess;




    private BPMNProfile_DataStoreNode bpmnprofile_datastorenode;




    private BPMNProfile_BPMNEvent bpmnprofile_bpmnevent;




    private BPMNProfile_Property bpmnprofile_property;




    private BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity;


    public BPMNProfile_BPMNProperty(
    ) {
        super(
        );
    }



    public BPMNProfile_BPMNProcess getBpmnprofile_bpmnprocess() {
        return bpmnprofile_bpmnprocess;
    }

    public void setBpmnprofile_bpmnprocess(BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess) {
        this.bpmnprofile_bpmnprocess = bpmnprofile_bpmnprocess;
    }
    public BPMNProfile_DataStoreNode getBpmnprofile_datastorenode() {
        return bpmnprofile_datastorenode;
    }

    public void setBpmnprofile_datastorenode(BPMNProfile_DataStoreNode bpmnprofile_datastorenode) {
        this.bpmnprofile_datastorenode = bpmnprofile_datastorenode;
    }
    public BPMNProfile_BPMNEvent getBpmnprofile_bpmnevent() {
        return bpmnprofile_bpmnevent;
    }

    public void setBpmnprofile_bpmnevent(BPMNProfile_BPMNEvent bpmnprofile_bpmnevent) {
        this.bpmnprofile_bpmnevent = bpmnprofile_bpmnevent;
    }
    public BPMNProfile_Property getBpmnprofile_property() {
        return bpmnprofile_property;
    }

    public void setBpmnprofile_property(BPMNProfile_Property bpmnprofile_property) {
        this.bpmnprofile_property = bpmnprofile_property;
    }
    public BPMNProfile_BPMNActivity getBpmnprofile_bpmnactivity() {
        return bpmnprofile_bpmnactivity;
    }

    public void setBpmnprofile_bpmnactivity(BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity) {
        this.bpmnprofile_bpmnactivity = bpmnprofile_bpmnactivity;
    }

}