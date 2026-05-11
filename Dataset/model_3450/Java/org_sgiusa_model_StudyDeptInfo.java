





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_StudyDeptInfo  {

    private String lastUpdate;
    private String id;





    private List<StudyDeptExam> studydeptexams;


    public org_sgiusa_model_StudyDeptInfo(
        String lastUpdate,        String id    ) {
        this.lastUpdate = lastUpdate;
        this.id = id;
        this.studydeptexams = new ArrayList<>();
    }

    public org_sgiusa_model_StudyDeptInfo(
        String lastUpdate,        String id        ArrayList<StudyDeptExam> studydeptexams    ) {
        this.lastUpdate = lastUpdate;
        this.id = id;
        this.studydeptexams = studydeptexams;
    }

    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<StudyDeptExam> getStudydeptexams() {
        return studydeptexams;
    }

    public void addStudydeptexam(Studydeptexam studydeptexam) {
        this.studydeptexams.add(studydeptexam);
    }

}