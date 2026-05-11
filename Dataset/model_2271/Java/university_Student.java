





import java.util.List;
import java.util.ArrayList;

public class university_Student  {

    private String id;





    private university_Course university_course;




    private List<university_Course> university_courses;


    public university_Student(
        String id    ) {
        this.id = id;
        this.university_courses = new ArrayList<>();
    }

    public university_Student(
        String id        ArrayList<university_Course> university_courses    ) {
        this.id = id;
        this.university_courses = university_courses;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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