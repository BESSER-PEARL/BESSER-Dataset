





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_DataObject extends ItemAwareElement, FlowElement {

    private String isCollection;





    private BPMNProfile_DataObjectReference bpmnprofile_dataobjectreference;




    private BPMNProfile_DataStoreNode bpmnprofile_datastorenode;


    public BPMNProfile_DataObject(
        String isCollection    ) {
        super(
        );
        this.isCollection = isCollection;
    }


    public String getIscollection() {
        return isCollection;
    }

    public void setIscollection(String isCollection) {
        this.isCollection = isCollection;
    }

    public BPMNProfile_DataObjectReference getBpmnprofile_dataobjectreference() {
        return bpmnprofile_dataobjectreference;
    }

    public void setBpmnprofile_dataobjectreference(BPMNProfile_DataObjectReference bpmnprofile_dataobjectreference) {
        this.bpmnprofile_dataobjectreference = bpmnprofile_dataobjectreference;
    }
    public BPMNProfile_DataStoreNode getBpmnprofile_datastorenode() {
        return bpmnprofile_datastorenode;
    }

    public void setBpmnprofile_datastorenode(BPMNProfile_DataStoreNode bpmnprofile_datastorenode) {
        this.bpmnprofile_datastorenode = bpmnprofile_datastorenode;
    }

}