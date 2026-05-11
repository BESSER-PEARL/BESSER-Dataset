





import java.util.List;
import java.util.ArrayList;

public class ntnustudies_ChosenSemester  {






    private ntnustudies_Semester ntnustudies_semester;




    private List<ntnustudies_Course> ntnustudies_courses;


    public ntnustudies_ChosenSemester(
    ) {
        this.ntnustudies_courses = new ArrayList<>();
    }

    public ntnustudies_ChosenSemester(
        ArrayList<ntnustudies_Course> ntnustudies_courses    ) {
        this.ntnustudies_courses = ntnustudies_courses;
    }


    public ntnustudies_Semester getNtnustudies_semester() {
        return ntnustudies_semester;
    }

    public void setNtnustudies_semester(ntnustudies_Semester ntnustudies_semester) {
        this.ntnustudies_semester = ntnustudies_semester;
    }
    public List<ntnustudies_Course> getNtnustudies_courses() {
        return ntnustudies_courses;
    }

    public void addNtnustudies_course(Ntnustudies_course ntnustudies_course) {
        this.ntnustudies_courses.add(ntnustudies_course);
    }

}