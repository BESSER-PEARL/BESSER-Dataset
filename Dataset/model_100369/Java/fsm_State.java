





import java.util.List;
import java.util.ArrayList;

public class fsm_State extends AbstractState {






    private fsm_Region fsm_region;




    private List<fsm_Region> fsm_regions;


    public fsm_State(
    ) {
        super(
        );
        this.fsm_regions = new ArrayList<>();
    }

    public fsm_State(
        ArrayList<fsm_Region> fsm_regions    ) {
        this.fsm_regions = fsm_regions;
    }


    public fsm_Region getFsm_region() {
        return fsm_region;
    }

    public void setFsm_region(fsm_Region fsm_region) {
        this.fsm_region = fsm_region;
    }
    public List<fsm_Region> getFsm_regions() {
        return fsm_regions;
    }

    public void addFsm_region(Fsm_region fsm_region) {
        this.fsm_regions.add(fsm_region);
    }

}