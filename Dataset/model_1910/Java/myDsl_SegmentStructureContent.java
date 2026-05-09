





import java.util.List;
import java.util.ArrayList;

public class myDsl_SegmentStructureContent  {

    private String name;





    private myDsl_SegmentStructure mydsl_segmentstructure;


    public myDsl_SegmentStructureContent(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_SegmentStructure getMydsl_segmentstructure() {
        return mydsl_segmentstructure;
    }

    public void setMydsl_segmentstructure(myDsl_SegmentStructure mydsl_segmentstructure) {
        this.mydsl_segmentstructure = mydsl_segmentstructure;
    }

}