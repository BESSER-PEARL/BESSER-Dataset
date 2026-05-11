





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataStoreReference extends FlowElement, ItemAwareElement {






    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_DataStore bpmn2_datastore;


    public bpmn2_DataStoreReference(
    ) {
        super(
        );
    }



    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_DataStore getBpmn2_datastore() {
        return bpmn2_datastore;
    }

    public void setBpmn2_datastore(bpmn2_DataStore bpmn2_datastore) {
        this.bpmn2_datastore = bpmn2_datastore;
    }

}