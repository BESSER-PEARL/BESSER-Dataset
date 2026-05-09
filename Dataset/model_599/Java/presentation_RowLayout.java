





import java.util.List;
import java.util.ArrayList;

public class presentation_RowLayout extends Layout {

    private String marginBottom;
    private String justify;
    private String marginHeight;
    private String wrap;
    private String fill;
    private String marginTop;
    private String pack;
    private String spacing;
    private String marginWidth;
    private String center;
    private String marginRight;
    private String marginLeft;
    private String type;



    public presentation_RowLayout(
        String marginBottom,        String justify,        String marginHeight,        String wrap,        String fill,        String marginTop,        String pack,        String spacing,        String marginWidth,        String center,        String marginRight,        String marginLeft,        String type    ) {
        super(
        );
        this.marginBottom = marginBottom;
        this.justify = justify;
        this.marginHeight = marginHeight;
        this.wrap = wrap;
        this.fill = fill;
        this.marginTop = marginTop;
        this.pack = pack;
        this.spacing = spacing;
        this.marginWidth = marginWidth;
        this.center = center;
        this.marginRight = marginRight;
        this.marginLeft = marginLeft;
        this.type = type;
    }


    public String getMarginbottom() {
        return marginBottom;
    }

    public void setMarginbottom(String marginBottom) {
        this.marginBottom = marginBottom;
    }
    public String getJustify() {
        return justify;
    }

    public void setJustify(String justify) {
        this.justify = justify;
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
    public String getFill() {
        return fill;
    }

    public void setFill(String fill) {
        this.fill = fill;
    }
    public String getMargintop() {
        return marginTop;
    }

    public void setMargintop(String marginTop) {
        this.marginTop = marginTop;
    }
    public String getPack() {
        return pack;
    }

    public void setPack(String pack) {
        this.pack = pack;
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
    public String getCenter() {
        return center;
    }

    public void setCenter(String center) {
        this.center = center;
    }
    public String getMarginright() {
        return marginRight;
    }

    public void setMarginright(String marginRight) {
        this.marginRight = marginRight;
    }
    public String getMarginleft() {
        return marginLeft;
    }

    public void setMarginleft(String marginLeft) {
        this.marginLeft = marginLeft;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}