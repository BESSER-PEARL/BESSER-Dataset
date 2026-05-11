





import java.util.List;
import java.util.ArrayList;

public class railDsl_TrackObject extends Declaration, RouteObject {

    private float length;



    public railDsl_TrackObject(
        float length    ) {
        super(
        );
        this.length = length;
    }


    public float getLength() {
        return length;
    }

    public void setLength(float length) {
        this.length = length;
    }


}