





import java.util.List;
import java.util.ArrayList;

public class book_Rotation extends Animation {

    private float toAngle;
    private float fromAngle;



    public book_Rotation(
        float toAngle,        float fromAngle    ) {
        super(
        );
        this.toAngle = toAngle;
        this.fromAngle = fromAngle;
    }


    public float getToangle() {
        return toAngle;
    }

    public void setToangle(float toAngle) {
        this.toAngle = toAngle;
    }
    public float getFromangle() {
        return fromAngle;
    }

    public void setFromangle(float fromAngle) {
        this.fromAngle = fromAngle;
    }


}