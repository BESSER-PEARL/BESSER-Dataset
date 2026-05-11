





import java.util.List;
import java.util.ArrayList;

public class ntnustudies_Semester  {

    private String type;
    private int year;





    private ntnustudies_Programme ntnustudies_programme;




    private ntnustudies_Programme ntnustudies_programme;




    private ntnustudies_Specialization ntnustudies_specialization;




    private List<ntnustudies_Course> ntnustudies_courses;


    public ntnustudies_Semester(
        String type,        int year    ) {
        this.type = type;
        this.year = year;
        this.ntnustudies_courses = new ArrayList<>();
    }

    public ntnustudies_Semester(
        String type,        int year        ArrayList<ntnustudies_Course> ntnustudies_courses    ) {
        this.type = type;
        this.year = year;
        this.ntnustudies_courses = ntnustudies_courses;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public ntnustudies_Programme getNtnustudies_programme() {
        return ntnustudies_programme;
    }

    public void setNtnustudies_programme(ntnustudies_Programme ntnustudies_programme) {
        this.ntnustudies_programme = ntnustudies_programme;
    }
    public ntnustudies_Programme getNtnustudies_programme() {
        return ntnustudies_programme;
    }

    public void setNtnustudies_programme(ntnustudies_Programme ntnustudies_programme) {
        this.ntnustudies_programme = ntnustudies_programme;
    }
    public ntnustudies_Specialization getNtnustudies_specialization() {
        return ntnustudies_specialization;
    }

    public void setNtnustudies_specialization(ntnustudies_Specialization ntnustudies_specialization) {
        this.ntnustudies_specialization = ntnustudies_specialization;
    }
    public List<ntnustudies_Course> getNtnustudies_courses() {
        return ntnustudies_courses;
    }

    public void addNtnustudies_course(Ntnustudies_course ntnustudies_course) {
        this.ntnustudies_courses.add(ntnustudies_course);
    }

}