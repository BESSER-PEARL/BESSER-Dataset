





import java.util.List;
import java.util.ArrayList;

public class study_Semester  {

    private String season;
    private int year;



    public study_Semester(
        String season,        int year    ) {
        this.season = season;
        this.year = year;
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


}