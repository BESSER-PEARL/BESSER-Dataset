





import java.util.List;
import java.util.ArrayList;

public class graph_ElkShape extends ElkGraphElement {

    private float x;
    private float height;
    private float width;
    private float y;



    public graph_ElkShape(
        float x,        float height,        float width,        float y    ) {
        super(
        );
        this.x = x;
        this.height = height;
        this.width = width;
        this.y = y;
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


}