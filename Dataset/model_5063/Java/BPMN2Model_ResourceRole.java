





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ResourceRole extends BaseElement {

    private String name;





    private BPMN2Model_ResourceAssignmentExpression bpmn2model_resourceassignmentexpression;




    private BPMN2Model_Process bpmn2model_process;




    private List<BPMN2Model_ResourceParameterBinding> bpmn2model_resourceparameterbindings;




    private BPMN2Model_Resource bpmn2model_resource;




    private BPMN2Model_Activity bpmn2model_activity;


    public BPMN2Model_ResourceRole(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2model_resourceparameterbindings = new ArrayList<>();
    }

    public BPMN2Model_ResourceRole(
        String name        ArrayList<BPMN2Model_ResourceParameterBinding> bpmn2model_resourceparameterbindings    ) {
        this.name = name;
        this.bpmn2model_resourceparameterbindings = bpmn2model_resourceparameterbindings;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BPMN2Model_ResourceAssignmentExpression getBpmn2model_resourceassignmentexpression() {
        return bpmn2model_resourceassignmentexpression;
    }

    public void setBpmn2model_resourceassignmentexpression(BPMN2Model_ResourceAssignmentExpression bpmn2model_resourceassignmentexpression) {
        this.bpmn2model_resourceassignmentexpression = bpmn2model_resourceassignmentexpression;
    }
    public BPMN2Model_Process getBpmn2model_process() {
        return bpmn2model_process;
    }

    public void setBpmn2model_process(BPMN2Model_Process bpmn2model_process) {
        this.bpmn2model_process = bpmn2model_process;
    }
    public List<BPMN2Model_ResourceParameterBinding> getBpmn2model_resourceparameterbindings() {
        return bpmn2model_resourceparameterbindings;
    }

    public void addBpmn2model_resourceparameterbinding(Bpmn2model_resourceparameterbinding bpmn2model_resourceparameterbinding) {
        this.bpmn2model_resourceparameterbindings.add(bpmn2model_resourceparameterbinding);
    }
    public BPMN2Model_Resource getBpmn2model_resource() {
        return bpmn2model_resource;
    }

    public void setBpmn2model_resource(BPMN2Model_Resource bpmn2model_resource) {
        this.bpmn2model_resource = bpmn2model_resource;
    }
    public BPMN2Model_Activity getBpmn2model_activity() {
        return bpmn2model_activity;
    }

    public void setBpmn2model_activity(BPMN2Model_Activity bpmn2model_activity) {
        this.bpmn2model_activity = bpmn2model_activity;
    }

}