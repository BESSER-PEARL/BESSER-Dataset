





import java.util.List;
import java.util.ArrayList;

public class ntnustudies_Department  {

    private String shortName;
    private String name;





    private List<ntnustudies_Programme> ntnustudies_programmes;




    private List<ntnustudies_Course> ntnustudies_courses;


    public ntnustudies_Department(
        String shortName,        String name    ) {
        this.shortName = shortName;
        this.name = name;
        this.ntnustudies_programmes = new ArrayList<>();
        this.ntnustudies_courses = new ArrayList<>();
    }

    public ntnustudies_Department(
        String shortName,        String name        ArrayList<ntnustudies_Programme> ntnustudies_programmes,        ArrayList<ntnustudies_Course> ntnustudies_courses    ) {
        this.shortName = shortName;
        this.name = name;
        this.ntnustudies_programmes = ntnustudies_programmes;
        this.ntnustudies_courses = ntnustudies_courses;
    }

    public String getShortname() {
        return shortName;
    }

    public void setShortname(String shortName) {
        this.shortName = shortName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ntnustudies_Programme> getNtnustudies_programmes() {
        return ntnustudies_programmes;
    }

    public void addNtnustudies_programme(Ntnustudies_programme ntnustudies_programme) {
        this.ntnustudies_programmes.add(ntnustudies_programme);
    }
    public List<ntnustudies_Course> getNtnustudies_courses() {
        return ntnustudies_courses;
    }

    public void addNtnustudies_course(Ntnustudies_course ntnustudies_course) {
        this.ntnustudies_courses.add(ntnustudies_course);
    }

}