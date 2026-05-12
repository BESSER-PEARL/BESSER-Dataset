





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private String ID;
    private String Date;





    private Student student;




    private Faculty faculty;


    public Attendance(
        String ID,        String Date    ) {
        this.ID = ID;
        this.Date = Date;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }
    public Faculty getFaculty() {
        return faculty;
    }

    public void setFaculty(Faculty faculty) {
        this.faculty = faculty;
    }

}