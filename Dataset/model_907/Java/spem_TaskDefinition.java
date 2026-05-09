





import java.util.List;
import java.util.ArrayList;

public class spem_TaskDefinition extends WorkDefinition, MethodContentElement {






    private List<spem_Step> spem_steps;




    private spem_TaskDefinition spem_taskdefinition;


    public spem_TaskDefinition(
    ) {
        super(
        );
        this.spem_steps = new ArrayList<>();
    }

    public spem_TaskDefinition(
        ArrayList<spem_Step> spem_steps    ) {
        this.spem_steps = spem_steps;
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

}