





import java.util.List;
import java.util.ArrayList;

public class gsml_GradingSystem  {






    private List<gsml_Course> gsml_courses;


    public gsml_GradingSystem(
    ) {
        this.gsml_courses = new ArrayList<>();
    }

    public gsml_GradingSystem(
        ArrayList<gsml_Course> gsml_courses    ) {
        this.gsml_courses = gsml_courses;
    }


    public List<gsml_Course> getGsml_courses() {
        return gsml_courses;
    }

    public void addGsml_course(Gsml_course gsml_course) {
        this.gsml_courses.add(gsml_course);
    }

}