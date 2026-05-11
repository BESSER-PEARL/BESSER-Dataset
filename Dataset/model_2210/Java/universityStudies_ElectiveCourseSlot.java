





import java.util.List;
import java.util.ArrayList;

public class universityStudies_ElectiveCourseSlot extends CourseSlot {






    private List<universityStudies_Course> universitystudies_courses;


    public universityStudies_ElectiveCourseSlot(
    ) {
        super(
        );
        this.universitystudies_courses = new ArrayList<>();
    }

    public universityStudies_ElectiveCourseSlot(
        ArrayList<universityStudies_Course> universitystudies_courses    ) {
        this.universitystudies_courses = universitystudies_courses;
    }


    public List<universityStudies_Course> getUniversitystudies_courses() {
        return universitystudies_courses;
    }

    public void addUniversitystudies_course(Universitystudies_course universitystudies_course) {
        this.universitystudies_courses.add(universitystudies_course);
    }

}