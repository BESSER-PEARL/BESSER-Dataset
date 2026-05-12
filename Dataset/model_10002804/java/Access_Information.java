





import java.util.List;
import java.util.ArrayList;

public class Access_Information  {






    private Teacher_Interface teacher_interface;




    private Department department;




    private Student student;


    public Access_Information(
    ) {
    }



    public Teacher_Interface getTeacher_interface() {
        return teacher_interface;
    }

    public void setTeacher_interface(Teacher_Interface teacher_interface) {
        this.teacher_interface = teacher_interface;
    }
    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }
    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }

}