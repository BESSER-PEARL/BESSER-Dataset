





import java.util.List;
import java.util.ArrayList;

public class studyplan_Semester  {

    private String name;
    private String season;
    private int year;





    private studyplan_Program studyplan_program;


    public studyplan_Semester(
        String name,        String season,        int year    ) {
        this.name = name;
        this.season = season;
        this.year = year;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSeason() {
        return season;
    }

    public void setSeason(String season) {
        this.season = season;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public studyplan_Program getStudyplan_program() {
        return studyplan_program;
    }

    public void setStudyplan_program(studyplan_Program studyplan_program) {
        this.studyplan_program = studyplan_program;
    }

}