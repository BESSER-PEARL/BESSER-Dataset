





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ItemDefinition extends RootElement {

    private String itemKind;
    private String isCollection;





    private BPMNProfile_Import bpmnprofile_import;




    private BPMNProfile_DataStore bpmnprofile_datastore;


    public BPMNProfile_ItemDefinition(
        String itemKind,        String isCollection    ) {
        super(
        );
        this.itemKind = itemKind;
        this.isCollection = isCollection;
    }


    public String getItemkind() {
        return itemKind;
    }

    public void setItemkind(String itemKind) {
        this.itemKind = itemKind;
    }
    public String getIscollection() {
        return isCollection;
    }

    public void setIscollection(String isCollection) {
        this.isCollection = isCollection;
    }

    public BPMNProfile_Import getBpmnprofile_import() {
        return bpmnprofile_import;
    }

    public void setBpmnprofile_import(BPMNProfile_Import bpmnprofile_import) {
        this.bpmnprofile_import = bpmnprofile_import;
    }
    public BPMNProfile_DataStore getBpmnprofile_datastore() {
        return bpmnprofile_datastore;
    }

    public void setBpmnprofile_datastore(BPMNProfile_DataStore bpmnprofile_datastore) {
        this.bpmnprofile_datastore = bpmnprofile_datastore;
    }

}