





import java.util.List;
import java.util.ArrayList;

public class spem_TaskDefinition extends MethodContentElement, WorkDefinition {






    private List<spem_Qualification> spem_qualifications;




    private List<spem_Step> spem_steps;




    private spem_TaskUse spem_taskuse;


    public spem_TaskDefinition(
    ) {
        super(
        );
        this.spem_qualifications = new ArrayList<>();
        this.spem_steps = new ArrayList<>();
    }

    public spem_TaskDefinition(
        ArrayList<spem_Qualification> spem_qualifications,        ArrayList<spem_Step> spem_steps    ) {
        this.spem_qualifications = spem_qualifications;
        this.spem_steps = spem_steps;
    }


    public List<spem_Qualification> getSpem_qualifications() {
        return spem_qualifications;
    }

    public void addSpem_qualification(Spem_qualification spem_qualification) {
        this.spem_qualifications.add(spem_qualification);
    }
    public List<spem_Step> getSpem_steps() {
        return spem_steps;
    }

    public void addSpem_step(Spem_step spem_step) {
        this.spem_steps.add(spem_step);
    }
    public spem_TaskUse getSpem_taskuse() {
        return spem_taskuse;
    }

    public void setSpem_taskuse(spem_TaskUse spem_taskuse) {
        this.spem_taskuse = spem_taskuse;
    }

}