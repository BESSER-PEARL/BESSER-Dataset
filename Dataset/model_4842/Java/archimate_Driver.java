





import java.util.List;
import java.util.ArrayList;

public class archimate_Driver extends MotivationElement {






    private List<archimate_Assessment> archimate_assessments;




    private archimate_Assessment archimate_assessment;


    public archimate_Driver(
    ) {
        super(
        );
        this.archimate_assessments = new ArrayList<>();
    }

    public archimate_Driver(
        ArrayList<archimate_Assessment> archimate_assessments    ) {
        this.archimate_assessments = archimate_assessments;
    }


    public List<archimate_Assessment> getArchimate_assessments() {
        return archimate_assessments;
    }

    public void addArchimate_assessment(Archimate_assessment archimate_assessment) {
        this.archimate_assessments.add(archimate_assessment);
    }
    public archimate_Assessment getArchimate_assessment() {
        return archimate_assessment;
    }

    public void setArchimate_assessment(archimate_Assessment archimate_assessment) {
        this.archimate_assessment = archimate_assessment;
    }

}