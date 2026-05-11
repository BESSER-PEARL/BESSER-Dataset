





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_GlobalTask extends CallableElement {






    private List<BPMN2Model_ResourceRole> bpmn2model_resourceroles;


    public BPMN2Model_GlobalTask(
    ) {
        super(
        );
        this.bpmn2model_resourceroles = new ArrayList<>();
    }

    public BPMN2Model_GlobalTask(
        ArrayList<BPMN2Model_ResourceRole> bpmn2model_resourceroles    ) {
        this.bpmn2model_resourceroles = bpmn2model_resourceroles;
    }


    public List<BPMN2Model_ResourceRole> getBpmn2model_resourceroles() {
        return bpmn2model_resourceroles;
    }

    public void addBpmn2model_resourcerole(Bpmn2model_resourcerole bpmn2model_resourcerole) {
        this.bpmn2model_resourceroles.add(bpmn2model_resourcerole);
    }

}