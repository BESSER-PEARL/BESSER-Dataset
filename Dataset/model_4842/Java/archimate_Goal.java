





import java.util.List;
import java.util.ArrayList;

public class archimate_Goal extends MotivationElement {






    private List<archimate_Assessment> archimate_assessments;




    private archimate_Driver archimate_driver;




    private archimate_Assessment archimate_assessment;




    private List<archimate_Driver> archimate_drivers;




    private archimate_Requirement archimate_requirement;




    private archimate_Outcome archimate_outcome;


    public archimate_Goal(
    ) {
        super(
        );
        this.archimate_assessments = new ArrayList<>();
        this.archimate_drivers = new ArrayList<>();
    }

    public archimate_Goal(
        ArrayList<archimate_Assessment> archimate_assessments,        ArrayList<archimate_Driver> archimate_drivers    ) {
        this.archimate_assessments = archimate_assessments;
        this.archimate_drivers = archimate_drivers;
    }


    public List<archimate_Assessment> getArchimate_assessments() {
        return archimate_assessments;
    }

    public void addArchimate_assessment(Archimate_assessment archimate_assessment) {
        this.archimate_assessments.add(archimate_assessment);
    }
    public archimate_Driver getArchimate_driver() {
        return archimate_driver;
    }

    public void setArchimate_driver(archimate_Driver archimate_driver) {
        this.archimate_driver = archimate_driver;
    }
    public archimate_Assessment getArchimate_assessment() {
        return archimate_assessment;
    }

    public void setArchimate_assessment(archimate_Assessment archimate_assessment) {
        this.archimate_assessment = archimate_assessment;
    }
    public List<archimate_Driver> getArchimate_drivers() {
        return archimate_drivers;
    }

    public void addArchimate_driver(Archimate_driver archimate_driver) {
        this.archimate_drivers.add(archimate_driver);
    }
    public archimate_Requirement getArchimate_requirement() {
        return archimate_requirement;
    }

    public void setArchimate_requirement(archimate_Requirement archimate_requirement) {
        this.archimate_requirement = archimate_requirement;
    }
    public archimate_Outcome getArchimate_outcome() {
        return archimate_outcome;
    }

    public void setArchimate_outcome(archimate_Outcome archimate_outcome) {
        this.archimate_outcome = archimate_outcome;
    }

}