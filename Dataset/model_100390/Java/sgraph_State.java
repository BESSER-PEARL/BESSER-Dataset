





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends SpecificationElement, ReactiveElement, ScopedElement, CompositeElement, RegularState {

    private boolean subchart;
    private String substatechartId;
    private boolean composite;
    private boolean leaf;
    private boolean simple;
    private boolean orthogonal;





    private sgraph_Statechart sgraph_statechart;


    public sgraph_State(
        boolean subchart,        String substatechartId,        boolean composite,        boolean leaf,        boolean simple,        boolean orthogonal    ) {
        super(
        );
        this.subchart = subchart;
        this.substatechartId = substatechartId;
        this.composite = composite;
        this.leaf = leaf;
        this.simple = simple;
        this.orthogonal = orthogonal;
    }


    public boolean getSubchart() {
        return subchart;
    }

    public void setSubchart(boolean subchart) {
        this.subchart = subchart;
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
    public boolean getOrthogonal() {
        return orthogonal;
    }

    public void setOrthogonal(boolean orthogonal) {
        this.orthogonal = orthogonal;
    }

    public sgraph_Statechart getSgraph_statechart() {
        return sgraph_statechart;
    }

    public void setSgraph_statechart(sgraph_Statechart sgraph_statechart) {
        this.sgraph_statechart = sgraph_statechart;
    }

}