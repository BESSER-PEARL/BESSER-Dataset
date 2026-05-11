





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNActivity extends FlowNode, InteractionNode {

    private String completionQuantity;
    private String isForCompensation;
    private String startQuantity;





    private BPMNProfile_Action bpmnprofile_action;




    private List<BPMNProfile_ResourceRole> bpmnprofile_resourceroles;




    private List<BPMNProfile_BPMNProperty> bpmnprofile_bpmnpropertys;


    public BPMNProfile_BPMNActivity(
        String completionQuantity,        String isForCompensation,        String startQuantity    ) {
        super(
        );
        this.completionQuantity = completionQuantity;
        this.isForCompensation = isForCompensation;
        this.startQuantity = startQuantity;
        this.bpmnprofile_resourceroles = new ArrayList<>();
        this.bpmnprofile_bpmnpropertys = new ArrayList<>();
    }

    public BPMNProfile_BPMNActivity(
        String completionQuantity,        String isForCompensation,        String startQuantity        ArrayList<BPMNProfile_ResourceRole> bpmnprofile_resourceroles,        ArrayList<BPMNProfile_BPMNProperty> bpmnprofile_bpmnpropertys    ) {
        this.completionQuantity = completionQuantity;
        this.isForCompensation = isForCompensation;
        this.startQuantity = startQuantity;
        this.bpmnprofile_resourceroles = bpmnprofile_resourceroles;
        this.bpmnprofile_bpmnpropertys = bpmnprofile_bpmnpropertys;
    }

    public String getCompletionquantity() {
        return completionQuantity;
    }

    public void setCompletionquantity(String completionQuantity) {
        this.completionQuantity = completionQuantity;
    }
    public String getIsforcompensation() {
        return isForCompensation;
    }

    public void setIsforcompensation(String isForCompensation) {
        this.isForCompensation = isForCompensation;
    }
    public String getStartquantity() {
        return startQuantity;
    }

    public void setStartquantity(String startQuantity) {
        this.startQuantity = startQuantity;
    }

    public BPMNProfile_Action getBpmnprofile_action() {
        return bpmnprofile_action;
    }

    public void setBpmnprofile_action(BPMNProfile_Action bpmnprofile_action) {
        this.bpmnprofile_action = bpmnprofile_action;
    }
    public List<BPMNProfile_ResourceRole> getBpmnprofile_resourceroles() {
        return bpmnprofile_resourceroles;
    }

    public void addBpmnprofile_resourcerole(Bpmnprofile_resourcerole bpmnprofile_resourcerole) {
        this.bpmnprofile_resourceroles.add(bpmnprofile_resourcerole);
    }
    public List<BPMNProfile_BPMNProperty> getBpmnprofile_bpmnpropertys() {
        return bpmnprofile_bpmnpropertys;
    }

    public void addBpmnprofile_bpmnproperty(Bpmnprofile_bpmnproperty bpmnprofile_bpmnproperty) {
        this.bpmnprofile_bpmnpropertys.add(bpmnprofile_bpmnproperty);
    }

}