





import java.util.List;
import java.util.ArrayList;

public class statemachines_almostuml_State extends almostuml_Vertex, almostuml_NamedElement {






    private List<Region> regions;


    public statemachines_almostuml_State(
    ) {
        super(
        );
        this.regions = new ArrayList<>();
    }

    public statemachines_almostuml_State(
        ArrayList<Region> regions    ) {
        this.regions = regions;
    }


    public List<Region> getRegions() {
        return regions;
    }

    public void addRegion(Region region) {
        this.regions.add(region);
    }

}