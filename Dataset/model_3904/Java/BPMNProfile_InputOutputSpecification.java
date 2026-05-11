





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_InputOutputSpecification extends BaseElement {






    private List<BPMNProfile_OutputSet> bpmnprofile_outputsets;




    private List<BPMNProfile_DataInput> bpmnprofile_datainputs;




    private List<BPMNProfile_DataOutput> bpmnprofile_dataoutputs;




    private BPMNProfile_Behavior bpmnprofile_behavior;




    private BPMNProfile_CallableElement bpmnprofile_callableelement;




    private BPMNProfile_Action bpmnprofile_action;




    private List<BPMNProfile_InputSet> bpmnprofile_inputsets;


    public BPMNProfile_InputOutputSpecification(
    ) {
        super(
        );
        this.bpmnprofile_outputsets = new ArrayList<>();
        this.bpmnprofile_datainputs = new ArrayList<>();
        this.bpmnprofile_dataoutputs = new ArrayList<>();
        this.bpmnprofile_inputsets = new ArrayList<>();
    }

    public BPMNProfile_InputOutputSpecification(
        ArrayList<BPMNProfile_OutputSet> bpmnprofile_outputsets,        ArrayList<BPMNProfile_DataInput> bpmnprofile_datainputs,        ArrayList<BPMNProfile_DataOutput> bpmnprofile_dataoutputs,        ArrayList<BPMNProfile_InputSet> bpmnprofile_inputsets    ) {
        this.bpmnprofile_outputsets = bpmnprofile_outputsets;
        this.bpmnprofile_datainputs = bpmnprofile_datainputs;
        this.bpmnprofile_dataoutputs = bpmnprofile_dataoutputs;
        this.bpmnprofile_inputsets = bpmnprofile_inputsets;
    }


    public List<BPMNProfile_OutputSet> getBpmnprofile_outputsets() {
        return bpmnprofile_outputsets;
    }

    public void addBpmnprofile_outputset(Bpmnprofile_outputset bpmnprofile_outputset) {
        this.bpmnprofile_outputsets.add(bpmnprofile_outputset);
    }
    public List<BPMNProfile_DataInput> getBpmnprofile_datainputs() {
        return bpmnprofile_datainputs;
    }

    public void addBpmnprofile_datainput(Bpmnprofile_datainput bpmnprofile_datainput) {
        this.bpmnprofile_datainputs.add(bpmnprofile_datainput);
    }
    public List<BPMNProfile_DataOutput> getBpmnprofile_dataoutputs() {
        return bpmnprofile_dataoutputs;
    }

    public void addBpmnprofile_dataoutput(Bpmnprofile_dataoutput bpmnprofile_dataoutput) {
        this.bpmnprofile_dataoutputs.add(bpmnprofile_dataoutput);
    }
    public BPMNProfile_Behavior getBpmnprofile_behavior() {
        return bpmnprofile_behavior;
    }

    public void setBpmnprofile_behavior(BPMNProfile_Behavior bpmnprofile_behavior) {
        this.bpmnprofile_behavior = bpmnprofile_behavior;
    }
    public BPMNProfile_CallableElement getBpmnprofile_callableelement() {
        return bpmnprofile_callableelement;
    }

    public void setBpmnprofile_callableelement(BPMNProfile_CallableElement bpmnprofile_callableelement) {
        this.bpmnprofile_callableelement = bpmnprofile_callableelement;
    }
    public BPMNProfile_Action getBpmnprofile_action() {
        return bpmnprofile_action;
    }

    public void setBpmnprofile_action(BPMNProfile_Action bpmnprofile_action) {
        this.bpmnprofile_action = bpmnprofile_action;
    }
    public List<BPMNProfile_InputSet> getBpmnprofile_inputsets() {
        return bpmnprofile_inputsets;
    }

    public void addBpmnprofile_inputset(Bpmnprofile_inputset bpmnprofile_inputset) {
        this.bpmnprofile_inputsets.add(bpmnprofile_inputset);
    }

}