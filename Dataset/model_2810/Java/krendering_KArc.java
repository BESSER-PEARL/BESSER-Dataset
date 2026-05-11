





import java.util.List;
import java.util.ArrayList;

public class krendering_KArc extends KContainerRendering {

    private String arcType;
    private float arcAngle;
    private float startAngle;



    public krendering_KArc(
        String arcType,        float arcAngle,        float startAngle    ) {
        super(
        );
        this.arcType = arcType;
        this.arcAngle = arcAngle;
        this.startAngle = startAngle;
    }


    public String getArctype() {
        return arcType;
    }

    public void setArctype(String arcType) {
        this.arcType = arcType;
    }
    public float getArcangle() {
        return arcAngle;
    }

    public void setArcangle(float arcAngle) {
        this.arcAngle = arcAngle;
    }
    public float getStartangle() {
        return startAngle;
    }

    public void setStartangle(float startAngle) {
        this.startAngle = startAngle;
    }


}