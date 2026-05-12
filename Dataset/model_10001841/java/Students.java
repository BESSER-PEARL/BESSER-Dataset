





import java.util.List;
import java.util.ArrayList;

public class Students  {

    private String Name;
    private None Course;
    private None ID;





    private Teachers teachers;


    public Students(
        String Name,        None Course,        None ID    ) {
        this.Name = Name;
        this.Course = Course;
        this.ID = ID;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public None getCourse() {
        return Course;
    }

    public void setCourse(None Course) {
        this.Course = Course;
    }
    public None getId() {
        return ID;
    }

    public void setId(None ID) {
        this.ID = ID;
    }

    public Teachers getTeachers() {
        return teachers;
    }

    public void setTeachers(Teachers teachers) {
        this.teachers = teachers;
    }

}