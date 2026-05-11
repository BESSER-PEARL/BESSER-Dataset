





import java.util.List;
import java.util.ArrayList;

public class mm_styles_Style extends styles_AbstractStyle, StyleContainer {

    private String id;
    private String angle;
    private String stretchV;
    private String description;
    private String horizontalAlignment;
    private String stretchH;
    private String verticalAlignment;
    private String proportional;



    public mm_styles_Style(
        String id,        String angle,        String stretchV,        String description,        String horizontalAlignment,        String stretchH,        String verticalAlignment,        String proportional    ) {
        super(
        );
        this.id = id;
        this.angle = angle;
        this.stretchV = stretchV;
        this.description = description;
        this.horizontalAlignment = horizontalAlignment;
        this.stretchH = stretchH;
        this.verticalAlignment = verticalAlignment;
        this.proportional = proportional;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public String getStretchv() {
        return stretchV;
    }

    public void setStretchv(String stretchV) {
        this.stretchV = stretchV;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public String getStretchh() {
        return stretchH;
    }

    public void setStretchh(String stretchH) {
        this.stretchH = stretchH;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public String getProportional() {
        return proportional;
    }

    public void setProportional(String proportional) {
        this.proportional = proportional;
    }


}