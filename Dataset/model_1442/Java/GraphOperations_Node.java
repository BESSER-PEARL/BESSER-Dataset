





import java.util.List;
import java.util.ArrayList;

public class GraphOperations_Node extends Element {

    private int depth;
    private float degree;



    public GraphOperations_Node(
        int depth,        float degree    ) {
        super(
        );
        this.depth = depth;
        this.degree = degree;
    }


    public int getDepth() {
        return depth;
    }

    public void setDepth(int depth) {
        this.depth = depth;
    }
    public float getDegree() {
        return degree;
    }

    public void setDegree(float degree) {
        this.degree = degree;
    }


}