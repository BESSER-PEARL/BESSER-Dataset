





import java.util.List;
import java.util.ArrayList;

public class graph_GPoint  {

    private float x;
    private float y;





    private graph_GEdge graph_gedge;


    public graph_GPoint(
        float x,        float y    ) {
        this.x = x;
        this.y = y;
    }


    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public graph_GEdge getGraph_gedge() {
        return graph_gedge;
    }

    public void setGraph_gedge(graph_GEdge graph_gedge) {
        this.graph_gedge = graph_gedge;
    }

}