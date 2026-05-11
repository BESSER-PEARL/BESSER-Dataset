





import java.util.List;
import java.util.ArrayList;

public class mm_styles_Style extends styles_AbstractStyle, StyleContainer {

    private String stretchH;
    private String id;
    private String stretchV;
    private String description;
    private String verticalAlignment;
    private String horizontalAlignment;
    private String proportional;
    private String angle;



    public mm_styles_Style(
        String stretchH,        String id,        String stretchV,        String description,        String verticalAlignment,        String horizontalAlignment,        String proportional,        String angle    ) {
        super(
        );
        this.stretchH = stretchH;
        this.id = id;
        this.stretchV = stretchV;
        this.description = description;
        this.verticalAlignment = verticalAlignment;
        this.horizontalAlignment = horizontalAlignment;
        this.proportional = proportional;
        this.angle = angle;
    }


    public String getStretchh() {
        return stretchH;
    }

    public void setStretchh(String stretchH) {
        this.stretchH = stretchH;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public String getProportional() {
        return proportional;
    }

    public void setProportional(String proportional) {
        this.proportional = proportional;
    }
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }


}