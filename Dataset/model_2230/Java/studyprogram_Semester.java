





import java.util.List;
import java.util.ArrayList;

public class studyprogram_Semester  {

    private int year;
    private String season;





    private studyprogram_Program studyprogram_program;


    public studyprogram_Semester(
        int year,        String season    ) {
        this.year = year;
        this.season = season;
    }


    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getSeason() {
        return season;
    }

    public void setSeason(String season) {
        this.season = season;
    }

    public studyprogram_Program getStudyprogram_program() {
        return studyprogram_program;
    }

    public void setStudyprogram_program(studyprogram_Program studyprogram_program) {
        this.studyprogram_program = studyprogram_program;
    }

}