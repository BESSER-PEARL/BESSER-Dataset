





import java.util.List;
import java.util.ArrayList;

public class mm_styles_Style extends StyleContainer, styles_AbstractStyle {

    private String angle;
    private String stretchH;
    private String proportional;
    private String horizontalAlignment;
    private String description;
    private String stretchV;
    private String rotation;
    private String verticalAlignment;
    private String id;



    public mm_styles_Style(
        String angle,        String stretchH,        String proportional,        String horizontalAlignment,        String description,        String stretchV,        String rotation,        String verticalAlignment,        String id    ) {
        super(
        );
        this.angle = angle;
        this.stretchH = stretchH;
        this.proportional = proportional;
        this.horizontalAlignment = horizontalAlignment;
        this.description = description;
        this.stretchV = stretchV;
        this.rotation = rotation;
        this.verticalAlignment = verticalAlignment;
        this.id = id;
    }


    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public String getStretchh() {
        return stretchH;
    }

    public void setStretchh(String stretchH) {
        this.stretchH = stretchH;
    }
    public String getProportional() {
        return proportional;
    }

    public void setProportional(String proportional) {
        this.proportional = proportional;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getStretchv() {
        return stretchV;
    }

    public void setStretchv(String stretchV) {
        this.stretchV = stretchV;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}