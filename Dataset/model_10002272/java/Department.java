





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String doctorList;
    private String departmentName;
    private String nurseList;
    private String departmentID;



    public Department(
        String doctorList,        String departmentName,        String nurseList,        String departmentID    ) {
        this.doctorList = doctorList;
        this.departmentName = departmentName;
        this.nurseList = nurseList;
        this.departmentID = departmentID;
    }


    public String getDoctorlist() {
        return doctorList;
    }

    public void setDoctorlist(String doctorList) {
        this.doctorList = doctorList;
    }
    public String getDepartmentname() {
        return departmentName;
    }

    public void setDepartmentname(String departmentName) {
        this.departmentName = departmentName;
    }
    public String getNurselist() {
        return nurseList;
    }

    public void setNurselist(String nurseList) {
        this.nurseList = nurseList;
    }
    public String getDepartmentid() {
        return departmentID;
    }

    public void setDepartmentid(String departmentID) {
        this.departmentID = departmentID;
    }


}