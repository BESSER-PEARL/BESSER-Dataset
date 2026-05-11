





import java.util.List;
import java.util.ArrayList;

public class gsml_Grading  {

    private String Semester;





    private gsml_Course gsml_course;


    public gsml_Grading(
        String Semester    ) {
        this.Semester = Semester;
    }


    public String getSemester() {
        return Semester;
    }

    public void setSemester(String Semester) {
        this.Semester = Semester;
    }

    public gsml_Course getGsml_course() {
        return gsml_course;
    }

    public void setGsml_course(gsml_Course gsml_course) {
        this.gsml_course = gsml_course;
    }

}