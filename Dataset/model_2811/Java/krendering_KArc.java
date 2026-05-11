





import java.util.List;
import java.util.ArrayList;

public class krendering_KArc extends KContainerRendering {

    private float startAngle;
    private String arcType;
    private float arcAngle;



    public krendering_KArc(
        float startAngle,        String arcType,        float arcAngle    ) {
        super(
        );
        this.startAngle = startAngle;
        this.arcType = arcType;
        this.arcAngle = arcAngle;
    }


    public float getStartangle() {
        return startAngle;
    }

    public void setStartangle(float startAngle) {
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


}