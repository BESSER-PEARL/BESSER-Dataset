





import java.util.List;
import java.util.ArrayList;

public class uma_Ellipse extends GraphicPrimitive {

    private String startAngle;
    private String radiusY;
    private String radiusX;
    private String endAngle;
    private String rotation;





    private uma_Point uma_point;


    public uma_Ellipse(
        String startAngle,        String radiusY,        String radiusX,        String endAngle,        String rotation    ) {
        super(
        );
        this.startAngle = startAngle;
        this.radiusY = radiusY;
        this.radiusX = radiusX;
        this.endAngle = endAngle;
        this.rotation = rotation;
    }


    public String getStartangle() {
        return startAngle;
    }

    public void setStartangle(String startAngle) {
        this.startAngle = startAngle;
    }
    public String getRadiusy() {
        return radiusY;
    }

    public void setRadiusy(String radiusY) {
        this.radiusY = radiusY;
    }
    public String getRadiusx() {
        return radiusX;
    }

    public void setRadiusx(String radiusX) {
        this.radiusX = radiusX;
    }
    public String getEndangle() {
        return endAngle;
    }

    public void setEndangle(String endAngle) {
        this.endAngle = endAngle;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }

    public uma_Point getUma_point() {
        return uma_point;
    }

    public void setUma_point(uma_Point uma_point) {
        this.uma_point = uma_point;
    }

}