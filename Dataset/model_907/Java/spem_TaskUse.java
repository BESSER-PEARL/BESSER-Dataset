





import java.util.List;
import java.util.ArrayList;

public class spem_TaskUse extends MethodContentUse, WorkBreakdownElement {

    private String preCondition;
    private String postCondition;





    private spem_TaskDefinition spem_taskdefinition;




    private List<spem_Step> spem_steps;


    public spem_TaskUse(
        String preCondition,        String postCondition    ) {
        super(
        );
        this.preCondition = preCondition;
        this.postCondition = postCondition;
        this.spem_steps = new ArrayList<>();
    }

    public spem_TaskUse(
        String preCondition,        String postCondition        ArrayList<spem_Step> spem_steps    ) {
        this.preCondition = preCondition;
        this.postCondition = postCondition;
        this.spem_steps = spem_steps;
    }

    public String getPrecondition() {
        return preCondition;
    }

    public void setPrecondition(String preCondition) {
        this.preCondition = preCondition;
    }
    public String getPostcondition() {
        return postCondition;
    }

    public void setPostcondition(String postCondition) {
        this.postCondition = postCondition;
    }

    public spem_TaskDefinition getSpem_taskdefinition() {
        return spem_taskdefinition;
    }

    public void setSpem_taskdefinition(spem_TaskDefinition spem_taskdefinition) {
        this.spem_taskdefinition = spem_taskdefinition;
    }
    public List<spem_Step> getSpem_steps() {
        return spem_steps;
    }

    public void addSpem_step(Spem_step spem_step) {
        this.spem_steps.add(spem_step);
    }

}