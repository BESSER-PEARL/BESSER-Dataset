





import java.util.List;
import java.util.ArrayList;

public class university_Professor  {

    private String name;





    private university_Course university_course;




    private List<university_Course> university_courses;


    public university_Professor(
        String name    ) {
        this.name = name;
        this.university_courses = new ArrayList<>();
    }

    public university_Professor(
        String name        ArrayList<university_Course> university_courses    ) {
        this.name = name;
        this.university_courses = university_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public university_Course getUniversity_course() {
        return university_course;
    }

    public void setUniversity_course(university_Course university_course) {
        this.university_course = university_course;
    }
    public List<university_Course> getUniversity_courses() {
        return university_courses;
    }

    public void addUniversity_course(University_course university_course) {
        this.university_courses.add(university_course);
    }

}