





import java.util.List;
import java.util.ArrayList;

public class diagnosis  {

    private String diagnoses;
    private int id;





    private Examination examination;




    private List<Disease> diseases;


    public diagnosis(
        String diagnoses,        int id    ) {
        this.diagnoses = diagnoses;
        this.id = id;
        this.diseases = new ArrayList<>();
    }

    public diagnosis(
        String diagnoses,        int id        ArrayList<Disease> diseases    ) {
        this.diagnoses = diagnoses;
        this.id = id;
        this.diseases = diseases;
    }

    public String getDiagnoses() {
        return diagnoses;
    }

    public void setDiagnoses(String diagnoses) {
        this.diagnoses = diagnoses;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Examination getExamination() {
        return examination;
    }

    public void setExamination(Examination examination) {
        this.examination = examination;
    }
    public List<Disease> getDiseases() {
        return diseases;
    }

    public void addDisease(Disease disease) {
        this.diseases.add(disease);
    }

}