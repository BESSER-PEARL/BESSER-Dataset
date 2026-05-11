





import java.util.List;
import java.util.ArrayList;

public class dXP_Class extends Base {

    private String classCode;
    private String title;
    private String location;
    private String classType;





    private dXP_Enrolment dxp_enrolment;




    private dXP_Course dxp_course;


    public dXP_Class(
        String classCode,        String title,        String location,        String classType    ) {
        super(
        );
        this.classCode = classCode;
        this.title = title;
        this.location = location;
        this.classType = classType;
    }


    public String getClasscode() {
        return classCode;
    }

    public void setClasscode(String classCode) {
        this.classCode = classCode;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getClasstype() {
        return classType;
    }

    public void setClasstype(String classType) {
        this.classType = classType;
    }

    public dXP_Enrolment getDxp_enrolment() {
        return dxp_enrolment;
    }

    public void setDxp_enrolment(dXP_Enrolment dxp_enrolment) {
        this.dxp_enrolment = dxp_enrolment;
    }
    public dXP_Course getDxp_course() {
        return dxp_course;
    }

    public void setDxp_course(dXP_Course dxp_course) {
        this.dxp_course = dxp_course;
    }

}