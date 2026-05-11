





import java.util.List;
import java.util.ArrayList;

public class geoff_style_Stroke extends Identifiable {

    private String miterLimit;
    private String lineCap;
    private String width;
    private float lineDash;
    private String lineJoin;



    public geoff_style_Stroke(
        String miterLimit,        String lineCap,        String width,        float lineDash,        String lineJoin    ) {
        super(
        );
        this.miterLimit = miterLimit;
        this.lineCap = lineCap;
        this.width = width;
        this.lineDash = lineDash;
        this.lineJoin = lineJoin;
    }


    public String getMiterlimit() {
        return miterLimit;
    }

    public void setMiterlimit(String miterLimit) {
        this.miterLimit = miterLimit;
    }
    public String getLinecap() {
        return lineCap;
    }

    public void setLinecap(String lineCap) {
        this.lineCap = lineCap;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public float getLinedash() {
        return lineDash;
    }

    public void setLinedash(float lineDash) {
        this.lineDash = lineDash;
    }
    public String getLinejoin() {
        return lineJoin;
    }

    public void setLinejoin(String lineJoin) {
        this.lineJoin = lineJoin;
    }


}