





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private None lecturer__;
    private None course;
    private None hod;
    private None students__;





    private Lecturer lecturer;




    private HOD hod;




    private List<Student> students;


    public Department(
        None lecturer__,        None course,        None hod,        None students__    ) {
        this.lecturer__ = lecturer__;
        this.course = course;
        this.hod = hod;
        this.students__ = students__;
        this.students = new ArrayList<>();
    }

    public Department(
        None lecturer__,        None course,        None hod,        None students__        ArrayList<Student> students    ) {
        this.lecturer__ = lecturer__;
        this.course = course;
        this.hod = hod;
        this.students__ = students__;
        this.students = students;
    }

    public None getLecturer__() {
        return lecturer__;
    }

    public void setLecturer__(None lecturer__) {
        this.lecturer__ = lecturer__;
    }
    public None getCourse() {
        return course;
    }

    public void setCourse(None course) {
        this.course = course;
    }
    public None getHod() {
        return hod;
    }

    public void setHod(None hod) {
        this.hod = hod;
    }
    public None getStudents__() {
        return students__;
    }

    public void setStudents__(None students__) {
        this.students__ = students__;
    }

    public Lecturer getLecturer() {
        return lecturer;
    }

    public void setLecturer(Lecturer lecturer) {
        this.lecturer = lecturer;
    }
    public HOD getHod() {
        return hod;
    }

    public void setHod(HOD hod) {
        this.hod = hod;
    }
    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}