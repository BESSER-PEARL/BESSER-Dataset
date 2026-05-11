





import java.util.List;
import java.util.ArrayList;

public class nodesAndEdges_ShapedNode extends Node {

    private float size;
    private String shape;



    public nodesAndEdges_ShapedNode(
        float size,        String shape    ) {
        super(
        );
        this.size = size;
        this.shape = shape;
    }


    public float getSize() {
        return size;
    }

    public void setSize(float size) {
        this.size = size;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }


}