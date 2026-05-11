





import java.util.List;
import java.util.ArrayList;

public class study_Course  {

    private String code;
    private String name;
    private String season;
    private int year;
    private float credits;





    private study_Semester study_semester;




    private study_Department study_department;




    private study_Department study_department;


    public study_Course(
        String code,        String name,        String season,        int year,        float credits    ) {
        this.code = code;
        this.name = name;
        this.season = season;
        this.year = year;
        this.credits = credits;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
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
    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
    }

    public study_Semester getStudy_semester() {
        return study_semester;
    }

    public void setStudy_semester(study_Semester study_semester) {
        this.study_semester = study_semester;
    }
    public study_Department getStudy_department() {
        return study_department;
    }

    public void setStudy_department(study_Department study_department) {
        this.study_department = study_department;
    }
    public study_Department getStudy_department() {
        return study_department;
    }

    public void setStudy_department(study_Department study_department) {
        this.study_department = study_department;
    }

}