





import java.util.List;
import java.util.ArrayList;

public class classrooms  {

    private String subject;
    private String teacher;
    private int number;



    public classrooms(
        String subject,        String teacher,        int number    ) {
        this.subject = subject;
        this.teacher = teacher;
        this.number = number;
    }


    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public String getTeacher() {
        return teacher;
    }

    public void setTeacher(String teacher) {
        this.teacher = teacher;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}