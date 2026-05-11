





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_CallableElement extends RootElement {






    private List<BPMNProfile_InputOutputBinding> bpmnprofile_inputoutputbindings;




    private List<BPMNProfile_BPMNInterface> bpmnprofile_bpmninterfaces;




    private BPMNProfile_CallActivity bpmnprofile_callactivity;




    private BPMNProfile_InputOutputSpecification bpmnprofile_inputoutputspecification;




    private BPMNProfile_BPMNInterface bpmnprofile_bpmninterface;




    private BPMNProfile_Behavior bpmnprofile_behavior;


    public BPMNProfile_CallableElement(
    ) {
        super(
        );
        this.bpmnprofile_inputoutputbindings = new ArrayList<>();
        this.bpmnprofile_bpmninterfaces = new ArrayList<>();
    }

    public BPMNProfile_CallableElement(
        ArrayList<BPMNProfile_InputOutputBinding> bpmnprofile_inputoutputbindings,        ArrayList<BPMNProfile_BPMNInterface> bpmnprofile_bpmninterfaces    ) {
        this.bpmnprofile_inputoutputbindings = bpmnprofile_inputoutputbindings;
        this.bpmnprofile_bpmninterfaces = bpmnprofile_bpmninterfaces;
    }


    public List<BPMNProfile_InputOutputBinding> getBpmnprofile_inputoutputbindings() {
        return bpmnprofile_inputoutputbindings;
    }

    public void addBpmnprofile_inputoutputbinding(Bpmnprofile_inputoutputbinding bpmnprofile_inputoutputbinding) {
        this.bpmnprofile_inputoutputbindings.add(bpmnprofile_inputoutputbinding);
    }
    public List<BPMNProfile_BPMNInterface> getBpmnprofile_bpmninterfaces() {
        return bpmnprofile_bpmninterfaces;
    }

    public void addBpmnprofile_bpmninterface(Bpmnprofile_bpmninterface bpmnprofile_bpmninterface) {
        this.bpmnprofile_bpmninterfaces.add(bpmnprofile_bpmninterface);
    }
    public BPMNProfile_CallActivity getBpmnprofile_callactivity() {
        return bpmnprofile_callactivity;
    }

    public void setBpmnprofile_callactivity(BPMNProfile_CallActivity bpmnprofile_callactivity) {
        this.bpmnprofile_callactivity = bpmnprofile_callactivity;
    }
    public BPMNProfile_InputOutputSpecification getBpmnprofile_inputoutputspecification() {
        return bpmnprofile_inputoutputspecification;
    }

    public void setBpmnprofile_inputoutputspecification(BPMNProfile_InputOutputSpecification bpmnprofile_inputoutputspecification) {
        this.bpmnprofile_inputoutputspecification = bpmnprofile_inputoutputspecification;
    }
    public BPMNProfile_BPMNInterface getBpmnprofile_bpmninterface() {
        return bpmnprofile_bpmninterface;
    }

    public void setBpmnprofile_bpmninterface(BPMNProfile_BPMNInterface bpmnprofile_bpmninterface) {
        this.bpmnprofile_bpmninterface = bpmnprofile_bpmninterface;
    }
    public BPMNProfile_Behavior getBpmnprofile_behavior() {
        return bpmnprofile_behavior;
    }

    public void setBpmnprofile_behavior(BPMNProfile_Behavior bpmnprofile_behavior) {
        this.bpmnprofile_behavior = bpmnprofile_behavior;
    }

}