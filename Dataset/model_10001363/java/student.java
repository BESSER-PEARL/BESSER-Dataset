





import java.util.List;
import java.util.ArrayList;

public class student  {

    private String minor_dept;
    private String major_dept;



    public student(
        String minor_dept,        String major_dept    ) {
        this.minor_dept = minor_dept;
        this.major_dept = major_dept;
    }


    public String getMinor_dept() {
        return minor_dept;
    }

    public void setMinor_dept(String minor_dept) {
        this.minor_dept = minor_dept;
    }
    public String getMajor_dept() {
        return major_dept;
    }

    public void setMajor_dept(String major_dept) {
        this.major_dept = major_dept;
    }


}