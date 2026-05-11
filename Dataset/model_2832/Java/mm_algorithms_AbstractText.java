





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_AbstractText extends GraphicsAlgorithm {

    private String verticalAlignment;
    private String value;
    private String angle;
    private String horizontalAlignment;



    public mm_algorithms_AbstractText(
        String verticalAlignment,        String value,        String angle,        String horizontalAlignment    ) {
        super(
        );
        this.verticalAlignment = verticalAlignment;
        this.value = value;
        this.angle = angle;
        this.horizontalAlignment = horizontalAlignment;
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
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }


}