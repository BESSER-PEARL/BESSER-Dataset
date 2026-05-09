





import java.util.List;
import java.util.ArrayList;

public class graph_GDimension  {

    private float height;
    private float width;





    private graph_GBoundsAware graph_gboundsaware;


    public graph_GDimension(
        float height,        float width    ) {
        this.height = height;
        this.width = width;
    }


    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }

    public graph_GBoundsAware getGraph_gboundsaware() {
        return graph_gboundsaware;
    }

    public void setGraph_gboundsaware(graph_GBoundsAware graph_gboundsaware) {
        this.graph_gboundsaware = graph_gboundsaware;
    }

}