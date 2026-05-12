





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends ReactiveElement, RegularState, SpecificationElement, CompositeElement, DocumentedElement, ScopedElement {

    private boolean composite;
    private boolean subchart;
    private boolean leaf;
    private boolean orthogonal;
    private String substatechartId;
    private boolean simple;





    private sgraph_Statechart sgraph_statechart;


    public sgraph_State(
        boolean composite,        boolean subchart,        boolean leaf,        boolean orthogonal,        String substatechartId,        boolean simple    ) {
        super(
        );
        this.composite = composite;
        this.subchart = subchart;
        this.leaf = leaf;
        this.orthogonal = orthogonal;
        this.substatechartId = substatechartId;
        this.simple = simple;
    }


    public boolean getComposite() {
        return composite;
    }

    public void setComposite(boolean composite) {
        this.composite = composite;
    }
    public boolean getSubchart() {
        return subchart;
    }

    public void setSubchart(boolean subchart) {
        this.subchart = subchart;
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