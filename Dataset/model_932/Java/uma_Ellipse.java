





import java.util.List;
import java.util.ArrayList;

public class uma_Ellipse extends GraphicPrimitive {

    private String startAngle;
    private String radiusY;
    private String rotation;
    private String radiusX;
    private String endAngle;





    private uma_Point uma_point;


    public uma_Ellipse(
        String startAngle,        String radiusY,        String rotation,        String radiusX,        String endAngle    ) {
        super(
        );
        this.startAngle = startAngle;
        this.radiusY = radiusY;
        this.rotation = rotation;
        this.radiusX = radiusX;
        this.endAngle = endAngle;
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
    public String getEndangle() {
        return endAngle;
    }

    public void setEndangle(String endAngle) {
        this.endAngle = endAngle;
    }

    public uma_Point getUma_point() {
        return uma_point;
    }

    public void setUma_point(uma_Point uma_point) {
        this.uma_point = uma_point;
    }

}