





import java.util.List;
import java.util.ArrayList;

public class model_Button extends FontSupport, StateSupport, TextAlignmentSupport, Widget, IconSupport, LinkSupport, SkinSupport, ColorBackgroundSupport {

    private String style;



    public model_Button(
        String style    ) {
        super(
        );
        this.style = style;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }


}