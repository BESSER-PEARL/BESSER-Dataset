





import java.util.List;
import java.util.ArrayList;

public class University_Course  {

    private int courseNumber;
    private String name;
    private String courseType;





    private University_Student university_student;




    private List<University_Course> university_courses;




    private University_Professor university_professor;


    public University_Course(
        int courseNumber,        String name,        String courseType    ) {
        this.courseNumber = courseNumber;
        this.name = name;
        this.courseType = courseType;
        this.university_courses = new ArrayList<>();
    }

    public University_Course(
        int courseNumber,        String name,        String courseType        ArrayList<University_Course> university_courses    ) {
        this.courseNumber = courseNumber;
        this.name = name;
        this.courseType = courseType;
        this.university_courses = university_courses;
    }

    public int getCoursenumber() {
        return courseNumber;
    }

    public void setCoursenumber(int courseNumber) {
        this.courseNumber = courseNumber;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCoursetype() {
        return courseType;
    }

    public void setCoursetype(String courseType) {
        this.courseType = courseType;
    }

    public University_Student getUniversity_student() {
        return university_student;
    }

    public void setUniversity_student(University_Student university_student) {
        this.university_student = university_student;
    }
    public List<University_Course> getUniversity_courses() {
        return university_courses;
    }

    public void addUniversity_course(University_course university_course) {
        this.university_courses.add(university_course);
    }
    public University_Professor getUniversity_professor() {
        return university_professor;
    }

    public void setUniversity_professor(University_Professor university_professor) {
        this.university_professor = university_professor;
    }

}