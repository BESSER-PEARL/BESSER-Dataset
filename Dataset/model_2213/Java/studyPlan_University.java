





import java.util.List;
import java.util.ArrayList;

public class studyPlan_University  {

    private String name;





    private List<studyPlan_Course> studyplan_courses;




    private studyPlan_Course studyplan_course;


    public studyPlan_University(
        String name    ) {
        this.name = name;
        this.studyplan_courses = new ArrayList<>();
    }

    public studyPlan_University(
        String name        ArrayList<studyPlan_Course> studyplan_courses    ) {
        this.name = name;
        this.studyplan_courses = studyplan_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<studyPlan_Course> getStudyplan_courses() {
        return studyplan_courses;
    }

    public void addStudyplan_course(Studyplan_course studyplan_course) {
        this.studyplan_courses.add(studyplan_course);
    }
    public studyPlan_Course getStudyplan_course() {
        return studyplan_course;
    }

    public void setStudyplan_course(studyPlan_Course studyplan_course) {
        this.studyplan_course = studyplan_course;
    }

}