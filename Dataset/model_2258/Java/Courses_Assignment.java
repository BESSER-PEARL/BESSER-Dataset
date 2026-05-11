





import java.util.List;
import java.util.ArrayList;

public class Courses_Assignment  {

    private String name;
    private boolean mandatory;
    private String description;





    private Courses_Course courses_course;


    public Courses_Assignment(
        String name,        boolean mandatory,        String description    ) {
        this.name = name;
        this.mandatory = mandatory;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Courses_Course getCourses_course() {
        return courses_course;
    }

    public void setCourses_course(Courses_Course courses_course) {
        this.courses_course = courses_course;
    }

}