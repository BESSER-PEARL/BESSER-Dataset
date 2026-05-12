





import java.util.List;
import java.util.ArrayList;

public class sgraph_CompositeElement  {






    private List<sgraph_Region> sgraph_regions;




    private sgraph_Region sgraph_region;


    public sgraph_CompositeElement(
    ) {
        this.sgraph_regions = new ArrayList<>();
    }

    public sgraph_CompositeElement(
        ArrayList<sgraph_Region> sgraph_regions    ) {
        this.sgraph_regions = sgraph_regions;
    }


    public List<sgraph_Region> getSgraph_regions() {
        return sgraph_regions;
    }

    public void addSgraph_region(Sgraph_region sgraph_region) {
        this.sgraph_regions.add(sgraph_region);
    }
    public sgraph_Region getSgraph_region() {
        return sgraph_region;
    }

    public void setSgraph_region(sgraph_Region sgraph_region) {
        this.sgraph_region = sgraph_region;
    }

}