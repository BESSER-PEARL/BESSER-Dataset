





import java.util.List;
import java.util.ArrayList;

public class siddhi_APP extends AppAnnotation {

    private String ap;





    private List<siddhi_AnnotationElement> siddhi_annotationelements;




    private siddhi_Name siddhi_name;


    public siddhi_APP(
        String ap    ) {
        super(
        );
        this.ap = ap;
        this.siddhi_annotationelements = new ArrayList<>();
    }

    public siddhi_APP(
        String ap        ArrayList<siddhi_AnnotationElement> siddhi_annotationelements    ) {
        this.ap = ap;
        this.siddhi_annotationelements = siddhi_annotationelements;
    }

    public String getAp() {
        return ap;
    }

    public void setAp(String ap) {
        this.ap = ap;
    }

    public List<siddhi_AnnotationElement> getSiddhi_annotationelements() {
        return siddhi_annotationelements;
    }

    public void addSiddhi_annotationelement(Siddhi_annotationelement siddhi_annotationelement) {
        this.siddhi_annotationelements.add(siddhi_annotationelement);
    }
    public siddhi_Name getSiddhi_name() {
        return siddhi_name;
    }

    public void setSiddhi_name(siddhi_Name siddhi_name) {
        this.siddhi_name = siddhi_name;
    }

}