





import java.util.List;
import java.util.ArrayList;

public class presentation_FormLayout extends Layout {

    private String spacing;
    private String marginWidth;
    private String marginHeight;
    private String marginLeft;
    private String marginBottom;
    private String marginTop;
    private String marginRight;



    public presentation_FormLayout(
        String spacing,        String marginWidth,        String marginHeight,        String marginLeft,        String marginBottom,        String marginTop,        String marginRight    ) {
        super(
        );
        this.spacing = spacing;
        this.marginWidth = marginWidth;
        this.marginHeight = marginHeight;
        this.marginLeft = marginLeft;
        this.marginBottom = marginBottom;
        this.marginTop = marginTop;
        this.marginRight = marginRight;
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
    public String getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(String marginHeight) {
        this.marginHeight = marginHeight;
    }
    public String getMarginleft() {
        return marginLeft;
    }

    public void setMarginleft(String marginLeft) {
        this.marginLeft = marginLeft;
    }
    public String getMarginbottom() {
        return marginBottom;
    }

    public void setMarginbottom(String marginBottom) {
        this.marginBottom = marginBottom;
    }
    public String getMargintop() {
        return marginTop;
    }

    public void setMargintop(String marginTop) {
        this.marginTop = marginTop;
    }
    public String getMarginright() {
        return marginRight;
    }

    public void setMarginright(String marginRight) {
        this.marginRight = marginRight;
    }


}