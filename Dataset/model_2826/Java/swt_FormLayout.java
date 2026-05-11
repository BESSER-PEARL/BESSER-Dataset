





import java.util.List;
import java.util.ArrayList;

public class swt_FormLayout  {

    private int marginTop;
    private int spacing;
    private int marginBottom;
    private int marginWidth;
    private int marginHeight;
    private int marginLeft;
    private int marginRight;



    public swt_FormLayout(
        int marginTop,        int spacing,        int marginBottom,        int marginWidth,        int marginHeight,        int marginLeft,        int marginRight    ) {
        this.marginTop = marginTop;
        this.spacing = spacing;
        this.marginBottom = marginBottom;
        this.marginWidth = marginWidth;
        this.marginHeight = marginHeight;
        this.marginLeft = marginLeft;
        this.marginRight = marginRight;
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
    public int getMarginbottom() {
        return marginBottom;
    }

    public void setMarginbottom(int marginBottom) {
        this.marginBottom = marginBottom;
    }
    public int getMarginwidth() {
        return marginWidth;
    }

    public void setMarginwidth(int marginWidth) {
        this.marginWidth = marginWidth;
    }
    public int getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(int marginHeight) {
        this.marginHeight = marginHeight;
    }
    public int getMarginleft() {
        return marginLeft;
    }

    public void setMarginleft(int marginLeft) {
        this.marginLeft = marginLeft;
    }
    public int getMarginright() {
        return marginRight;
    }

    public void setMarginright(int marginRight) {
        this.marginRight = marginRight;
    }


}