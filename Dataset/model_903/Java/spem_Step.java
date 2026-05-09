





import java.util.List;
import java.util.ArrayList;

public class spem_Step extends DescribableElement, WorkDefinition, VariabilityElement {

    private String name;





    private spem_TaskUse spem_taskuse;




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

    public spem_TaskUse getSpem_taskuse() {
        return spem_taskuse;
    }

    public void setSpem_taskuse(spem_TaskUse spem_taskuse) {
        this.spem_taskuse = spem_taskuse;
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