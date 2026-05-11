





import java.util.List;
import java.util.ArrayList;

public class krendering_KRoundedRectangle extends KContainerRendering {

    private float cornerWidth;
    private float cornerHeight;



    public krendering_KRoundedRectangle(
        float cornerWidth,        float cornerHeight    ) {
        super(
        );
        this.cornerWidth = cornerWidth;
        this.cornerHeight = cornerHeight;
    }


    public float getCornerwidth() {
        return cornerWidth;
    }

    public void setCornerwidth(float cornerWidth) {
        this.cornerWidth = cornerWidth;
    }
    public float getCornerheight() {
        return cornerHeight;
    }

    public void setCornerheight(float cornerHeight) {
        this.cornerHeight = cornerHeight;
    }


}