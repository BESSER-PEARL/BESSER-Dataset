





import java.util.List;
import java.util.ArrayList;

public class studyprogramme_University  {

    private String name;





    private List<studyprogramme_Specialization> studyprogramme_specializations;




    private List<studyprogramme_Programme> studyprogramme_programmes;




    private List<studyprogramme_Course> studyprogramme_courses;


    public studyprogramme_University(
        String name    ) {
        this.name = name;
        this.studyprogramme_specializations = new ArrayList<>();
        this.studyprogramme_programmes = new ArrayList<>();
        this.studyprogramme_courses = new ArrayList<>();
    }

    public studyprogramme_University(
        String name        ArrayList<studyprogramme_Specialization> studyprogramme_specializations,        ArrayList<studyprogramme_Programme> studyprogramme_programmes,        ArrayList<studyprogramme_Course> studyprogramme_courses    ) {
        this.name = name;
        this.studyprogramme_specializations = studyprogramme_specializations;
        this.studyprogramme_programmes = studyprogramme_programmes;
        this.studyprogramme_courses = studyprogramme_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<studyprogramme_Specialization> getStudyprogramme_specializations() {
        return studyprogramme_specializations;
    }

    public void addStudyprogramme_specialization(Studyprogramme_specialization studyprogramme_specialization) {
        this.studyprogramme_specializations.add(studyprogramme_specialization);
    }
    public List<studyprogramme_Programme> getStudyprogramme_programmes() {
        return studyprogramme_programmes;
    }

    public void addStudyprogramme_programme(Studyprogramme_programme studyprogramme_programme) {
        this.studyprogramme_programmes.add(studyprogramme_programme);
    }
    public List<studyprogramme_Course> getStudyprogramme_courses() {
        return studyprogramme_courses;
    }

    public void addStudyprogramme_course(Studyprogramme_course studyprogramme_course) {
        this.studyprogramme_courses.add(studyprogramme_course);
    }

}