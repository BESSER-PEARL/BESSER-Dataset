





import java.util.List;
import java.util.ArrayList;

public class mm_styles_Style extends styles_AbstractStyle, StyleContainer {

    private String proportional;
    private String verticalAlignment;
    private String horizontalAlignment;
    private String id;
    private String stretchH;
    private String angle;
    private String description;
    private String stretchV;



    public mm_styles_Style(
        String proportional,        String verticalAlignment,        String horizontalAlignment,        String id,        String stretchH,        String angle,        String description,        String stretchV    ) {
        super(
        );
        this.proportional = proportional;
        this.verticalAlignment = verticalAlignment;
        this.horizontalAlignment = horizontalAlignment;
        this.id = id;
        this.stretchH = stretchH;
        this.angle = angle;
        this.description = description;
        this.stretchV = stretchV;
    }


    public String getProportional() {
        return proportional;
    }

    public void setProportional(String proportional) {
        this.proportional = proportional;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getStretchh() {
        return stretchH;
    }

    public void setStretchh(String stretchH) {
        this.stretchH = stretchH;
    }
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
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


}