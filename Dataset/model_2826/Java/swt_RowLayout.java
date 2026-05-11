





import java.util.List;
import java.util.ArrayList;

public class swt_RowLayout  {

    private String orientationStyle;
    private int marginRight;
    private int marginLeft;
    private int marginBottom;
    private boolean pack;
    private int marginWidth;
    private boolean fill;
    private boolean center;
    private boolean wrap;
    private int marginTop;
    private int spacing;
    private boolean justify;
    private int marginHeight;



    public swt_RowLayout(
        String orientationStyle,        int marginRight,        int marginLeft,        int marginBottom,        boolean pack,        int marginWidth,        boolean fill,        boolean center,        boolean wrap,        int marginTop,        int spacing,        boolean justify,        int marginHeight    ) {
        this.orientationStyle = orientationStyle;
        this.marginRight = marginRight;
        this.marginLeft = marginLeft;
        this.marginBottom = marginBottom;
        this.pack = pack;
        this.marginWidth = marginWidth;
        this.fill = fill;
        this.center = center;
        this.wrap = wrap;
        this.marginTop = marginTop;
        this.spacing = spacing;
        this.justify = justify;
        this.marginHeight = marginHeight;
    }


    public String getOrientationstyle() {
        return orientationStyle;
    }

    public void setOrientationstyle(String orientationStyle) {
        this.orientationStyle = orientationStyle;
    }
    public int getMarginright() {
        return marginRight;
    }

    public void setMarginright(int marginRight) {
        this.marginRight = marginRight;
    }
    public int getMarginleft() {
        return marginLeft;
    }

    public void setMarginleft(int marginLeft) {
        this.marginLeft = marginLeft;
    }
    public int getMarginbottom() {
        return marginBottom;
    }

    public void setMarginbottom(int marginBottom) {
        this.marginBottom = marginBottom;
    }
    public boolean getPack() {
        return pack;
    }

    public void setPack(boolean pack) {
        this.pack = pack;
    }
    public int getMarginwidth() {
        return marginWidth;
    }

    public void setMarginwidth(int marginWidth) {
        this.marginWidth = marginWidth;
    }
    public boolean getFill() {
        return fill;
    }

    public void setFill(boolean fill) {
        this.fill = fill;
    }
    public boolean getCenter() {
        return center;
    }

    public void setCenter(boolean center) {
        this.center = center;
    }
    public boolean getWrap() {
        return wrap;
    }

    public void setWrap(boolean wrap) {
        this.wrap = wrap;
    }
    public int getMargintop() {
        return marginTop;
    }

    public void setMargintop(int marginTop) {
        this.marginTop = marginTop;
    }
    public int getSpacing() {
        return spacing;
    }

    public void setSpacing(int spacing) {
        this.spacing = spacing;
    }
    public boolean getJustify() {
        return justify;
    }

    public void setJustify(boolean justify) {
        this.justify = justify;
    }
    public int getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(int marginHeight) {
        this.marginHeight = marginHeight;
    }


}