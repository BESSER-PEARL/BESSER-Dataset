





import java.util.List;
import java.util.ArrayList;

public class studyplan_CourseGroup  {

    private String courseStatus;
    private String group;



    public studyplan_CourseGroup(
        String courseStatus,        String group    ) {
        this.courseStatus = courseStatus;
        this.group = group;
    }


    public String getCoursestatus() {
        return courseStatus;
    }

    public void setCoursestatus(String courseStatus) {
        this.courseStatus = courseStatus;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }


}