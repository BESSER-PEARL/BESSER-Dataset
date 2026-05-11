





import java.util.List;
import java.util.ArrayList;

public class krendering_KShadow extends KStyle {

    private float xOffset;
    private float yOffset;
    private float blur;





    private krendering_KColor krendering_kcolor;


    public krendering_KShadow(
        float xOffset,        float yOffset,        float blur    ) {
        super(
        );
        this.xOffset = xOffset;
        this.yOffset = yOffset;
        this.blur = blur;
    }


    public float getXoffset() {
        return xOffset;
    }

    public void setXoffset(float xOffset) {
        this.xOffset = xOffset;
    }
    public float getYoffset() {
        return yOffset;
    }

    public void setYoffset(float yOffset) {
        this.yOffset = yOffset;
    }
    public float getBlur() {
        return blur;
    }

    public void setBlur(float blur) {
        this.blur = blur;
    }

    public krendering_KColor getKrendering_kcolor() {
        return krendering_kcolor;
    }

    public void setKrendering_kcolor(krendering_KColor krendering_kcolor) {
        this.krendering_kcolor = krendering_kcolor;
    }

}