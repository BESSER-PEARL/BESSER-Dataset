





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends SpecificationElement, CompositeElement, ScopedElement, RegularState, ReactiveElement, DocumentedElement {

    private boolean orthogonal;
    private String substatechartId;
    private boolean composite;
    private boolean subchart;
    private boolean simple;
    private boolean leaf;



    public sgraph_State(
        boolean orthogonal,        String substatechartId,        boolean composite,        boolean subchart,        boolean simple,        boolean leaf    ) {
        super(
        );
        this.orthogonal = orthogonal;
        this.substatechartId = substatechartId;
        this.composite = composite;
        this.subchart = subchart;
        this.simple = simple;
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
    public boolean getLeaf() {
        return leaf;
    }

    public void setLeaf(boolean leaf) {
        this.leaf = leaf;
    }


}