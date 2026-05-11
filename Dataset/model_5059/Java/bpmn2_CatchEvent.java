





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CatchEvent extends Event {

    private boolean parallelMultiple;





    private List<bpmn2_EventDefinition> bpmn2_eventdefinitions;




    private List<bpmn2_EventDefinition> bpmn2_eventdefinitions;




    private List<bpmn2_DataOutputAssociation> bpmn2_dataoutputassociations;


    public bpmn2_CatchEvent(
        boolean parallelMultiple    ) {
        super(
        );
        this.parallelMultiple = parallelMultiple;
        this.bpmn2_eventdefinitions = new ArrayList<>();
        this.bpmn2_eventdefinitions = new ArrayList<>();
        this.bpmn2_dataoutputassociations = new ArrayList<>();
    }

    public bpmn2_CatchEvent(
        boolean parallelMultiple        ArrayList<bpmn2_EventDefinition> bpmn2_eventdefinitions,        ArrayList<bpmn2_EventDefinition> bpmn2_eventdefinitions,        ArrayList<bpmn2_DataOutputAssociation> bpmn2_dataoutputassociations    ) {
        this.parallelMultiple = parallelMultiple;
        this.bpmn2_eventdefinitions = bpmn2_eventdefinitions;
        this.bpmn2_eventdefinitions = bpmn2_eventdefinitions;
        this.bpmn2_dataoutputassociations = bpmn2_dataoutputassociations;
    }

    public boolean getParallelmultiple() {
        return parallelMultiple;
    }

    public void setParallelmultiple(boolean parallelMultiple) {
        this.parallelMultiple = parallelMultiple;
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
    public List<bpmn2_DataOutputAssociation> getBpmn2_dataoutputassociations() {
        return bpmn2_dataoutputassociations;
    }

    public void addBpmn2_dataoutputassociation(Bpmn2_dataoutputassociation bpmn2_dataoutputassociation) {
        this.bpmn2_dataoutputassociations.add(bpmn2_dataoutputassociation);
    }

}