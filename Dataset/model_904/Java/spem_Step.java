





import java.util.List;
import java.util.ArrayList;

public class spem_Step extends DescribableElement, WorkDefinition, VariabilityElement {

    private String name;





    private spem_TaskDefinition spem_taskdefinition;




    private spem_Step spem_step;




    private spem_Step spem_step;


    public spem_Step(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public spem_TaskDefinition getSpem_taskdefinition() {
        return spem_taskdefinition;
    }

    public void setSpem_taskdefinition(spem_TaskDefinition spem_taskdefinition) {
        this.spem_taskdefinition = spem_taskdefinition;
    }
    public spem_Step getSpem_step() {
        return spem_step;
    }

    public void setSpem_step(spem_Step spem_step) {
        this.spem_step = spem_step;
    }
    public spem_Step getSpem_step() {
        return spem_step;
    }

    public void setSpem_step(spem_Step spem_step) {
        this.spem_step = spem_step;
    }

}