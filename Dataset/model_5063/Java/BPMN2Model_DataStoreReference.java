





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_DataStoreReference extends FlowElement, ItemAwareElement {






    private BPMN2Model_DataStore bpmn2model_datastore;


    public BPMN2Model_DataStoreReference(
    ) {
        super(
        );
    }



    public BPMN2Model_DataStore getBpmn2model_datastore() {
        return bpmn2model_datastore;
    }

    public void setBpmn2model_datastore(BPMN2Model_DataStore bpmn2model_datastore) {
        this.bpmn2model_datastore = bpmn2model_datastore;
    }

}