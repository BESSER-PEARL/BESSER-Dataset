





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends SpecificationElement, DocumentedElement, RegularState, CompositeElement, ReactiveElement, ScopedElement {

    private boolean orthogonal;
    private boolean simple;
    private boolean leaf;
    private boolean composite;



    public sgraph_State(
        boolean orthogonal,        boolean simple,        boolean leaf,        boolean composite    ) {
        super(
        );
        this.orthogonal = orthogonal;
        this.simple = simple;
        this.leaf = leaf;
        this.composite = composite;
    }


    public boolean getOrthogonal() {
        return orthogonal;
    }

    public void setOrthogonal(boolean orthogonal) {
        this.orthogonal = orthogonal;
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


}