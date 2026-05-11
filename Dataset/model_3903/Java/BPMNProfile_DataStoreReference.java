





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_DataStoreReference extends ItemAwareElement, FlowElement {






    private BPMNProfile_DataStore bpmnprofile_datastore;




    private BPMNProfile_DataStoreNode bpmnprofile_datastorenode;


    public BPMNProfile_DataStoreReference(
    ) {
        super(
        );
    }



    public BPMNProfile_DataStore getBpmnprofile_datastore() {
        return bpmnprofile_datastore;
    }

    public void setBpmnprofile_datastore(BPMNProfile_DataStore bpmnprofile_datastore) {
        this.bpmnprofile_datastore = bpmnprofile_datastore;
    }
    public BPMNProfile_DataStoreNode getBpmnprofile_datastorenode() {
        return bpmnprofile_datastorenode;
    }

    public void setBpmnprofile_datastorenode(BPMNProfile_DataStoreNode bpmnprofile_datastorenode) {
        this.bpmnprofile_datastorenode = bpmnprofile_datastorenode;
    }

}