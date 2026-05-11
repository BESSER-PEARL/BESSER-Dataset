





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_AbstractText extends GraphicsAlgorithm {

    private String rotation;
    private String value;
    private String horizontalAlignment;
    private String verticalAlignment;
    private String angle;



    public mm_algorithms_AbstractText(
        String rotation,        String value,        String horizontalAlignment,        String verticalAlignment,        String angle    ) {
        super(
        );
        this.rotation = rotation;
        this.value = value;
        this.horizontalAlignment = horizontalAlignment;
        this.verticalAlignment = verticalAlignment;
        this.angle = angle;
    }


    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }


}