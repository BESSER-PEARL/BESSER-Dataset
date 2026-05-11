





import java.util.List;
import java.util.ArrayList;

public class krendering_KColoring extends KStyle {

    private int alpha;
    private float gradientAngle;
    private int targetAlpha;



    public krendering_KColoring(
        int alpha,        float gradientAngle,        int targetAlpha    ) {
        super(
        );
        this.alpha = alpha;
        this.gradientAngle = gradientAngle;
        this.targetAlpha = targetAlpha;
    }


    public int getAlpha() {
        return alpha;
    }

    public void setAlpha(int alpha) {
        this.alpha = alpha;
    }
    public float getGradientangle() {
        return gradientAngle;
    }

    public void setGradientangle(float gradientAngle) {
        this.gradientAngle = gradientAngle;
    }
    public int getTargetalpha() {
        return targetAlpha;
    }

    public void setTargetalpha(int targetAlpha) {
        this.targetAlpha = targetAlpha;
    }


}