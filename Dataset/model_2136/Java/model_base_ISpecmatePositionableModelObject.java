





import java.util.List;
import java.util.ArrayList;

public class model_base_ISpecmatePositionableModelObject extends ISpecmateModelObject {

    private float x;
    private float width;
    private float y;
    private float height;



    public model_base_ISpecmatePositionableModelObject(
        float x,        float width,        float y,        float height    ) {
        super(
        );
        this.x = x;
        this.width = width;
        this.y = y;
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
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }


}