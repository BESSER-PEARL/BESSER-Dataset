





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends Vertex, ReactiveElement, ExpressionElement, ScopedElement {

    private boolean orthogonal;
    private boolean submachine;
    private boolean composite;
    private boolean simple;
    private boolean leaf;



    public sgraph_State(
        boolean orthogonal,        boolean submachine,        boolean composite,        boolean simple,        boolean leaf    ) {
        super(
        );
        this.orthogonal = orthogonal;
        this.submachine = submachine;
        this.composite = composite;
        this.simple = simple;
        this.leaf = leaf;
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
    public boolean getLeaf() {
        return leaf;
    }

    public void setLeaf(boolean leaf) {
        this.leaf = leaf;
    }


}