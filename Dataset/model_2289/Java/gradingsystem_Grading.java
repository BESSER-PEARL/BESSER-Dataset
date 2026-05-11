





import java.util.List;
import java.util.ArrayList;

public class gradingsystem_Grading  {

    private String semester;





    private gradingsystem_Course gradingsystem_course;


    public gradingsystem_Grading(
        String semester    ) {
        this.semester = semester;
    }


    public String getSemester() {
        return semester;
    }

    public void setSemester(String semester) {
        this.semester = semester;
    }

    public gradingsystem_Course getGradingsystem_course() {
        return gradingsystem_course;
    }

    public void setGradingsystem_course(gradingsystem_Course gradingsystem_course) {
        this.gradingsystem_course = gradingsystem_course;
    }

}