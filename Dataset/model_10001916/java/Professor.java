





import java.util.List;
import java.util.ArrayList;

public class Professor  {

    private String course_name;
    private None professor_id;
    private None course_id;
    private String professor_name;





    private List<student> students;


    public Professor(
        String course_name,        None professor_id,        None course_id,        String professor_name    ) {
        this.course_name = course_name;
        this.professor_id = professor_id;
        this.course_id = course_id;
        this.professor_name = professor_name;
        this.students = new ArrayList<>();
    }

    public Professor(
        String course_name,        None professor_id,        None course_id,        String professor_name        ArrayList<student> students    ) {
        this.course_name = course_name;
        this.professor_id = professor_id;
        this.course_id = course_id;
        this.professor_name = professor_name;
        this.students = students;
    }

    public String getCourse_name() {
        return course_name;
    }

    public void setCourse_name(String course_name) {
        this.course_name = course_name;
    }
    public None getProfessor_id() {
        return professor_id;
    }

    public void setProfessor_id(None professor_id) {
        this.professor_id = professor_id;
    }
    public None getCourse_id() {
        return course_id;
    }

    public void setCourse_id(None course_id) {
        this.course_id = course_id;
    }
    public String getProfessor_name() {
        return professor_name;
    }

    public void setProfessor_name(String professor_name) {
        this.professor_name = professor_name;
    }

    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}