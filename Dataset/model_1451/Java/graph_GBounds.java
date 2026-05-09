





import java.util.List;
import java.util.ArrayList;

public class graph_GBounds  {

    private float x;
    private float height;
    private float y;
    private float width;





    private graph_GModelRoot graph_gmodelroot;


    public graph_GBounds(
        float x,        float height,        float y,        float width    ) {
        this.x = x;
        this.height = height;
        this.y = y;
        this.width = width;
    }


    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }

    public graph_GModelRoot getGraph_gmodelroot() {
        return graph_gmodelroot;
    }

    public void setGraph_gmodelroot(graph_GModelRoot graph_gmodelroot) {
        this.graph_gmodelroot = graph_gmodelroot;
    }

}