





import java.util.List;
import java.util.ArrayList;

public class studyprogramme_ElectiveCourseList  {

    private String name;





    private List<studyprogramme_Course> studyprogramme_courses;


    public studyprogramme_ElectiveCourseList(
        String name    ) {
        this.name = name;
        this.studyprogramme_courses = new ArrayList<>();
    }

    public studyprogramme_ElectiveCourseList(
        String name        ArrayList<studyprogramme_Course> studyprogramme_courses    ) {
        this.name = name;
        this.studyprogramme_courses = studyprogramme_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<studyprogramme_Course> getStudyprogramme_courses() {
        return studyprogramme_courses;
    }

    public void addStudyprogramme_course(Studyprogramme_course studyprogramme_course) {
        this.studyprogramme_courses.add(studyprogramme_course);
    }

}