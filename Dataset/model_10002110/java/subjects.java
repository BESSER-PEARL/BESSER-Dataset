





import java.util.List;
import java.util.ArrayList;

public class subjects  {

    private int classroom;
    private String teacher;
    private String name;
    private String Section;



    public subjects(
        int classroom,        String teacher,        String name,        String Section    ) {
        this.classroom = classroom;
        this.teacher = teacher;
        this.name = name;
        this.Section = Section;
    }


    public int getClassroom() {
        return classroom;
    }

    public void setClassroom(int classroom) {
        this.classroom = classroom;
    }
    public String getTeacher() {
        return teacher;
    }

    public void setTeacher(String teacher) {
        this.teacher = teacher;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSection() {
        return Section;
    }

    public void setSection(String Section) {
        this.Section = Section;
    }


}