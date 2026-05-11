





import java.util.List;
import java.util.ArrayList;

public class cs_CSPoint  {

    private float y;
    private float x;





    private cs_CSShape cs_csshape;


    public cs_CSPoint(
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

    public cs_CSShape getCs_csshape() {
        return cs_csshape;
    }

    public void setCs_csshape(cs_CSShape cs_csshape) {
        this.cs_csshape = cs_csshape;
    }

}