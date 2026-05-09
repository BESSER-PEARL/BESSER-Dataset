





import java.util.List;
import java.util.ArrayList;

public class graph_GBounds  {

    private float height;
    private float x;
    private float width;
    private float y;





    private graph_GModelRoot graph_gmodelroot;


    public graph_GBounds(
        float height,        float x,        float width,        float y    ) {
        this.height = height;
        this.x = x;
        this.width = width;
        this.y = y;
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
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public graph_GModelRoot getGraph_gmodelroot() {
        return graph_gmodelroot;
    }

    public void setGraph_gmodelroot(graph_GModelRoot graph_gmodelroot) {
        this.graph_gmodelroot = graph_gmodelroot;
    }

}