





import java.util.List;
import java.util.ArrayList;

public class education_Student  {

    private String name;





    private education_Course education_course;




    private education_School education_school;




    private List<education_Course> education_courses;




    private List<education_School> education_schools;


    public education_Student(
        String name    ) {
        this.name = name;
        this.education_courses = new ArrayList<>();
        this.education_schools = new ArrayList<>();
    }

    public education_Student(
        String name        ArrayList<education_Course> education_courses,        ArrayList<education_School> education_schools    ) {
        this.name = name;
        this.education_courses = education_courses;
        this.education_schools = education_schools;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public education_Course getEducation_course() {
        return education_course;
    }

    public void setEducation_course(education_Course education_course) {
        this.education_course = education_course;
    }
    public education_School getEducation_school() {
        return education_school;
    }

    public void setEducation_school(education_School education_school) {
        this.education_school = education_school;
    }
    public List<education_Course> getEducation_courses() {
        return education_courses;
    }

    public void addEducation_course(Education_course education_course) {
        this.education_courses.add(education_course);
    }
    public List<education_School> getEducation_schools() {
        return education_schools;
    }

    public void addEducation_school(Education_school education_school) {
        this.education_schools.add(education_school);
    }

}