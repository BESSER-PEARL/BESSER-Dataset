





import java.util.List;
import java.util.ArrayList;

public class book_Rotation extends Animation {

    private float fromAngle;
    private float toAngle;



    public book_Rotation(
        float fromAngle,        float toAngle    ) {
        super(
        );
        this.fromAngle = fromAngle;
        this.toAngle = toAngle;
    }


    public float getFromangle() {
        return fromAngle;
    }

    public void setFromangle(float fromAngle) {
        this.fromAngle = fromAngle;
    }
    public float getToangle() {
        return toAngle;
    }

    public void setToangle(float toAngle) {
        this.toAngle = toAngle;
    }


}