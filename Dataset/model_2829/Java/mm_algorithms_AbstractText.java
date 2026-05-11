





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_AbstractText extends GraphicsAlgorithm {

    private String rotation;
    private String horizontalAlignment;
    private String angle;
    private String verticalAlignment;
    private String value;



    public mm_algorithms_AbstractText(
        String rotation,        String horizontalAlignment,        String angle,        String verticalAlignment,        String value    ) {
        super(
        );
        this.rotation = rotation;
        this.horizontalAlignment = horizontalAlignment;
        this.angle = angle;
        this.verticalAlignment = verticalAlignment;
        this.value = value;
    }


    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}