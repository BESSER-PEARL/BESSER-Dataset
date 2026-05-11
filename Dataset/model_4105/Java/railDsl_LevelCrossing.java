





import java.util.List;
import java.util.ArrayList;

public class railDsl_LevelCrossing extends SegmentObject {

    private boolean closed;
    private float length;



    public railDsl_LevelCrossing(
        boolean closed,        float length    ) {
        super(
        );
        this.closed = closed;
        this.length = length;
    }


    public boolean getClosed() {
        return closed;
    }

    public void setClosed(boolean closed) {
        this.closed = closed;
    }
    public float getLength() {
        return length;
    }

    public void setLength(float length) {
        this.length = length;
    }


}