





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_SecondaryScheduler extends Scheduler {






    private List<GRM_SchedulableResource> grm_schedulableresources;


    public MARTE_GRM_SecondaryScheduler(
    ) {
        super(
        );
        this.grm_schedulableresources = new ArrayList<>();
    }

    public MARTE_GRM_SecondaryScheduler(
        ArrayList<GRM_SchedulableResource> grm_schedulableresources    ) {
        this.grm_schedulableresources = grm_schedulableresources;
    }


    public List<GRM_SchedulableResource> getGrm_schedulableresources() {
        return grm_schedulableresources;
    }

    public void addGrm_schedulableresource(Grm_schedulableresource grm_schedulableresource) {
        this.grm_schedulableresources.add(grm_schedulableresource);
    }

}