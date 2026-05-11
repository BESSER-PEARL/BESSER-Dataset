





import java.util.List;
import java.util.ArrayList;

public class study_Specialization  {

    private String name;





    private study_Programme study_programme;




    private study_Semester study_semester;




    private study_Programme study_programme;




    private List<study_Semester> study_semesters;


    public study_Specialization(
        String name    ) {
        this.name = name;
        this.study_semesters = new ArrayList<>();
    }

    public study_Specialization(
        String name        ArrayList<study_Semester> study_semesters    ) {
        this.name = name;
        this.study_semesters = study_semesters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public study_Programme getStudy_programme() {
        return study_programme;
    }

    public void setStudy_programme(study_Programme study_programme) {
        this.study_programme = study_programme;
    }
    public study_Semester getStudy_semester() {
        return study_semester;
    }

    public void setStudy_semester(study_Semester study_semester) {
        this.study_semester = study_semester;
    }
    public study_Programme getStudy_programme() {
        return study_programme;
    }

    public void setStudy_programme(study_Programme study_programme) {
        this.study_programme = study_programme;
    }
    public List<study_Semester> getStudy_semesters() {
        return study_semesters;
    }

    public void addStudy_semester(Study_semester study_semester) {
        this.study_semesters.add(study_semester);
    }

}