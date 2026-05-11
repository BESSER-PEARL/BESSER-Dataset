





import java.util.List;
import java.util.ArrayList;

public class krendering_KShadow extends KStyle {

    private float yOffset;
    private float xOffset;
    private float blur;



    public krendering_KShadow(
        float yOffset,        float xOffset,        float blur    ) {
        super(
        );
        this.yOffset = yOffset;
        this.xOffset = xOffset;
        this.blur = blur;
    }


    public float getYoffset() {
        return yOffset;
    }

    public void setYoffset(float yOffset) {
        this.yOffset = yOffset;
    }
    public float getXoffset() {
        return xOffset;
    }

    public void setXoffset(float xOffset) {
        this.xOffset = xOffset;
    }
    public float getBlur() {
        return blur;
    }

    public void setBlur(float blur) {
        this.blur = blur;
    }


}