





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ThrowEvent extends Event {






    private List<bpmn2_EventDefinition> bpmn2_eventdefinitions;




    private List<bpmn2_DataInputAssociation> bpmn2_datainputassociations;




    private List<bpmn2_EventDefinition> bpmn2_eventdefinitions;


    public bpmn2_ThrowEvent(
    ) {
        super(
        );
        this.bpmn2_eventdefinitions = new ArrayList<>();
        this.bpmn2_datainputassociations = new ArrayList<>();
        this.bpmn2_eventdefinitions = new ArrayList<>();
    }

    public bpmn2_ThrowEvent(
        ArrayList<bpmn2_EventDefinition> bpmn2_eventdefinitions,        ArrayList<bpmn2_DataInputAssociation> bpmn2_datainputassociations,        ArrayList<bpmn2_EventDefinition> bpmn2_eventdefinitions    ) {
        this.bpmn2_eventdefinitions = bpmn2_eventdefinitions;
        this.bpmn2_datainputassociations = bpmn2_datainputassociations;
        this.bpmn2_eventdefinitions = bpmn2_eventdefinitions;
    }


    public List<bpmn2_EventDefinition> getBpmn2_eventdefinitions() {
        return bpmn2_eventdefinitions;
    }

    public void addBpmn2_eventdefinition(Bpmn2_eventdefinition bpmn2_eventdefinition) {
        this.bpmn2_eventdefinitions.add(bpmn2_eventdefinition);
    }
    public List<bpmn2_DataInputAssociation> getBpmn2_datainputassociations() {
        return bpmn2_datainputassociations;
    }

    public void addBpmn2_datainputassociation(Bpmn2_datainputassociation bpmn2_datainputassociation) {
        this.bpmn2_datainputassociations.add(bpmn2_datainputassociation);
    }
    public List<bpmn2_EventDefinition> getBpmn2_eventdefinitions() {
        return bpmn2_eventdefinitions;
    }

    public void addBpmn2_eventdefinition(Bpmn2_eventdefinition bpmn2_eventdefinition) {
        this.bpmn2_eventdefinitions.add(bpmn2_eventdefinition);
    }

}