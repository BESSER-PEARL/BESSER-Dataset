





import java.util.List;
import java.util.ArrayList;

public class metaModelSM_State  {






    private List<metaModelSM_Region> metamodelsm_regions;


    public metaModelSM_State(
    ) {
        this.metamodelsm_regions = new ArrayList<>();
    }

    public metaModelSM_State(
        ArrayList<metaModelSM_Region> metamodelsm_regions    ) {
        this.metamodelsm_regions = metamodelsm_regions;
    }


    public List<metaModelSM_Region> getMetamodelsm_regions() {
        return metamodelsm_regions;
    }

    public void addMetamodelsm_region(Metamodelsm_region metamodelsm_region) {
        this.metamodelsm_regions.add(metamodelsm_region);
    }

}