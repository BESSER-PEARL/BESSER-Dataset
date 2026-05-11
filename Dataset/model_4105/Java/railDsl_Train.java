





import java.util.List;
import java.util.ArrayList;

public class railDsl_Train extends Declaration {

    private float speed;
    private float acceleration;
    private float length;





    private railDsl_SegmentPosition raildsl_segmentposition;


    public railDsl_Train(
        float speed,        float acceleration,        float length    ) {
        super(
        );
        this.speed = speed;
        this.acceleration = acceleration;
        this.length = length;
    }


    public float getSpeed() {
        return speed;
    }

    public void setSpeed(float speed) {
        this.speed = speed;
    }
    public float getAcceleration() {
        return acceleration;
    }

    public void setAcceleration(float acceleration) {
        this.acceleration = acceleration;
    }
    public float getLength() {
        return length;
    }

    public void setLength(float length) {
        this.length = length;
    }

    public railDsl_SegmentPosition getRaildsl_segmentposition() {
        return raildsl_segmentposition;
    }

    public void setRaildsl_segmentposition(railDsl_SegmentPosition raildsl_segmentposition) {
        this.raildsl_segmentposition = raildsl_segmentposition;
    }

}