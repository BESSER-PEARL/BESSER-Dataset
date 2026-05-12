





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends ScopedElement, RegularState, DocumentedElement, ReactiveElement, CompositeElement, SpecificationElement {

    private String substatechartId;
    private boolean subchart;
    private boolean simple;
    private boolean composite;
    private boolean orthogonal;
    private boolean leaf;





    private sgraph_Statechart sgraph_statechart;


    public sgraph_State(
        String substatechartId,        boolean subchart,        boolean simple,        boolean composite,        boolean orthogonal,        boolean leaf    ) {
        super(
        );
        this.substatechartId = substatechartId;
        this.subchart = subchart;
        this.simple = simple;
        this.composite = composite;
        this.orthogonal = orthogonal;
        this.leaf = leaf;
    }


    public String getSubstatechartid() {
        return substatechartId;
    }

    public void setSubstatechartid(String substatechartId) {
        this.substatechartId = substatechartId;
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

}