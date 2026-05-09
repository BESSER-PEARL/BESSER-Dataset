





import java.util.List;
import java.util.ArrayList;

public class capellacommon_State extends AbstractState {






    private List<capellacommon_Region> capellacommon_regions;


    public capellacommon_State(
    ) {
        super(
        );
        this.capellacommon_regions = new ArrayList<>();
    }

    public capellacommon_State(
        ArrayList<capellacommon_Region> capellacommon_regions    ) {
        this.capellacommon_regions = capellacommon_regions;
    }


    public List<capellacommon_Region> getCapellacommon_regions() {
        return capellacommon_regions;
    }

    public void addCapellacommon_region(Capellacommon_region capellacommon_region) {
        this.capellacommon_regions.add(capellacommon_region);
    }

}