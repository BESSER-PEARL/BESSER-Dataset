





import java.util.List;
import java.util.ArrayList;

public class swt_LineAttributes  {

    private float dash;
    private String cap;
    private String style;
    private float miterLimit;
    private float dashOffset;
    private String join;
    private float width;



    public swt_LineAttributes(
        float dash,        String cap,        String style,        float miterLimit,        float dashOffset,        String join,        float width    ) {
        this.dash = dash;
        this.cap = cap;
        this.style = style;
        this.miterLimit = miterLimit;
        this.dashOffset = dashOffset;
        this.join = join;
        this.width = width;
    }


    public float getDash() {
        return dash;
    }

    public void setDash(float dash) {
        this.dash = dash;
    }
    public String getCap() {
        return cap;
    }

    public void setCap(String cap) {
        this.cap = cap;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public float getMiterlimit() {
        return miterLimit;
    }

    public void setMiterlimit(float miterLimit) {
        this.miterLimit = miterLimit;
    }
    public float getDashoffset() {
        return dashOffset;
    }

    public void setDashoffset(float dashOffset) {
        this.dashOffset = dashOffset;
    }
    public String getJoin() {
        return join;
    }

    public void setJoin(String join) {
        this.join = join;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }


}