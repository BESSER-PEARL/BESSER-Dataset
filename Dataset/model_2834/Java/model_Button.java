





import java.util.List;
import java.util.ArrayList;

public class model_Button extends SkinSupport, TextAlignmentSupport, LinkSupport, Widget, ColorBackgroundSupport, FontSupport, ClickSupport, StateSupport, IconSupport {

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