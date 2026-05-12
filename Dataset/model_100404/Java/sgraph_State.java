





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends RegularState, ScopedElement, ReactiveElement, ExpressionElement {

    private boolean simple;
    private boolean submachine;
    private boolean leaf;
    private boolean orthogonal;
    private String substatechartId;
    private boolean composite;





    private sgraph_Statechart sgraph_statechart;




    private List<sgraph_Region> sgraph_regions;


    public sgraph_State(
        boolean simple,        boolean submachine,        boolean leaf,        boolean orthogonal,        String substatechartId,        boolean composite    ) {
        super(
        );
        this.simple = simple;
        this.submachine = submachine;
        this.leaf = leaf;
        this.orthogonal = orthogonal;
        this.substatechartId = substatechartId;
        this.composite = composite;
        this.sgraph_regions = new ArrayList<>();
    }

    public sgraph_State(
        boolean simple,        boolean submachine,        boolean leaf,        boolean orthogonal,        String substatechartId,        boolean composite        ArrayList<sgraph_Region> sgraph_regions    ) {
        this.simple = simple;
        this.submachine = submachine;
        this.leaf = leaf;
        this.orthogonal = orthogonal;
        this.substatechartId = substatechartId;
        this.composite = composite;
        this.sgraph_regions = sgraph_regions;
    }

    public boolean getSimple() {
        return simple;
    }

    public void setSimple(boolean simple) {
        this.simple = simple;
    }
    public boolean getSubmachine() {
        return submachine;
    }

    public void setSubmachine(boolean submachine) {
        this.submachine = submachine;
    }
    public boolean getLeaf() {
        return leaf;
    }

    public void setLeaf(boolean leaf) {
        this.leaf = leaf;
    }
    public boolean getOrthogonal() {
        return orthogonal;
    }

    public void setOrthogonal(boolean orthogonal) {
        this.orthogonal = orthogonal;
    }
    public String getSubstatechartid() {
        return substatechartId;
    }

    public void setSubstatechartid(String substatechartId) {
        this.substatechartId = substatechartId;
    }
    public boolean getComposite() {
        return composite;
    }

    public void setComposite(boolean composite) {
        this.composite = composite;
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