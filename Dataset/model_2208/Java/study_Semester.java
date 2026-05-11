





import java.util.List;
import java.util.ArrayList;

public class study_Semester  {

    private String Season;
    private int year;





    private study_SemesterCourse study_semestercourse;




    private study_Programme study_programme;




    private study_Programme study_programme;




    private List<study_SemesterCourse> study_semestercourses;


    public study_Semester(
        String Season,        int year    ) {
        this.Season = Season;
        this.year = year;
        this.study_semestercourses = new ArrayList<>();
    }

    public study_Semester(
        String Season,        int year        ArrayList<study_SemesterCourse> study_semestercourses    ) {
        this.Season = Season;
        this.year = year;
        this.study_semestercourses = study_semestercourses;
    }

    public String getSeason() {
        return Season;
    }

    public void setSeason(String Season) {
        this.Season = Season;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public study_SemesterCourse getStudy_semestercourse() {
        return study_semestercourse;
    }

    public void setStudy_semestercourse(study_SemesterCourse study_semestercourse) {
        this.study_semestercourse = study_semestercourse;
    }
    public study_Programme getStudy_programme() {
        return study_programme;
    }

    public void setStudy_programme(study_Programme study_programme) {
        this.study_programme = study_programme;
    }
    public study_Programme getStudy_programme() {
        return study_programme;
    }

    public void setStudy_programme(study_Programme study_programme) {
        this.study_programme = study_programme;
    }
    public List<study_SemesterCourse> getStudy_semestercourses() {
        return study_semestercourses;
    }

    public void addStudy_semestercourse(Study_semestercourse study_semestercourse) {
        this.study_semestercourses.add(study_semestercourse);
    }

}