





import java.util.List;
import java.util.ArrayList;

public class spem_ProcessComponent extends ProcessPackage {






    private spem_ProcessComponentUse spem_processcomponentuse;




    private spem_Activity spem_activity;


    public spem_ProcessComponent(
    ) {
        super(
        );
    }



    public spem_ProcessComponentUse getSpem_processcomponentuse() {
        return spem_processcomponentuse;
    }

    public void setSpem_processcomponentuse(spem_ProcessComponentUse spem_processcomponentuse) {
        this.spem_processcomponentuse = spem_processcomponentuse;
    }
    public spem_Activity getSpem_activity() {
        return spem_activity;
    }

    public void setSpem_activity(spem_Activity spem_activity) {
        this.spem_activity = spem_activity;
    }

}