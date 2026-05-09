





import java.util.List;
import java.util.ArrayList;

public class spem_ProcessComponent extends ProcessPackage {






    private spem_Activity spem_activity;




    private List<spem_WorkProductPort> spem_workproductports;




    private spem_ProcessComponentUse spem_processcomponentuse;


    public spem_ProcessComponent(
    ) {
        super(
        );
        this.spem_workproductports = new ArrayList<>();
    }

    public spem_ProcessComponent(
        ArrayList<spem_WorkProductPort> spem_workproductports    ) {
        this.spem_workproductports = spem_workproductports;
    }


    public spem_Activity getSpem_activity() {
        return spem_activity;
    }

    public void setSpem_activity(spem_Activity spem_activity) {
        this.spem_activity = spem_activity;
    }
    public List<spem_WorkProductPort> getSpem_workproductports() {
        return spem_workproductports;
    }

    public void addSpem_workproductport(Spem_workproductport spem_workproductport) {
        this.spem_workproductports.add(spem_workproductport);
    }
    public spem_ProcessComponentUse getSpem_processcomponentuse() {
        return spem_processcomponentuse;
    }

    public void setSpem_processcomponentuse(spem_ProcessComponentUse spem_processcomponentuse) {
        this.spem_processcomponentuse = spem_processcomponentuse;
    }

}