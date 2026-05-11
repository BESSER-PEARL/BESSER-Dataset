





import java.util.List;
import java.util.ArrayList;

public class mm_styles_AdaptedGradientColoredAreas  {

    private String definedStyleId;
    private String gradientType;



    public mm_styles_AdaptedGradientColoredAreas(
        String definedStyleId,        String gradientType    ) {
        this.definedStyleId = definedStyleId;
        this.gradientType = gradientType;
    }


    public String getDefinedstyleid() {
        return definedStyleId;
    }

    public void setDefinedstyleid(String definedStyleId) {
        this.definedStyleId = definedStyleId;
    }
    public String getGradienttype() {
        return gradientType;
    }

    public void setGradienttype(String gradientType) {
        this.gradientType = gradientType;
    }


}