





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CatchEvent extends Event {

    private boolean parallelMultiple;





    private List<bpmn2_DataOutputAssociation> bpmn2_dataoutputassociations;




    private List<bpmn2_DataOutput> bpmn2_dataoutputs;




    private bpmn2_OutputSet bpmn2_outputset;




    private List<bpmn2_EventDefinition> bpmn2_eventdefinitions;




    private List<bpmn2_EventDefinition> bpmn2_eventdefinitions;


    public bpmn2_CatchEvent(
        boolean parallelMultiple    ) {
        super(
        );
        this.parallelMultiple = parallelMultiple;
        this.bpmn2_dataoutputassociations = new ArrayList<>();
        this.bpmn2_dataoutputs = new ArrayList<>();
        this.bpmn2_eventdefinitions = new ArrayList<>();
        this.bpmn2_eventdefinitions = new ArrayList<>();
    }

    public bpmn2_CatchEvent(
        boolean parallelMultiple        ArrayList<bpmn2_DataOutputAssociation> bpmn2_dataoutputassociations,        ArrayList<bpmn2_DataOutput> bpmn2_dataoutputs,        ArrayList<bpmn2_EventDefinition> bpmn2_eventdefinitions,        ArrayList<bpmn2_EventDefinition> bpmn2_eventdefinitions    ) {
        this.parallelMultiple = parallelMultiple;
        this.bpmn2_dataoutputassociations = bpmn2_dataoutputassociations;
        this.bpmn2_dataoutputs = bpmn2_dataoutputs;
        this.bpmn2_eventdefinitions = bpmn2_eventdefinitions;
        this.bpmn2_eventdefinitions = bpmn2_eventdefinitions;
    }

    public boolean getParallelmultiple() {
        return parallelMultiple;
    }

    public void setParallelmultiple(boolean parallelMultiple) {
        this.parallelMultiple = parallelMultiple;
    }

    public List<bpmn2_DataOutputAssociation> getBpmn2_dataoutputassociations() {
        return bpmn2_dataoutputassociations;
    }

    public void addBpmn2_dataoutputassociation(Bpmn2_dataoutputassociation bpmn2_dataoutputassociation) {
        this.bpmn2_dataoutputassociations.add(bpmn2_dataoutputassociation);
    }
    public List<bpmn2_DataOutput> getBpmn2_dataoutputs() {
        return bpmn2_dataoutputs;
    }

    public void addBpmn2_dataoutput(Bpmn2_dataoutput bpmn2_dataoutput) {
        this.bpmn2_dataoutputs.add(bpmn2_dataoutput);
    }
    public bpmn2_OutputSet getBpmn2_outputset() {
        return bpmn2_outputset;
    }

    public void setBpmn2_outputset(bpmn2_OutputSet bpmn2_outputset) {
        this.bpmn2_outputset = bpmn2_outputset;
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

}