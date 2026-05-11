





import java.util.List;
import java.util.ArrayList;

public class studies_StudyYear  {

    private String programName;





    private List<studies_StudyYear> studies_studyyears;




    private studies_Semester studies_semester;




    private studies_Semester studies_semester;




    private studies_StudyInstance studies_studyinstance;


    public studies_StudyYear(
        String programName    ) {
        this.programName = programName;
        this.studies_studyyears = new ArrayList<>();
    }

    public studies_StudyYear(
        String programName        ArrayList<studies_StudyYear> studies_studyyears    ) {
        this.programName = programName;
        this.studies_studyyears = studies_studyyears;
    }

    public String getProgramname() {
        return programName;
    }

    public void setProgramname(String programName) {
        this.programName = programName;
    }

    public List<studies_StudyYear> getStudies_studyyears() {
        return studies_studyyears;
    }

    public void addStudies_studyyear(Studies_studyyear studies_studyyear) {
        this.studies_studyyears.add(studies_studyyear);
    }
    public studies_Semester getStudies_semester() {
        return studies_semester;
    }

    public void setStudies_semester(studies_Semester studies_semester) {
        this.studies_semester = studies_semester;
    }
    public studies_Semester getStudies_semester() {
        return studies_semester;
    }

    public void setStudies_semester(studies_Semester studies_semester) {
        this.studies_semester = studies_semester;
    }
    public studies_StudyInstance getStudies_studyinstance() {
        return studies_studyinstance;
    }

    public void setStudies_studyinstance(studies_StudyInstance studies_studyinstance) {
        this.studies_studyinstance = studies_studyinstance;
    }

}