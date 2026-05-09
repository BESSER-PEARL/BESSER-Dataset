





import java.util.List;
import java.util.ArrayList;

public class presentation_FillLayout extends Layout {

    private String type;
    private String marginHeight;
    private String spacing;
    private String marginWidth;



    public presentation_FillLayout(
        String type,        String marginHeight,        String spacing,        String marginWidth    ) {
        super(
        );
        this.type = type;
        this.marginHeight = marginHeight;
        this.spacing = spacing;
        this.marginWidth = marginWidth;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(String marginHeight) {
        this.marginHeight = marginHeight;
    }
    public String getSpacing() {
        return spacing;
    }

    public void setSpacing(String spacing) {
        this.spacing = spacing;
    }
    public String getMarginwidth() {
        return marginWidth;
    }

    public void setMarginwidth(String marginWidth) {
        this.marginWidth = marginWidth;
    }


}