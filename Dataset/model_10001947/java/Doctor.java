





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String qualification;





    private Model model;




    private List<Treatment> treatments;


    public Doctor(
        String qualification    ) {
        this.qualification = qualification;
        this.treatments = new ArrayList<>();
    }

    public Doctor(
        String qualification        ArrayList<Treatment> treatments    ) {
        this.qualification = qualification;
        this.treatments = treatments;
    }

    public String getQualification() {
        return qualification;
    }

    public void setQualification(String qualification) {
        this.qualification = qualification;
    }

    public Model getModel() {
        return model;
    }

    public void setModel(Model model) {
        this.model = model;
    }
    public List<Treatment> getTreatments() {
        return treatments;
    }

    public void addTreatment(Treatment treatment) {
        this.treatments.add(treatment);
    }

}