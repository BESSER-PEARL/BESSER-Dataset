





import java.util.List;
import java.util.ArrayList;

public class Register  {

    private None professer_id;
    private None student_name;
    private None professor_name;
    private String course_id;
    private String course_name;
    private None student_id;





    private List<student> students;




    private List<Professor> professors;


    public Register(
        None professer_id,        None student_name,        None professor_name,        String course_id,        String course_name,        None student_id    ) {
        this.professer_id = professer_id;
        this.student_name = student_name;
        this.professor_name = professor_name;
        this.course_id = course_id;
        this.course_name = course_name;
        this.student_id = student_id;
        this.students = new ArrayList<>();
        this.professors = new ArrayList<>();
    }

    public Register(
        None professer_id,        None student_name,        None professor_name,        String course_id,        String course_name,        None student_id        ArrayList<student> students,        ArrayList<Professor> professors    ) {
        this.professer_id = professer_id;
        this.student_name = student_name;
        this.professor_name = professor_name;
        this.course_id = course_id;
        this.course_name = course_name;
        this.student_id = student_id;
        this.students = students;
        this.professors = professors;
    }

    public None getProfesser_id() {
        return professer_id;
    }

    public void setProfesser_id(None professer_id) {
        this.professer_id = professer_id;
    }
    public None getStudent_name() {
        return student_name;
    }

    public void setStudent_name(None student_name) {
        this.student_name = student_name;
    }
    public None getProfessor_name() {
        return professor_name;
    }

    public void setProfessor_name(None professor_name) {
        this.professor_name = professor_name;
    }
    public String getCourse_id() {
        return course_id;
    }

    public void setCourse_id(String course_id) {
        this.course_id = course_id;
    }
    public String getCourse_name() {
        return course_name;
    }

    public void setCourse_name(String course_name) {
        this.course_name = course_name;
    }
    public None getStudent_id() {
        return student_id;
    }

    public void setStudent_id(None student_id) {
        this.student_id = student_id;
    }

    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }
    public List<Professor> getProfessors() {
        return professors;
    }

    public void addProfessor(Professor professor) {
        this.professors.add(professor);
    }

}