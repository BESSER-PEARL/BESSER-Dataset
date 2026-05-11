





import java.util.List;
import java.util.ArrayList;

public class dmm_UniversityManagementSystem  {






    private List<dmm_Course> dmm_courses;


    public dmm_UniversityManagementSystem(
    ) {
        this.dmm_courses = new ArrayList<>();
    }

    public dmm_UniversityManagementSystem(
        ArrayList<dmm_Course> dmm_courses    ) {
        this.dmm_courses = dmm_courses;
    }


    public List<dmm_Course> getDmm_courses() {
        return dmm_courses;
    }

    public void addDmm_course(Dmm_course dmm_course) {
        this.dmm_courses.add(dmm_course);
    }

}