





import java.util.List;
import java.util.ArrayList;

public class exam  {






    private teachers teachers;




    private List<student> students;


    public exam(
    ) {
        this.students = new ArrayList<>();
    }

    public exam(
        ArrayList<student> students    ) {
        this.students = students;
    }


    public teachers getTeachers() {
        return teachers;
    }

    public void setTeachers(teachers teachers) {
        this.teachers = teachers;
    }
    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}