





import java.util.List;
import java.util.ArrayList;

public class krendering_KLineJoin extends KStyle {

    private String lineJoin;
    private float miterLimit;



    public krendering_KLineJoin(
        String lineJoin,        float miterLimit    ) {
        super(
        );
        this.lineJoin = lineJoin;
        this.miterLimit = miterLimit;
    }


    public String getLinejoin() {
        return lineJoin;
    }

    public void setLinejoin(String lineJoin) {
        this.lineJoin = lineJoin;
    }
    public float getMiterlimit() {
        return miterLimit;
    }

    public void setMiterlimit(float miterLimit) {
        this.miterLimit = miterLimit;
    }


}