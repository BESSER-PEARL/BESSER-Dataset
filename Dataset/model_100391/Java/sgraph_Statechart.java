





import java.util.List;
import java.util.ArrayList;

public class sgraph_Statechart extends ScopedElement, ExpressionElement, NamedElement, ReactiveElement {






    private sgraph_State sgraph_state;




    private List<sgraph_Region> sgraph_regions;


    public sgraph_Statechart(
    ) {
        super(
        );
        this.sgraph_regions = new ArrayList<>();
    }

    public sgraph_Statechart(
        ArrayList<sgraph_Region> sgraph_regions    ) {
        this.sgraph_regions = sgraph_regions;
    }


    public sgraph_State getSgraph_state() {
        return sgraph_state;
    }

    public void setSgraph_state(sgraph_State sgraph_state) {
        this.sgraph_state = sgraph_state;
    }
    public List<sgraph_Region> getSgraph_regions() {
        return sgraph_regions;
    }

    public void addSgraph_region(Sgraph_region sgraph_region) {
        this.sgraph_regions.add(sgraph_region);
    }

}