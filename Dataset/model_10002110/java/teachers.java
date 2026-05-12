





import java.util.List;
import java.util.ArrayList;

public class teachers  {

    private int classroom;
    private String section;
    private String name;
    private String subject;



    public teachers(
        int classroom,        String section,        String name,        String subject    ) {
        this.classroom = classroom;
        this.section = section;
        this.name = name;
        this.subject = subject;
    }


    public int getClassroom() {
        return classroom;
    }

    public void setClassroom(int classroom) {
        this.classroom = classroom;
    }
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }


}