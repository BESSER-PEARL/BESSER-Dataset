





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private None teachers__;
    private None hod;
    private None course;
    private None students__;





    private List<Student> students;




    private List<Teacher_Interface> teacher_interfaces;


    public Department(
        None teachers__,        None hod,        None course,        None students__    ) {
        this.teachers__ = teachers__;
        this.hod = hod;
        this.course = course;
        this.students__ = students__;
        this.students = new ArrayList<>();
        this.teacher_interfaces = new ArrayList<>();
    }

    public Department(
        None teachers__,        None hod,        None course,        None students__        ArrayList<Student> students,        ArrayList<Teacher_Interface> teacher_interfaces    ) {
        this.teachers__ = teachers__;
        this.hod = hod;
        this.course = course;
        this.students__ = students__;
        this.students = students;
        this.teacher_interfaces = teacher_interfaces;
    }

    public None getTeachers__() {
        return teachers__;
    }

    public void setTeachers__(None teachers__) {
        this.teachers__ = teachers__;
    }
    public None getHod() {
        return hod;
    }

    public void setHod(None hod) {
        this.hod = hod;
    }
    public None getCourse() {
        return course;
    }

    public void setCourse(None course) {
        this.course = course;
    }
    public None getStudents__() {
        return students__;
    }

    public void setStudents__(None students__) {
        this.students__ = students__;
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