





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends ExpressionElement, Vertex, ScopedElement, ReactiveElement {

    private boolean leaf;
    private boolean composite;
    private boolean orthogonal;
    private boolean submachine;
    private boolean simple;



    public sgraph_State(
        boolean leaf,        boolean composite,        boolean orthogonal,        boolean submachine,        boolean simple    ) {
        super(
        );
        this.leaf = leaf;
        this.composite = composite;
        this.orthogonal = orthogonal;
        this.submachine = submachine;
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
    public boolean getSimple() {
        return simple;
    }

    public void setSimple(boolean simple) {
        this.simple = simple;
    }


}