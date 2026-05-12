





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends CompositeElement, RegularState, SpecificationElement, ScopedElement, ReactiveElement {

    private boolean leaf;
    private boolean orthogonal;
    private boolean composite;
    private boolean simple;
    private String substatechartId;
    private boolean subchart;



    public sgraph_State(
        boolean leaf,        boolean orthogonal,        boolean composite,        boolean simple,        String substatechartId,        boolean subchart    ) {
        super(
        );
        this.leaf = leaf;
        this.orthogonal = orthogonal;
        this.composite = composite;
        this.simple = simple;
        this.substatechartId = substatechartId;
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
    public boolean getComposite() {
        return composite;
    }

    public void setComposite(boolean composite) {
        this.composite = composite;
    }
    public boolean getSimple() {
        return simple;
    }

    public void setSimple(boolean simple) {
        this.simple = simple;
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


}