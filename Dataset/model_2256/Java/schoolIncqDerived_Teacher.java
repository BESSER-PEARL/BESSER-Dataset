





import java.util.List;
import java.util.ArrayList;

public class schoolIncqDerived_Teacher  {

    private String name;





    private schoolIncqDerived_School schoolincqderived_school;




    private schoolIncqDerived_School schoolincqderived_school;




    private schoolIncqDerived_Course schoolincqderived_course;




    private schoolIncqDerived_School schoolincqderived_school;




    private List<schoolIncqDerived_Course> schoolincqderived_courses;


    public schoolIncqDerived_Teacher(
        String name    ) {
        this.name = name;
        this.schoolincqderived_courses = new ArrayList<>();
    }

    public schoolIncqDerived_Teacher(
        String name        ArrayList<schoolIncqDerived_Course> schoolincqderived_courses    ) {
        this.name = name;
        this.schoolincqderived_courses = schoolincqderived_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public schoolIncqDerived_School getSchoolincqderived_school() {
        return schoolincqderived_school;
    }

    public void setSchoolincqderived_school(schoolIncqDerived_School schoolincqderived_school) {
        this.schoolincqderived_school = schoolincqderived_school;
    }
    public schoolIncqDerived_School getSchoolincqderived_school() {
        return schoolincqderived_school;
    }

    public void setSchoolincqderived_school(schoolIncqDerived_School schoolincqderived_school) {
        this.schoolincqderived_school = schoolincqderived_school;
    }
    public schoolIncqDerived_Course getSchoolincqderived_course() {
        return schoolincqderived_course;
    }

    public void setSchoolincqderived_course(schoolIncqDerived_Course schoolincqderived_course) {
        this.schoolincqderived_course = schoolincqderived_course;
    }
    public schoolIncqDerived_School getSchoolincqderived_school() {
        return schoolincqderived_school;
    }

    public void setSchoolincqderived_school(schoolIncqDerived_School schoolincqderived_school) {
        this.schoolincqderived_school = schoolincqderived_school;
    }
    public List<schoolIncqDerived_Course> getSchoolincqderived_courses() {
        return schoolincqderived_courses;
    }

    public void addSchoolincqderived_course(Schoolincqderived_course schoolincqderived_course) {
        this.schoolincqderived_courses.add(schoolincqderived_course);
    }

}