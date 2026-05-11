





import java.util.List;
import java.util.ArrayList;

public class StudyProgramme_Specialization  {

    private String name;





    private StudyProgramme_Programme studyprogramme_programme;




    private StudyProgramme_Specialization studyprogramme_specialization;




    private List<StudyProgramme_Semester> studyprogramme_semesters;


    public StudyProgramme_Specialization(
        String name    ) {
        this.name = name;
        this.studyprogramme_semesters = new ArrayList<>();
    }

    public StudyProgramme_Specialization(
        String name        ArrayList<StudyProgramme_Semester> studyprogramme_semesters    ) {
        this.name = name;
        this.studyprogramme_semesters = studyprogramme_semesters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public StudyProgramme_Programme getStudyprogramme_programme() {
        return studyprogramme_programme;
    }

    public void setStudyprogramme_programme(StudyProgramme_Programme studyprogramme_programme) {
        this.studyprogramme_programme = studyprogramme_programme;
    }
    public StudyProgramme_Specialization getStudyprogramme_specialization() {
        return studyprogramme_specialization;
    }

    public void setStudyprogramme_specialization(StudyProgramme_Specialization studyprogramme_specialization) {
        this.studyprogramme_specialization = studyprogramme_specialization;
    }
    public List<StudyProgramme_Semester> getStudyprogramme_semesters() {
        return studyprogramme_semesters;
    }

    public void addStudyprogramme_semester(Studyprogramme_semester studyprogramme_semester) {
        this.studyprogramme_semesters.add(studyprogramme_semester);
    }

}