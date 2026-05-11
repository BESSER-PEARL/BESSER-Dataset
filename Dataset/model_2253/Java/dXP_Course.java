





import java.util.List;
import java.util.ArrayList;

public class dXP_Course extends Base {

    private String title;
    private String courseCode;





    private dXP_AcademicSession dxp_academicsession;


    public dXP_Course(
        String title,        String courseCode    ) {
        super(
        );
        this.title = title;
        this.courseCode = courseCode;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getCoursecode() {
        return courseCode;
    }

    public void setCoursecode(String courseCode) {
        this.courseCode = courseCode;
    }

    public dXP_AcademicSession getDxp_academicsession() {
        return dxp_academicsession;
    }

    public void setDxp_academicsession(dXP_AcademicSession dxp_academicsession) {
        this.dxp_academicsession = dxp_academicsession;
    }

}