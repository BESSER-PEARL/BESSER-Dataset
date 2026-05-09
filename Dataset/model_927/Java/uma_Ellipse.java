





import java.util.List;
import java.util.ArrayList;

public class uma_Ellipse extends GraphicPrimitive {

    private String endAngle;
    private String radiusY;
    private String startAngle;
    private String rotation;
    private String radiusX;





    private uma_Point uma_point;


    public uma_Ellipse(
        String endAngle,        String radiusY,        String startAngle,        String rotation,        String radiusX    ) {
        super(
        );
        this.endAngle = endAngle;
        this.radiusY = radiusY;
        this.startAngle = startAngle;
        this.rotation = rotation;
        this.radiusX = radiusX;
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
    public String getStartangle() {
        return startAngle;
    }

    public void setStartangle(String startAngle) {
        this.startAngle = startAngle;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getRadiusx() {
        return radiusX;
    }

    public void setRadiusx(String radiusX) {
        this.radiusX = radiusX;
    }

    public uma_Point getUma_point() {
        return uma_point;
    }

    public void setUma_point(uma_Point uma_point) {
        this.uma_point = uma_point;
    }

}