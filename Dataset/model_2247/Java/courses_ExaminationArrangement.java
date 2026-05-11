





import java.util.List;
import java.util.ArrayList;

public class courses_ExaminationArrangement  {

    private String grade;
    private String type;





    private courses_Content courses_content;


    public courses_ExaminationArrangement(
        String grade,        String type    ) {
        this.grade = grade;
        this.type = type;
    }


    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public courses_Content getCourses_content() {
        return courses_content;
    }

    public void setCourses_content(courses_Content courses_content) {
        this.courses_content = courses_content;
    }

}