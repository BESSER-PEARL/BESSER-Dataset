





import java.util.List;
import java.util.ArrayList;

public class krendering_KLineJoin extends KStyle {

    private float miterLimit;
    private String lineJoin;



    public krendering_KLineJoin(
        float miterLimit,        String lineJoin    ) {
        super(
        );
        this.miterLimit = miterLimit;
        this.lineJoin = lineJoin;
    }


    public float getMiterlimit() {
        return miterLimit;
    }

    public void setMiterlimit(float miterLimit) {
        this.miterLimit = miterLimit;
    }
    public String getLinejoin() {
        return lineJoin;
    }

    public void setLinejoin(String lineJoin) {
        this.lineJoin = lineJoin;
    }


}