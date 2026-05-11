





import java.util.List;
import java.util.ArrayList;

public class swt_FillLayout  {

    private int marginHeight;
    private int marginWidth;
    private String orientationStyle;
    private int spacing;



    public swt_FillLayout(
        int marginHeight,        int marginWidth,        String orientationStyle,        int spacing    ) {
        this.marginHeight = marginHeight;
        this.marginWidth = marginWidth;
        this.orientationStyle = orientationStyle;
        this.spacing = spacing;
    }


    public int getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(int marginHeight) {
        this.marginHeight = marginHeight;
    }
    public int getMarginwidth() {
        return marginWidth;
    }

    public void setMarginwidth(int marginWidth) {
        this.marginWidth = marginWidth;
    }
    public String getOrientationstyle() {
        return orientationStyle;
    }

    public void setOrientationstyle(String orientationStyle) {
        this.orientationStyle = orientationStyle;
    }
    public int getSpacing() {
        return spacing;
    }

    public void setSpacing(int spacing) {
        this.spacing = spacing;
    }


}