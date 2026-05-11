





import java.util.List;
import java.util.ArrayList;

public class programmes_Semester  {

    private int year;
    private String semesterType;





    private programmes_Programme programmes_programme;




    private programmes_Programme programmes_programme;




    private programmes_Specialization programmes_specialization;




    private List<programmes_Course> programmes_courses;


    public programmes_Semester(
        int year,        String semesterType    ) {
        this.year = year;
        this.semesterType = semesterType;
        this.programmes_courses = new ArrayList<>();
    }

    public programmes_Semester(
        int year,        String semesterType        ArrayList<programmes_Course> programmes_courses    ) {
        this.year = year;
        this.semesterType = semesterType;
        this.programmes_courses = programmes_courses;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getSemestertype() {
        return semesterType;
    }

    public void setSemestertype(String semesterType) {
        this.semesterType = semesterType;
    }

    public programmes_Programme getProgrammes_programme() {
        return programmes_programme;
    }

    public void setProgrammes_programme(programmes_Programme programmes_programme) {
        this.programmes_programme = programmes_programme;
    }
    public programmes_Programme getProgrammes_programme() {
        return programmes_programme;
    }

    public void setProgrammes_programme(programmes_Programme programmes_programme) {
        this.programmes_programme = programmes_programme;
    }
    public programmes_Specialization getProgrammes_specialization() {
        return programmes_specialization;
    }

    public void setProgrammes_specialization(programmes_Specialization programmes_specialization) {
        this.programmes_specialization = programmes_specialization;
    }
    public List<programmes_Course> getProgrammes_courses() {
        return programmes_courses;
    }

    public void addProgrammes_course(Programmes_course programmes_course) {
        this.programmes_courses.add(programmes_course);
    }

}