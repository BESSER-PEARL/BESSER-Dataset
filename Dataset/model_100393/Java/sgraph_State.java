





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends ExpressionElement, RegularState, ScopedElement, ReactiveElement {

    private boolean simple;
    private boolean leaf;
    private boolean composite;
    private String substatechartId;
    private boolean orthogonal;
    private boolean submachine;





    private List<sgraph_Region> sgraph_regions;




    private sgraph_Statechart sgraph_statechart;


    public sgraph_State(
        boolean simple,        boolean leaf,        boolean composite,        String substatechartId,        boolean orthogonal,        boolean submachine    ) {
        super(
        );
        this.simple = simple;
        this.leaf = leaf;
        this.composite = composite;
        this.substatechartId = substatechartId;
        this.orthogonal = orthogonal;
        this.submachine = submachine;
        this.sgraph_regions = new ArrayList<>();
    }

    public sgraph_State(
        boolean simple,        boolean leaf,        boolean composite,        String substatechartId,        boolean orthogonal,        boolean submachine        ArrayList<sgraph_Region> sgraph_regions    ) {
        this.simple = simple;
        this.leaf = leaf;
        this.composite = composite;
        this.substatechartId = substatechartId;
        this.orthogonal = orthogonal;
        this.submachine = submachine;
        this.sgraph_regions = sgraph_regions;
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
    public boolean getComposite() {
        return composite;
    }

    public void setComposite(boolean composite) {
        this.composite = composite;
    }
    public String getSubstatechartid() {
        return substatechartId;
    }

    public void setSubstatechartid(String substatechartId) {
        this.substatechartId = substatechartId;
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

    public List<sgraph_Region> getSgraph_regions() {
        return sgraph_regions;
    }

    public void addSgraph_region(Sgraph_region sgraph_region) {
        this.sgraph_regions.add(sgraph_region);
    }
    public sgraph_Statechart getSgraph_statechart() {
        return sgraph_statechart;
    }

    public void setSgraph_statechart(sgraph_Statechart sgraph_statechart) {
        this.sgraph_statechart = sgraph_statechart;
    }

}