





import java.util.List;
import java.util.ArrayList;

public class programmes_University  {

    private String name;





    private List<programmes_Course> programmes_courses;




    private List<programmes_Programme> programmes_programmes;


    public programmes_University(
        String name    ) {
        this.name = name;
        this.programmes_courses = new ArrayList<>();
        this.programmes_programmes = new ArrayList<>();
    }

    public programmes_University(
        String name        ArrayList<programmes_Course> programmes_courses,        ArrayList<programmes_Programme> programmes_programmes    ) {
        this.name = name;
        this.programmes_courses = programmes_courses;
        this.programmes_programmes = programmes_programmes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<programmes_Course> getProgrammes_courses() {
        return programmes_courses;
    }

    public void addProgrammes_course(Programmes_course programmes_course) {
        this.programmes_courses.add(programmes_course);
    }
    public List<programmes_Programme> getProgrammes_programmes() {
        return programmes_programmes;
    }

    public void addProgrammes_programme(Programmes_programme programmes_programme) {
        this.programmes_programmes.add(programmes_programme);
    }

}