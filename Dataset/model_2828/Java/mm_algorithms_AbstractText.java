





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_AbstractText extends GraphicsAlgorithm {

    private String value;
    private String horizontalAlignment;
    private String verticalAlignment;
    private String angle;





    private styles_Font styles_font;


    public mm_algorithms_AbstractText(
        String value,        String horizontalAlignment,        String verticalAlignment,        String angle    ) {
        super(
        );
        this.value = value;
        this.horizontalAlignment = horizontalAlignment;
        this.verticalAlignment = verticalAlignment;
        this.angle = angle;
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

    public styles_Font getStyles_font() {
        return styles_font;
    }

    public void setStyles_font(styles_Font styles_font) {
        this.styles_font = styles_font;
    }

}