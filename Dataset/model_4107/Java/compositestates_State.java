





import java.util.List;
import java.util.ArrayList;

public class compositestates_State extends AbstractState {






    private compositestates_Region compositestates_region;




    private List<compositestates_Region> compositestates_regions;


    public compositestates_State(
    ) {
        super(
        );
        this.compositestates_regions = new ArrayList<>();
    }

    public compositestates_State(
        ArrayList<compositestates_Region> compositestates_regions    ) {
        this.compositestates_regions = compositestates_regions;
    }


    public compositestates_Region getCompositestates_region() {
        return compositestates_region;
    }

    public void setCompositestates_region(compositestates_Region compositestates_region) {
        this.compositestates_region = compositestates_region;
    }
    public List<compositestates_Region> getCompositestates_regions() {
        return compositestates_regions;
    }

    public void addCompositestates_region(Compositestates_region compositestates_region) {
        this.compositestates_regions.add(compositestates_region);
    }

}