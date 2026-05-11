





import java.util.List;
import java.util.ArrayList;

public class dg_Circle extends GraphicalElement {

    private String radius;





    private dg_Point dg_point;


    public dg_Circle(
        String radius    ) {
        super(
        );
        this.radius = radius;
    }


    public String getRadius() {
        return radius;
    }

    public void setRadius(String radius) {
        this.radius = radius;
    }

    public dg_Point getDg_point() {
        return dg_point;
    }

    public void setDg_point(dg_Point dg_point) {
        this.dg_point = dg_point;
    }

}