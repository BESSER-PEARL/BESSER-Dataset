





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ResourceRole extends BaseElement {






    private BPMNProfile_Resource bpmnprofile_resource;




    private List<BPMNProfile_ResourceParameterBinding> bpmnprofile_resourceparameterbindings;




    private BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity;




    private BPMNProfile_ResourceAssignmentExpression bpmnprofile_resourceassignmentexpression;




    private BPMNProfile_GlobalTask bpmnprofile_globaltask;


    public BPMNProfile_ResourceRole(
    ) {
        super(
        );
        this.bpmnprofile_resourceparameterbindings = new ArrayList<>();
    }

    public BPMNProfile_ResourceRole(
        ArrayList<BPMNProfile_ResourceParameterBinding> bpmnprofile_resourceparameterbindings    ) {
        this.bpmnprofile_resourceparameterbindings = bpmnprofile_resourceparameterbindings;
    }


    public BPMNProfile_Resource getBpmnprofile_resource() {
        return bpmnprofile_resource;
    }

    public void setBpmnprofile_resource(BPMNProfile_Resource bpmnprofile_resource) {
        this.bpmnprofile_resource = bpmnprofile_resource;
    }
    public List<BPMNProfile_ResourceParameterBinding> getBpmnprofile_resourceparameterbindings() {
        return bpmnprofile_resourceparameterbindings;
    }

    public void addBpmnprofile_resourceparameterbinding(Bpmnprofile_resourceparameterbinding bpmnprofile_resourceparameterbinding) {
        this.bpmnprofile_resourceparameterbindings.add(bpmnprofile_resourceparameterbinding);
    }
    public BPMNProfile_BPMNActivity getBpmnprofile_bpmnactivity() {
        return bpmnprofile_bpmnactivity;
    }

    public void setBpmnprofile_bpmnactivity(BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity) {
        this.bpmnprofile_bpmnactivity = bpmnprofile_bpmnactivity;
    }
    public BPMNProfile_ResourceAssignmentExpression getBpmnprofile_resourceassignmentexpression() {
        return bpmnprofile_resourceassignmentexpression;
    }

    public void setBpmnprofile_resourceassignmentexpression(BPMNProfile_ResourceAssignmentExpression bpmnprofile_resourceassignmentexpression) {
        this.bpmnprofile_resourceassignmentexpression = bpmnprofile_resourceassignmentexpression;
    }
    public BPMNProfile_GlobalTask getBpmnprofile_globaltask() {
        return bpmnprofile_globaltask;
    }

    public void setBpmnprofile_globaltask(BPMNProfile_GlobalTask bpmnprofile_globaltask) {
        this.bpmnprofile_globaltask = bpmnprofile_globaltask;
    }

}