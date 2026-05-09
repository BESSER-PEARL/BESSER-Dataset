





import java.util.List;
import java.util.ArrayList;

public class presentation_RowLayout extends Layout {

    private String justify;
    private String marginWidth;
    private String type;
    private String center;
    private String marginBottom;
    private String marginLeft;
    private String pack;
    private String marginHeight;
    private String wrap;
    private String spacing;
    private String marginTop;
    private String marginRight;
    private String fill;



    public presentation_RowLayout(
        String justify,        String marginWidth,        String type,        String center,        String marginBottom,        String marginLeft,        String pack,        String marginHeight,        String wrap,        String spacing,        String marginTop,        String marginRight,        String fill    ) {
        super(
        );
        this.justify = justify;
        this.marginWidth = marginWidth;
        this.type = type;
        this.center = center;
        this.marginBottom = marginBottom;
        this.marginLeft = marginLeft;
        this.pack = pack;
        this.marginHeight = marginHeight;
        this.wrap = wrap;
        this.spacing = spacing;
        this.marginTop = marginTop;
        this.marginRight = marginRight;
        this.fill = fill;
    }


    public String getJustify() {
        return justify;
    }

    public void setJustify(String justify) {
        this.justify = justify;
    }
    public String getMarginwidth() {
        return marginWidth;
    }

    public void setMarginwidth(String marginWidth) {
        this.marginWidth = marginWidth;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getCenter() {
        return center;
    }

    public void setCenter(String center) {
        this.center = center;
    }
    public String getMarginbottom() {
        return marginBottom;
    }

    public void setMarginbottom(String marginBottom) {
        this.marginBottom = marginBottom;
    }
    public String getMarginleft() {
        return marginLeft;
    }

    public void setMarginleft(String marginLeft) {
        this.marginLeft = marginLeft;
    }
    public String getPack() {
        return pack;
    }

    public void setPack(String pack) {
        this.pack = pack;
    }
    public String getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(String marginHeight) {
        this.marginHeight = marginHeight;
    }
    public String getWrap() {
        return wrap;
    }

    public void setWrap(String wrap) {
        this.wrap = wrap;
    }
    public String getSpacing() {
        return spacing;
    }

    public void setSpacing(String spacing) {
        this.spacing = spacing;
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
    public String getFill() {
        return fill;
    }

    public void setFill(String fill) {
        this.fill = fill;
    }


}