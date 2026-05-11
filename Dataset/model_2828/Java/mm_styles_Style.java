





import java.util.List;
import java.util.ArrayList;

public class mm_styles_Style extends StyleContainer, styles_AbstractStyle {

    private String stretchV;
    private String description;
    private String proportional;
    private String angle;
    private String horizontalAlignment;
    private String id;
    private String verticalAlignment;
    private String stretchH;





    private styles_Font styles_font;


    public mm_styles_Style(
        String stretchV,        String description,        String proportional,        String angle,        String horizontalAlignment,        String id,        String verticalAlignment,        String stretchH    ) {
        super(
        );
        this.stretchV = stretchV;
        this.description = description;
        this.proportional = proportional;
        this.angle = angle;
        this.horizontalAlignment = horizontalAlignment;
        this.id = id;
        this.verticalAlignment = verticalAlignment;
        this.stretchH = stretchH;
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
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public String getStretchh() {
        return stretchH;
    }

    public void setStretchh(String stretchH) {
        this.stretchH = stretchH;
    }

    public styles_Font getStyles_font() {
        return styles_font;
    }

    public void setStyles_font(styles_Font styles_font) {
        this.styles_font = styles_font;
    }

}