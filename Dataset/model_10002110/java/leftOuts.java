





import java.util.List;
import java.util.ArrayList;

public class leftOuts  {

    private String students;
    private None subject;
    private None classroom;
    private None teachers;



    public leftOuts(
        String students,        None subject,        None classroom,        None teachers    ) {
        this.students = students;
        this.subject = subject;
        this.classroom = classroom;
        this.teachers = teachers;
    }


    public String getStudents() {
        return students;
    }

    public void setStudents(String students) {
        this.students = students;
    }
    public None getSubject() {
        return subject;
    }

    public void setSubject(None subject) {
        this.subject = subject;
    }
    public None getClassroom() {
        return classroom;
    }

    public void setClassroom(None classroom) {
        this.classroom = classroom;
    }
    public None getTeachers() {
        return teachers;
    }

    public void setTeachers(None teachers) {
        this.teachers = teachers;
    }


}