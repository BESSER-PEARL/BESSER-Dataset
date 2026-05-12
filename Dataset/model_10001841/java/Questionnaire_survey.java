





import java.util.List;
import java.util.ArrayList;

public class Questionnaire_survey  {

    private String Teachers;
    private String Students;



    public Questionnaire_survey(
        String Teachers,        String Students    ) {
        this.Teachers = Teachers;
        this.Students = Students;
    }


    public String getTeachers() {
        return Teachers;
    }

    public void setTeachers(String Teachers) {
        this.Teachers = Teachers;
    }
    public String getStudents() {
        return Students;
    }

    public void setStudents(String Students) {
        this.Students = Students;
    }


}