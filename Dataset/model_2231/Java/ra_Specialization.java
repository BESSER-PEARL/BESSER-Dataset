





import java.util.List;
import java.util.ArrayList;

public class ra_Specialization  {

    private String name;





    private List<ra_Semester> ra_semesters;




    private ra_Department ra_department;




    private ra_StudyPlan ra_studyplan;


    public ra_Specialization(
        String name    ) {
        this.name = name;
        this.ra_semesters = new ArrayList<>();
    }

    public ra_Specialization(
        String name        ArrayList<ra_Semester> ra_semesters    ) {
        this.name = name;
        this.ra_semesters = ra_semesters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ra_Semester> getRa_semesters() {
        return ra_semesters;
    }

    public void addRa_semester(Ra_semester ra_semester) {
        this.ra_semesters.add(ra_semester);
    }
    public ra_Department getRa_department() {
        return ra_department;
    }

    public void setRa_department(ra_Department ra_department) {
        this.ra_department = ra_department;
    }
    public ra_StudyPlan getRa_studyplan() {
        return ra_studyplan;
    }

    public void setRa_studyplan(ra_StudyPlan ra_studyplan) {
        this.ra_studyplan = ra_studyplan;
    }

}