





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends ScopedElement, ReactiveElement, SpecificationElement, CompositeElement, RegularState {

    private boolean orthogonal;
    private boolean subchart;
    private boolean composite;
    private String substatechartId;
    private boolean leaf;
    private boolean simple;





    private sgraph_Statechart sgraph_statechart;


    public sgraph_State(
        boolean orthogonal,        boolean subchart,        boolean composite,        String substatechartId,        boolean leaf,        boolean simple    ) {
        super(
        );
        this.orthogonal = orthogonal;
        this.subchart = subchart;
        this.composite = composite;
        this.substatechartId = substatechartId;
        this.leaf = leaf;
        this.simple = simple;
    }


    public boolean getOrthogonal() {
        return orthogonal;
    }

    public void setOrthogonal(boolean orthogonal) {
        this.orthogonal = orthogonal;
    }
    public boolean getSubchart() {
        return subchart;
    }

    public void setSubchart(boolean subchart) {
        this.subchart = subchart;
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
    public boolean getLeaf() {
        return leaf;
    }

    public void setLeaf(boolean leaf) {
        this.leaf = leaf;
    }
    public boolean getSimple() {
        return simple;
    }

    public void setSimple(boolean simple) {
        this.simple = simple;
    }

    public sgraph_Statechart getSgraph_statechart() {
        return sgraph_statechart;
    }

    public void setSgraph_statechart(sgraph_Statechart sgraph_statechart) {
        this.sgraph_statechart = sgraph_statechart;
    }

}