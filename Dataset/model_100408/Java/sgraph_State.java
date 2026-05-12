





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends ScopedElement, Vertex, ReactiveElement, ExpressionElement {

    private boolean composite;
    private boolean orthogonal;
    private boolean submachine;
    private boolean simple;
    private boolean leaf;





    private sgraph_Statechart sgraph_statechart;




    private List<sgraph_Region> sgraph_regions;


    public sgraph_State(
        boolean composite,        boolean orthogonal,        boolean submachine,        boolean simple,        boolean leaf    ) {
        super(
        );
        this.composite = composite;
        this.orthogonal = orthogonal;
        this.submachine = submachine;
        this.simple = simple;
        this.leaf = leaf;
        this.sgraph_regions = new ArrayList<>();
    }

    public sgraph_State(
        boolean composite,        boolean orthogonal,        boolean submachine,        boolean simple,        boolean leaf        ArrayList<sgraph_Region> sgraph_regions    ) {
        this.composite = composite;
        this.orthogonal = orthogonal;
        this.submachine = submachine;
        this.simple = simple;
        this.leaf = leaf;
        this.sgraph_regions = sgraph_regions;
    }

    public boolean getComposite() {
        return composite;
    }

    public void setComposite(boolean composite) {
        this.composite = composite;
    }
    public boolean getOrthogonal() {
        return orthogonal;
    }

    public void setOrthogonal(boolean orthogonal) {
        this.orthogonal = orthogonal;
    }
    public boolean getSubmachine() {
        return submachine;
    }

    public void setSubmachine(boolean submachine) {
        this.submachine = submachine;
    }
    public boolean getSimple() {
        return simple;
    }

    public void setSimple(boolean simple) {
        this.simple = simple;
    }
    public boolean getLeaf() {
        return leaf;
    }

    public void setLeaf(boolean leaf) {
        this.leaf = leaf;
    }

    public sgraph_Statechart getSgraph_statechart() {
        return sgraph_statechart;
    }

    public void setSgraph_statechart(sgraph_Statechart sgraph_statechart) {
        this.sgraph_statechart = sgraph_statechart;
    }
    public List<sgraph_Region> getSgraph_regions() {
        return sgraph_regions;
    }

    public void addSgraph_region(Sgraph_region sgraph_region) {
        this.sgraph_regions.add(sgraph_region);
    }

}