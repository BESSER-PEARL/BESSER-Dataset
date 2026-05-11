





import java.util.List;
import java.util.ArrayList;

public class ra_StudyPlan  {






    private List<ra_Semester> ra_semesters;




    private ra_Programme ra_programme;




    private ra_Programme ra_programme;




    private ra_Department ra_department;


    public ra_StudyPlan(
    ) {
        this.ra_semesters = new ArrayList<>();
    }

    public ra_StudyPlan(
        ArrayList<ra_Semester> ra_semesters    ) {
        this.ra_semesters = ra_semesters;
    }


    public List<ra_Semester> getRa_semesters() {
        return ra_semesters;
    }

    public void addRa_semester(Ra_semester ra_semester) {
        this.ra_semesters.add(ra_semester);
    }
    public ra_Programme getRa_programme() {
        return ra_programme;
    }

    public void setRa_programme(ra_Programme ra_programme) {
        this.ra_programme = ra_programme;
    }
    public ra_Programme getRa_programme() {
        return ra_programme;
    }

    public void setRa_programme(ra_Programme ra_programme) {
        this.ra_programme = ra_programme;
    }
    public ra_Department getRa_department() {
        return ra_department;
    }

    public void setRa_department(ra_Department ra_department) {
        this.ra_department = ra_department;
    }

}