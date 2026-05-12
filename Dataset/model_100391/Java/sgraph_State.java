





import java.util.List;
import java.util.ArrayList;

public class sgraph_State extends ScopedElement, ExpressionElement, ReactiveElement, Vertex {

    private boolean submachine;
    private boolean leaf;
    private boolean orthogonal;
    private boolean simple;
    private boolean composite;



    public sgraph_State(
        boolean submachine,        boolean leaf,        boolean orthogonal,        boolean simple,        boolean composite    ) {
        super(
        );
        this.submachine = submachine;
        this.leaf = leaf;
        this.orthogonal = orthogonal;
        this.simple = simple;
        this.composite = composite;
    }


    public boolean getSubmachine() {
        return submachine;
    }

    public void setSubmachine(boolean submachine) {
        this.submachine = submachine;
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


}