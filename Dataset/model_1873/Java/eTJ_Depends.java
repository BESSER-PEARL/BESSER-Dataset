





import java.util.List;
import java.util.ArrayList;

public class eTJ_Depends  {






    private List<eTJ_TaskDependency> etj_taskdependencys;


    public eTJ_Depends(
    ) {
        this.etj_taskdependencys = new ArrayList<>();
    }

    public eTJ_Depends(
        ArrayList<eTJ_TaskDependency> etj_taskdependencys    ) {
        this.etj_taskdependencys = etj_taskdependencys;
    }


    public List<eTJ_TaskDependency> getEtj_taskdependencys() {
        return etj_taskdependencys;
    }

    public void addEtj_taskdependency(Etj_taskdependency etj_taskdependency) {
        this.etj_taskdependencys.add(etj_taskdependency);
    }

}