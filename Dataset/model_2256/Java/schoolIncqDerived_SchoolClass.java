





import java.util.List;
import java.util.ArrayList;

public class schoolIncqDerived_SchoolClass  {

    private String code;





    private schoolIncqDerived_Teacher schoolincqderived_teacher;




    private schoolIncqDerived_Teacher schoolincqderived_teacher;




    private List<schoolIncqDerived_Course> schoolincqderived_courses;




    private schoolIncqDerived_Course schoolincqderived_course;


    public schoolIncqDerived_SchoolClass(
        String code    ) {
        this.code = code;
        this.schoolincqderived_courses = new ArrayList<>();
    }

    public schoolIncqDerived_SchoolClass(
        String code        ArrayList<schoolIncqDerived_Course> schoolincqderived_courses    ) {
        this.code = code;
        this.schoolincqderived_courses = schoolincqderived_courses;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public schoolIncqDerived_Teacher getSchoolincqderived_teacher() {
        return schoolincqderived_teacher;
    }

    public void setSchoolincqderived_teacher(schoolIncqDerived_Teacher schoolincqderived_teacher) {
        this.schoolincqderived_teacher = schoolincqderived_teacher;
    }
    public schoolIncqDerived_Teacher getSchoolincqderived_teacher() {
        return schoolincqderived_teacher;
    }

    public void setSchoolincqderived_teacher(schoolIncqDerived_Teacher schoolincqderived_teacher) {
        this.schoolincqderived_teacher = schoolincqderived_teacher;
    }
    public List<schoolIncqDerived_Course> getSchoolincqderived_courses() {
        return schoolincqderived_courses;
    }

    public void addSchoolincqderived_course(Schoolincqderived_course schoolincqderived_course) {
        this.schoolincqderived_courses.add(schoolincqderived_course);
    }
    public schoolIncqDerived_Course getSchoolincqderived_course() {
        return schoolincqderived_course;
    }

    public void setSchoolincqderived_course(schoolIncqDerived_Course schoolincqderived_course) {
        this.schoolincqderived_course = schoolincqderived_course;
    }

}