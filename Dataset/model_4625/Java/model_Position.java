





import java.util.List;
import java.util.ArrayList;

public class model_Position  {

    private float x;
    private float y;





    private model_XYChild model_xychild;


    public model_Position(
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

    public model_XYChild getModel_xychild() {
        return model_xychild;
    }

    public void setModel_xychild(model_XYChild model_xychild) {
        this.model_xychild = model_xychild;
    }

}