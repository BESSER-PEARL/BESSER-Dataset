





import java.util.List;
import java.util.ArrayList;

public class spem_TaskUse extends WorkBreakdownElement, MethodContentUse {

    private String postCondition;
    private String preCondition;





    private List<spem_Step> spem_steps;




    private spem_TaskDefinition spem_taskdefinition;




    private spem_ProcessPerformer spem_processperformer;




    private List<spem_ProcessParameter> spem_processparameters;


    public spem_TaskUse(
        String postCondition,        String preCondition    ) {
        super(
        );
        this.postCondition = postCondition;
        this.preCondition = preCondition;
        this.spem_steps = new ArrayList<>();
        this.spem_processparameters = new ArrayList<>();
    }

    public spem_TaskUse(
        String postCondition,        String preCondition        ArrayList<spem_Step> spem_steps,        ArrayList<spem_ProcessParameter> spem_processparameters    ) {
        this.postCondition = postCondition;
        this.preCondition = preCondition;
        this.spem_steps = spem_steps;
        this.spem_processparameters = spem_processparameters;
    }

    public String getPostcondition() {
        return postCondition;
    }

    public void setPostcondition(String postCondition) {
        this.postCondition = postCondition;
    }
    public String getPrecondition() {
        return preCondition;
    }

    public void setPrecondition(String preCondition) {
        this.preCondition = preCondition;
    }

    public List<spem_Step> getSpem_steps() {
        return spem_steps;
    }

    public void addSpem_step(Spem_step spem_step) {
        this.spem_steps.add(spem_step);
    }
    public spem_TaskDefinition getSpem_taskdefinition() {
        return spem_taskdefinition;
    }

    public void setSpem_taskdefinition(spem_TaskDefinition spem_taskdefinition) {
        this.spem_taskdefinition = spem_taskdefinition;
    }
    public spem_ProcessPerformer getSpem_processperformer() {
        return spem_processperformer;
    }

    public void setSpem_processperformer(spem_ProcessPerformer spem_processperformer) {
        this.spem_processperformer = spem_processperformer;
    }
    public List<spem_ProcessParameter> getSpem_processparameters() {
        return spem_processparameters;
    }

    public void addSpem_processparameter(Spem_processparameter spem_processparameter) {
        this.spem_processparameters.add(spem_processparameter);
    }

}