





import java.util.List;
import java.util.ArrayList;

public class railDsl_SegmentPosition  {

    private boolean atStart;
    private String orientation;
    private String side;
    private boolean atEnd;
    private float position;





    private railDsl_SegmentObject raildsl_segmentobject;


    public railDsl_SegmentPosition(
        boolean atStart,        String orientation,        String side,        boolean atEnd,        float position    ) {
        this.atStart = atStart;
        this.orientation = orientation;
        this.side = side;
        this.atEnd = atEnd;
        this.position = position;
    }


    public boolean getAtstart() {
        return atStart;
    }

    public void setAtstart(boolean atStart) {
        this.atStart = atStart;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getSide() {
        return side;
    }

    public void setSide(String side) {
        this.side = side;
    }
    public boolean getAtend() {
        return atEnd;
    }

    public void setAtend(boolean atEnd) {
        this.atEnd = atEnd;
    }
    public float getPosition() {
        return position;
    }

    public void setPosition(float position) {
        this.position = position;
    }

    public railDsl_SegmentObject getRaildsl_segmentobject() {
        return raildsl_segmentobject;
    }

    public void setRaildsl_segmentobject(railDsl_SegmentObject raildsl_segmentobject) {
        this.raildsl_segmentobject = raildsl_segmentobject;
    }

}