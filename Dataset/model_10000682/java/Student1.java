





import java.util.List;
import java.util.ArrayList;

public class Student1  {

    private int yearOfStudy;
    private String school;
    private String course;



    public Student1(
        int yearOfStudy,        String school,        String course    ) {
        this.yearOfStudy = yearOfStudy;
        this.school = school;
        this.course = course;
    }


    public int getYearofstudy() {
        return yearOfStudy;
    }

    public void setYearofstudy(int yearOfStudy) {
        this.yearOfStudy = yearOfStudy;
    }
    public String getSchool() {
        return school;
    }

    public void setSchool(String school) {
        this.school = school;
    }
    public String getCourse() {
        return course;
    }

    public void setCourse(String course) {
        this.course = course;
    }


}