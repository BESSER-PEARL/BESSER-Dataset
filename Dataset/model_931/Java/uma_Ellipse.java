





import java.util.List;
import java.util.ArrayList;

public class uma_Ellipse extends GraphicPrimitive {

    private String startAngle;
    private String radiusX;
    private String rotation;
    private String endAngle;
    private String radiusY;





    private uma_Point uma_point;


    public uma_Ellipse(
        String startAngle,        String radiusX,        String rotation,        String endAngle,        String radiusY    ) {
        super(
        );
        this.startAngle = startAngle;
        this.radiusX = radiusX;
        this.rotation = rotation;
        this.endAngle = endAngle;
        this.radiusY = radiusY;
    }


    public String getStartangle() {
        return startAngle;
    }

    public void setStartangle(String startAngle) {
        this.startAngle = startAngle;
    }
    public String getRadiusx() {
        return radiusX;
    }

    public void setRadiusx(String radiusX) {
        this.radiusX = radiusX;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getEndangle() {
        return endAngle;
    }

    public void setEndangle(String endAngle) {
        this.endAngle = endAngle;
    }
    public String getRadiusy() {
        return radiusY;
    }

    public void setRadiusy(String radiusY) {
        this.radiusY = radiusY;
    }

    public uma_Point getUma_point() {
        return uma_point;
    }

    public void setUma_point(uma_Point uma_point) {
        this.uma_point = uma_point;
    }

}