





import java.util.List;
import java.util.ArrayList;

public class graph_GBounds  {

    private float y;
    private float width;
    private float height;
    private float x;





    private graph_GModelRoot graph_gmodelroot;


    public graph_GBounds(
        float y,        float width,        float height,        float x    ) {
        this.y = y;
        this.width = width;
        this.height = height;
        this.x = x;
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
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }

    public graph_GModelRoot getGraph_gmodelroot() {
        return graph_gmodelroot;
    }

    public void setGraph_gmodelroot(graph_GModelRoot graph_gmodelroot) {
        this.graph_gmodelroot = graph_gmodelroot;
    }

}