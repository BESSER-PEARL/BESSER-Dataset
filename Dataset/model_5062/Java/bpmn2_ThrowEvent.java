





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ThrowEvent extends Event {






    private List<bpmn2_EventDefinition> bpmn2_eventdefinitions;




    private List<bpmn2_EventDefinition> bpmn2_eventdefinitions;




    private bpmn2_InputSet bpmn2_inputset;




    private List<bpmn2_DataInput> bpmn2_datainputs;




    private List<bpmn2_DataInputAssociation> bpmn2_datainputassociations;


    public bpmn2_ThrowEvent(
    ) {
        super(
        );
        this.bpmn2_eventdefinitions = new ArrayList<>();
        this.bpmn2_eventdefinitions = new ArrayList<>();
        this.bpmn2_datainputs = new ArrayList<>();
        this.bpmn2_datainputassociations = new ArrayList<>();
    }

    public bpmn2_ThrowEvent(
        ArrayList<bpmn2_EventDefinition> bpmn2_eventdefinitions,        ArrayList<bpmn2_EventDefinition> bpmn2_eventdefinitions,        ArrayList<bpmn2_DataInput> bpmn2_datainputs,        ArrayList<bpmn2_DataInputAssociation> bpmn2_datainputassociations    ) {
        this.bpmn2_eventdefinitions = bpmn2_eventdefinitions;
        this.bpmn2_eventdefinitions = bpmn2_eventdefinitions;
        this.bpmn2_datainputs = bpmn2_datainputs;
        this.bpmn2_datainputassociations = bpmn2_datainputassociations;
    }


    public List<bpmn2_EventDefinition> getBpmn2_eventdefinitions() {
        return bpmn2_eventdefinitions;
    }

    public void addBpmn2_eventdefinition(Bpmn2_eventdefinition bpmn2_eventdefinition) {
        this.bpmn2_eventdefinitions.add(bpmn2_eventdefinition);
    }
    public List<bpmn2_EventDefinition> getBpmn2_eventdefinitions() {
        return bpmn2_eventdefinitions;
    }

    public void addBpmn2_eventdefinition(Bpmn2_eventdefinition bpmn2_eventdefinition) {
        this.bpmn2_eventdefinitions.add(bpmn2_eventdefinition);
    }
    public bpmn2_InputSet getBpmn2_inputset() {
        return bpmn2_inputset;
    }

    public void setBpmn2_inputset(bpmn2_InputSet bpmn2_inputset) {
        this.bpmn2_inputset = bpmn2_inputset;
    }
    public List<bpmn2_DataInput> getBpmn2_datainputs() {
        return bpmn2_datainputs;
    }

    public void addBpmn2_datainput(Bpmn2_datainput bpmn2_datainput) {
        this.bpmn2_datainputs.add(bpmn2_datainput);
    }
    public List<bpmn2_DataInputAssociation> getBpmn2_datainputassociations() {
        return bpmn2_datainputassociations;
    }

    public void addBpmn2_datainputassociation(Bpmn2_datainputassociation bpmn2_datainputassociation) {
        this.bpmn2_datainputassociations.add(bpmn2_datainputassociation);
    }

}