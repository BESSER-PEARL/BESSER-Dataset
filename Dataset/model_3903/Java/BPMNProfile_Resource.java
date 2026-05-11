





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_Resource extends ItemDefinition {






    private List<BPMNProfile_ResourceParameter> bpmnprofile_resourceparameters;


    public BPMNProfile_Resource(
    ) {
        super(
        );
        this.bpmnprofile_resourceparameters = new ArrayList<>();
    }

    public BPMNProfile_Resource(
        ArrayList<BPMNProfile_ResourceParameter> bpmnprofile_resourceparameters    ) {
        this.bpmnprofile_resourceparameters = bpmnprofile_resourceparameters;
    }


    public List<BPMNProfile_ResourceParameter> getBpmnprofile_resourceparameters() {
        return bpmnprofile_resourceparameters;
    }

    public void addBpmnprofile_resourceparameter(Bpmnprofile_resourceparameter bpmnprofile_resourceparameter) {
        this.bpmnprofile_resourceparameters.add(bpmnprofile_resourceparameter);
    }

}