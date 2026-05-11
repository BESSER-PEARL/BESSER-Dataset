





import java.util.List;
import java.util.ArrayList;

public class railDsl_TrainSegment  {

    private float length;





    private railDsl_SegmentPosition raildsl_segmentposition;




    private railDsl_Train raildsl_train;


    public railDsl_TrainSegment(
        float length    ) {
        this.length = length;
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
    public railDsl_Train getRaildsl_train() {
        return raildsl_train;
    }

    public void setRaildsl_train(railDsl_Train raildsl_train) {
        this.raildsl_train = raildsl_train;
    }

}