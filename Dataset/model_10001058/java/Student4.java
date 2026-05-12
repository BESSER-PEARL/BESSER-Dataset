





import java.util.List;
import java.util.ArrayList;

public class Student4  {

    private String courseName;
    private int courseId;



    public Student4(
        String courseName,        int courseId    ) {
        this.courseName = courseName;
        this.courseId = courseId;
    }


    public String getCoursename() {
        return courseName;
    }

    public void setCoursename(String courseName) {
        this.courseName = courseName;
    }
    public int getCourseid() {
        return courseId;
    }

    public void setCourseid(int courseId) {
        this.courseId = courseId;
    }


}