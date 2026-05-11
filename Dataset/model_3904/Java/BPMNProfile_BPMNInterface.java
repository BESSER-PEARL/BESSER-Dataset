





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNInterface extends RootElement {






    private List<BPMNProfile_CallableElement> bpmnprofile_callableelements;




    private BPMNProfile_CallableElement bpmnprofile_callableelement;


    public BPMNProfile_BPMNInterface(
    ) {
        super(
        );
        this.bpmnprofile_callableelements = new ArrayList<>();
    }

    public BPMNProfile_BPMNInterface(
        ArrayList<BPMNProfile_CallableElement> bpmnprofile_callableelements    ) {
        this.bpmnprofile_callableelements = bpmnprofile_callableelements;
    }


    public List<BPMNProfile_CallableElement> getBpmnprofile_callableelements() {
        return bpmnprofile_callableelements;
    }

    public void addBpmnprofile_callableelement(Bpmnprofile_callableelement bpmnprofile_callableelement) {
        this.bpmnprofile_callableelements.add(bpmnprofile_callableelement);
    }
    public BPMNProfile_CallableElement getBpmnprofile_callableelement() {
        return bpmnprofile_callableelement;
    }

    public void setBpmnprofile_callableelement(BPMNProfile_CallableElement bpmnprofile_callableelement) {
        this.bpmnprofile_callableelement = bpmnprofile_callableelement;
    }

}