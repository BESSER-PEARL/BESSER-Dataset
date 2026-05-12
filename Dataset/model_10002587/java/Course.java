





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String Timing;
    private String name;





    private Student student;




    private List<Teacher> teachers;


    public Course(
        String Timing,        String name    ) {
        this.Timing = Timing;
        this.name = name;
        this.teachers = new ArrayList<>();
    }

    public Course(
        String Timing,        String name        ArrayList<Teacher> teachers    ) {
        this.Timing = Timing;
        this.name = name;
        this.teachers = teachers;
    }

    public String getTiming() {
        return Timing;
    }

    public void setTiming(String Timing) {
        this.Timing = Timing;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }
    public List<Teacher> getTeachers() {
        return teachers;
    }

    public void addTeacher(Teacher teacher) {
        this.teachers.add(teacher);
    }

}