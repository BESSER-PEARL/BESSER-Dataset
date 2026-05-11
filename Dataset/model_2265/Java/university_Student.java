





import java.util.List;
import java.util.ArrayList;

public class university_Student  {

    private String id;
    private String name;





    private List<university_Course> university_courses;




    private university_Course university_course;




    private university_University university_university;


    public university_Student(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
        this.university_courses = new ArrayList<>();
    }

    public university_Student(
        String id,        String name        ArrayList<university_Course> university_courses    ) {
        this.id = id;
        this.name = name;
        this.university_courses = university_courses;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<university_Course> getUniversity_courses() {
        return university_courses;
    }

    public void addUniversity_course(University_course university_course) {
        this.university_courses.add(university_course);
    }
    public university_Course getUniversity_course() {
        return university_course;
    }

    public void setUniversity_course(university_Course university_course) {
        this.university_course = university_course;
    }
    public university_University getUniversity_university() {
        return university_university;
    }

    public void setUniversity_university(university_University university_university) {
        this.university_university = university_university;
    }

}