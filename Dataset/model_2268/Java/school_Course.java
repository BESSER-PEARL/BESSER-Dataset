





import java.util.List;
import java.util.ArrayList;

public class school_Course  {

    private String name;
    private String courseNumber;





    private school_School school_school;




    private school_CourseOfStudy school_courseofstudy;


    public school_Course(
        String name,        String courseNumber    ) {
        this.name = name;
        this.courseNumber = courseNumber;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCoursenumber() {
        return courseNumber;
    }

    public void setCoursenumber(String courseNumber) {
        this.courseNumber = courseNumber;
    }

    public school_School getSchool_school() {
        return school_school;
    }

    public void setSchool_school(school_School school_school) {
        this.school_school = school_school;
    }
    public school_CourseOfStudy getSchool_courseofstudy() {
        return school_courseofstudy;
    }

    public void setSchool_courseofstudy(school_CourseOfStudy school_courseofstudy) {
        this.school_courseofstudy = school_courseofstudy;
    }

}