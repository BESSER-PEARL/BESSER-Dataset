





import java.util.List;
import java.util.ArrayList;

public class spem_ProcessPerformer extends WorkDefinitionPerformer, BreakdownElement {






    private spem_TaskUse spem_taskuse;




    private spem_Activity spem_activity;


    public spem_ProcessPerformer(
    ) {
        super(
        );
    }



    public spem_TaskUse getSpem_taskuse() {
        return spem_taskuse;
    }

    public void setSpem_taskuse(spem_TaskUse spem_taskuse) {
        this.spem_taskuse = spem_taskuse;
    }
    public spem_Activity getSpem_activity() {
        return spem_activity;
    }

    public void setSpem_activity(spem_Activity spem_activity) {
        this.spem_activity = spem_activity;
    }

}