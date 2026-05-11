





import java.util.List;
import java.util.ArrayList;

public class railDsl_Segment extends TrackObject {






    private railDsl_Vertex raildsl_vertex;




    private List<railDsl_SegmentObject> raildsl_segmentobjects;




    private railDsl_Vertex raildsl_vertex;




    private railDsl_SegmentPosition raildsl_segmentposition;


    public railDsl_Segment(
    ) {
        super(
        );
        this.raildsl_segmentobjects = new ArrayList<>();
    }

    public railDsl_Segment(
        ArrayList<railDsl_SegmentObject> raildsl_segmentobjects    ) {
        this.raildsl_segmentobjects = raildsl_segmentobjects;
    }


    public railDsl_Vertex getRaildsl_vertex() {
        return raildsl_vertex;
    }

    public void setRaildsl_vertex(railDsl_Vertex raildsl_vertex) {
        this.raildsl_vertex = raildsl_vertex;
    }
    public List<railDsl_SegmentObject> getRaildsl_segmentobjects() {
        return raildsl_segmentobjects;
    }

    public void addRaildsl_segmentobject(Raildsl_segmentobject raildsl_segmentobject) {
        this.raildsl_segmentobjects.add(raildsl_segmentobject);
    }
    public railDsl_Vertex getRaildsl_vertex() {
        return raildsl_vertex;
    }

    public void setRaildsl_vertex(railDsl_Vertex raildsl_vertex) {
        this.raildsl_vertex = raildsl_vertex;
    }
    public railDsl_SegmentPosition getRaildsl_segmentposition() {
        return raildsl_segmentposition;
    }

    public void setRaildsl_segmentposition(railDsl_SegmentPosition raildsl_segmentposition) {
        this.raildsl_segmentposition = raildsl_segmentposition;
    }

}