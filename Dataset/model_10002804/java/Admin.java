





import java.util.List;
import java.util.ArrayList;

public class Admin  {






    private List<Student> students;




    private List<Teacher_Interface> teacher_interfaces;


    public Admin(
    ) {
        this.students = new ArrayList<>();
        this.teacher_interfaces = new ArrayList<>();
    }

    public Admin(
        ArrayList<Student> students,        ArrayList<Teacher_Interface> teacher_interfaces    ) {
        this.students = students;
        this.teacher_interfaces = teacher_interfaces;
    }


    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }
    public List<Teacher_Interface> getTeacher_interfaces() {
        return teacher_interfaces;
    }

    public void addTeacher_interface(Teacher_interface teacher_interface) {
        this.teacher_interfaces.add(teacher_interface);
    }

}