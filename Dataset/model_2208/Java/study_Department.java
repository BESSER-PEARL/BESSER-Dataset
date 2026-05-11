





import java.util.List;
import java.util.ArrayList;

public class study_Department  {

    private String name;





    private List<study_Programme> study_programmes;




    private study_Course study_course;




    private study_Programme study_programme;




    private List<study_Course> study_courses;


    public study_Department(
        String name    ) {
        this.name = name;
        this.study_programmes = new ArrayList<>();
        this.study_courses = new ArrayList<>();
    }

    public study_Department(
        String name        ArrayList<study_Programme> study_programmes,        ArrayList<study_Course> study_courses    ) {
        this.name = name;
        this.study_programmes = study_programmes;
        this.study_courses = study_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<study_Programme> getStudy_programmes() {
        return study_programmes;
    }

    public void addStudy_programme(Study_programme study_programme) {
        this.study_programmes.add(study_programme);
    }
    public study_Course getStudy_course() {
        return study_course;
    }

    public void setStudy_course(study_Course study_course) {
        this.study_course = study_course;
    }
    public study_Programme getStudy_programme() {
        return study_programme;
    }

    public void setStudy_programme(study_Programme study_programme) {
        this.study_programme = study_programme;
    }
    public List<study_Course> getStudy_courses() {
        return study_courses;
    }

    public void addStudy_course(Study_course study_course) {
        this.study_courses.add(study_course);
    }

}