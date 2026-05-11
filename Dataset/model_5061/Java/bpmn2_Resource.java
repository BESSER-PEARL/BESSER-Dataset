





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Resource extends RootElement {

    private String name;





    private bpmn2_ResourceRole bpmn2_resourcerole;




    private List<bpmn2_ResourceParameter> bpmn2_resourceparameters;


    public bpmn2_Resource(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_resourceparameters = new ArrayList<>();
    }

    public bpmn2_Resource(
        String name        ArrayList<bpmn2_ResourceParameter> bpmn2_resourceparameters    ) {
        this.name = name;
        this.bpmn2_resourceparameters = bpmn2_resourceparameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_ResourceRole getBpmn2_resourcerole() {
        return bpmn2_resourcerole;
    }

    public void setBpmn2_resourcerole(bpmn2_ResourceRole bpmn2_resourcerole) {
        this.bpmn2_resourcerole = bpmn2_resourcerole;
    }
    public List<bpmn2_ResourceParameter> getBpmn2_resourceparameters() {
        return bpmn2_resourceparameters;
    }

    public void addBpmn2_resourceparameter(Bpmn2_resourceparameter bpmn2_resourceparameter) {
        this.bpmn2_resourceparameters.add(bpmn2_resourceparameter);
    }

}