





import java.util.List;
import java.util.ArrayList;

public class Courses_Person  {

    private String role;
    private String name;
    private int id;





    private Courses_Course courses_course;


    public Courses_Person(
        String role,        String name,        int id    ) {
        this.role = role;
        this.name = name;
        this.id = id;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Courses_Course getCourses_course() {
        return courses_course;
    }

    public void setCourses_course(Courses_Course courses_course) {
        this.courses_course = courses_course;
    }

}