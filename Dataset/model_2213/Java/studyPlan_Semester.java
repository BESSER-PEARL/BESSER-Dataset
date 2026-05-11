





import java.util.List;
import java.util.ArrayList;

public class studyPlan_Semester  {

    private String codename;
    private String season;
    private int year;



    public studyPlan_Semester(
        String codename,        String season,        int year    ) {
        this.codename = codename;
        this.season = season;
        this.year = year;
    }


    public String getCodename() {
        return codename;
    }

    public void setCodename(String codename) {
        this.codename = codename;
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