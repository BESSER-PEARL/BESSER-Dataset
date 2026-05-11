





import java.util.List;
import java.util.ArrayList;

public class Concept_Segment extends Trackelement {

    private int Segment_length;



    public Concept_Segment(
        int Segment_length    ) {
        super(
        );
        this.Segment_length = Segment_length;
    }


    public int getSegment_length() {
        return Segment_length;
    }

    public void setSegment_length(int Segment_length) {
        this.Segment_length = Segment_length;
    }


}