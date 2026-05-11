





import java.util.List;
import java.util.ArrayList;

public class studyplan_Semester  {

    private int year;
    private String name;
    private String season;



    public studyplan_Semester(
        int year,        String name,        String season    ) {
        this.year = year;
        this.name = name;
        this.season = season;
    }


    public int getYear() {
        return year;
    }

    public void setYear(int year) {
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


}