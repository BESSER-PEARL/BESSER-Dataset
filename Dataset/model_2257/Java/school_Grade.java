





import java.util.List;
import java.util.ArrayList;

public class school_Grade  {

    private String year;
    private String grade;





    private school_Course school_course;




    private school_Pupil school_pupil;


    public school_Grade(
        String year,        String grade    ) {
        this.year = year;
        this.grade = grade;
    }


    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }

    public school_Course getSchool_course() {
        return school_course;
    }

    public void setSchool_course(school_Course school_course) {
        this.school_course = school_course;
    }
    public school_Pupil getSchool_pupil() {
        return school_pupil;
    }

    public void setSchool_pupil(school_Pupil school_pupil) {
        this.school_pupil = school_pupil;
    }

}