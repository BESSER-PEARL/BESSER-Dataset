





import java.util.List;
import java.util.ArrayList;

public class mm_styles_AdaptedGradientColoredAreas  {

    private String gradientType;
    private String definedStyleId;



    public mm_styles_AdaptedGradientColoredAreas(
        String gradientType,        String definedStyleId    ) {
        this.gradientType = gradientType;
        this.definedStyleId = definedStyleId;
    }


    public String getGradienttype() {
        return gradientType;
    }

    public void setGradienttype(String gradientType) {
        this.gradientType = gradientType;
    }
    public String getDefinedstyleid() {
        return definedStyleId;
    }

    public void setDefinedstyleid(String definedStyleId) {
        this.definedStyleId = definedStyleId;
    }


}