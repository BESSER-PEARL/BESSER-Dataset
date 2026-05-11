





import java.util.List;
import java.util.ArrayList;

public class studies_University  {

    private String name;





    private List<studies_Course> studies_courses;




    private List<studies_Study> studies_studys;


    public studies_University(
        String name    ) {
        this.name = name;
        this.studies_courses = new ArrayList<>();
        this.studies_studys = new ArrayList<>();
    }

    public studies_University(
        String name        ArrayList<studies_Course> studies_courses,        ArrayList<studies_Study> studies_studys    ) {
        this.name = name;
        this.studies_courses = studies_courses;
        this.studies_studys = studies_studys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<studies_Course> getStudies_courses() {
        return studies_courses;
    }

    public void addStudies_course(Studies_course studies_course) {
        this.studies_courses.add(studies_course);
    }
    public List<studies_Study> getStudies_studys() {
        return studies_studys;
    }

    public void addStudies_study(Studies_study studies_study) {
        this.studies_studys.add(studies_study);
    }

}