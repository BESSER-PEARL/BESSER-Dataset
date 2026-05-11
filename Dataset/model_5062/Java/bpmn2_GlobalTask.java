





import java.util.List;
import java.util.ArrayList;

public class bpmn2_GlobalTask extends CallableElement {






    private List<bpmn2_ResourceRole> bpmn2_resourceroles;


    public bpmn2_GlobalTask(
    ) {
        super(
        );
        this.bpmn2_resourceroles = new ArrayList<>();
    }

    public bpmn2_GlobalTask(
        ArrayList<bpmn2_ResourceRole> bpmn2_resourceroles    ) {
        this.bpmn2_resourceroles = bpmn2_resourceroles;
    }


    public List<bpmn2_ResourceRole> getBpmn2_resourceroles() {
        return bpmn2_resourceroles;
    }

    public void addBpmn2_resourcerole(Bpmn2_resourcerole bpmn2_resourcerole) {
        this.bpmn2_resourceroles.add(bpmn2_resourcerole);
    }

}