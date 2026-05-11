





import java.util.List;
import java.util.ArrayList;

public class region_RgRegion extends ModelRoot {

    private String containerClass;





    private List<region_RgState> region_rgstates;




    private region_RgInitialPseudostate region_rginitialpseudostate;


    public region_RgRegion(
        String containerClass    ) {
        super(
        );
        this.containerClass = containerClass;
        this.region_rgstates = new ArrayList<>();
    }

    public region_RgRegion(
        String containerClass        ArrayList<region_RgState> region_rgstates    ) {
        this.containerClass = containerClass;
        this.region_rgstates = region_rgstates;
    }

    public String getContainerclass() {
        return containerClass;
    }

    public void setContainerclass(String containerClass) {
        this.containerClass = containerClass;
    }

    public List<region_RgState> getRegion_rgstates() {
        return region_rgstates;
    }

    public void addRegion_rgstate(Region_rgstate region_rgstate) {
        this.region_rgstates.add(region_rgstate);
    }
    public region_RgInitialPseudostate getRegion_rginitialpseudostate() {
        return region_rginitialpseudostate;
    }

    public void setRegion_rginitialpseudostate(region_RgInitialPseudostate region_rginitialpseudostate) {
        this.region_rginitialpseudostate = region_rginitialpseudostate;
    }

}