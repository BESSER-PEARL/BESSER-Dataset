





import java.util.List;
import java.util.ArrayList;

public class ConceptASE_Segment extends Trackelement {

    private int Segment_height;
    private int Segment_length;



    public ConceptASE_Segment(
        int Segment_height,        int Segment_length    ) {
        super(
        );
        this.Segment_height = Segment_height;
        this.Segment_length = Segment_length;
    }


    public int getSegment_height() {
        return Segment_height;
    }

    public void setSegment_height(int Segment_height) {
        this.Segment_height = Segment_height;
    }
    public int getSegment_length() {
        return Segment_length;
    }

    public void setSegment_length(int Segment_length) {
        this.Segment_length = Segment_length;
    }


}