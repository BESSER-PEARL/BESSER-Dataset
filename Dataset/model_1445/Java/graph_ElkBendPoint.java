





import java.util.List;
import java.util.ArrayList;

public class graph_ElkBendPoint  {

    private float y;
    private float x;





    private graph_ElkEdgeSection graph_elkedgesection;


    public graph_ElkBendPoint(
        float y,        float x    ) {
        this.y = y;
        this.x = x;
    }


    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }

    public graph_ElkEdgeSection getGraph_elkedgesection() {
        return graph_elkedgesection;
    }

    public void setGraph_elkedgesection(graph_ElkEdgeSection graph_elkedgesection) {
        this.graph_elkedgesection = graph_elkedgesection;
    }

}