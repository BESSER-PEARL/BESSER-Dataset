





import java.util.List;
import java.util.ArrayList;

public class bpmn2_InputOutputSpecification extends BaseElement {






    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_Activity bpmn2_activity;




    private List<bpmn2_DataInput> bpmn2_datainputs;




    private List<bpmn2_InputSet> bpmn2_inputsets;




    private List<bpmn2_DataOutput> bpmn2_dataoutputs;




    private bpmn2_CallableElement bpmn2_callableelement;


    public bpmn2_InputOutputSpecification(
    ) {
        super(
        );
        this.bpmn2_datainputs = new ArrayList<>();
        this.bpmn2_inputsets = new ArrayList<>();
        this.bpmn2_dataoutputs = new ArrayList<>();
    }

    public bpmn2_InputOutputSpecification(
        ArrayList<bpmn2_DataInput> bpmn2_datainputs,        ArrayList<bpmn2_InputSet> bpmn2_inputsets,        ArrayList<bpmn2_DataOutput> bpmn2_dataoutputs    ) {
        this.bpmn2_datainputs = bpmn2_datainputs;
        this.bpmn2_inputsets = bpmn2_inputsets;
        this.bpmn2_dataoutputs = bpmn2_dataoutputs;
    }


    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_Activity getBpmn2_activity() {
        return bpmn2_activity;
    }

    public void setBpmn2_activity(bpmn2_Activity bpmn2_activity) {
        this.bpmn2_activity = bpmn2_activity;
    }
    public List<bpmn2_DataInput> getBpmn2_datainputs() {
        return bpmn2_datainputs;
    }

    public void addBpmn2_datainput(Bpmn2_datainput bpmn2_datainput) {
        this.bpmn2_datainputs.add(bpmn2_datainput);
    }
    public List<bpmn2_InputSet> getBpmn2_inputsets() {
        return bpmn2_inputsets;
    }

    public void addBpmn2_inputset(Bpmn2_inputset bpmn2_inputset) {
        this.bpmn2_inputsets.add(bpmn2_inputset);
    }
    public List<bpmn2_DataOutput> getBpmn2_dataoutputs() {
        return bpmn2_dataoutputs;
    }

    public void addBpmn2_dataoutput(Bpmn2_dataoutput bpmn2_dataoutput) {
        this.bpmn2_dataoutputs.add(bpmn2_dataoutput);
    }
    public bpmn2_CallableElement getBpmn2_callableelement() {
        return bpmn2_callableelement;
    }

    public void setBpmn2_callableelement(bpmn2_CallableElement bpmn2_callableelement) {
        this.bpmn2_callableelement = bpmn2_callableelement;
    }

}