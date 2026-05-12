





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends RegularState, CompositeElement, ScopedElement, ReactiveElement, SpecificationElement, DocumentedElement {

    private boolean composite;
    private boolean leaf;
    private boolean subchart;
    private boolean simple;
    private boolean orthogonal;
    private String substatechartId;





    private sgraph_Statechart sgraph_statechart;


    public sgraph_State(
        boolean composite,        boolean leaf,        boolean subchart,        boolean simple,        boolean orthogonal,        String substatechartId    ) {
        super(
        );
        this.composite = composite;
        this.leaf = leaf;
        this.subchart = subchart;
        this.simple = simple;
        this.orthogonal = orthogonal;
        this.substatechartId = substatechartId;
    }


    public boolean getComposite() {
        return composite;
    }

    public void setComposite(boolean composite) {
        this.composite = composite;
    }
    public boolean getLeaf() {
        return leaf;
    }

    public void setLeaf(boolean leaf) {
        this.leaf = leaf;
    }
    public boolean getSubchart() {
        return subchart;
    }

    public void setSubchart(boolean subchart) {
        this.subchart = subchart;
    }
    public boolean getSimple() {
        return simple;
    }

    public void setSimple(boolean simple) {
        this.simple = simple;
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

    public sgraph_Statechart getSgraph_statechart() {
        return sgraph_statechart;
    }

    public void setSgraph_statechart(sgraph_Statechart sgraph_statechart) {
        this.sgraph_statechart = sgraph_statechart;
    }

}