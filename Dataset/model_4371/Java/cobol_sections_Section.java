





import java.util.List;
import java.util.ArrayList;

public class cobol_sections_Section extends commons_NamedElement, labels_Procedure {

    private String segmentNumber;



    public cobol_sections_Section(
        String segmentNumber    ) {
        super(
        );
        this.segmentNumber = segmentNumber;
    }


    public String getSegmentnumber() {
        return segmentNumber;
    }

    public void setSegmentnumber(String segmentNumber) {
        this.segmentNumber = segmentNumber;
    }


}