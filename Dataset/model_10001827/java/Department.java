





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String departmentID;
    private String departmentName;
    private String doctorList;
    private String nurseList;





    private Hospital hospital;


    public Department(
        String departmentID,        String departmentName,        String doctorList,        String nurseList    ) {
        this.departmentID = departmentID;
        this.departmentName = departmentName;
        this.doctorList = doctorList;
        this.nurseList = nurseList;
    }


    public String getDepartmentid() {
        return departmentID;
    }

    public void setDepartmentid(String departmentID) {
        this.departmentID = departmentID;
    }
    public String getDepartmentname() {
        return departmentName;
    }

    public void setDepartmentname(String departmentName) {
        this.departmentName = departmentName;
    }
    public String getDoctorlist() {
        return doctorList;
    }

    public void setDoctorlist(String doctorList) {
        this.doctorList = doctorList;
    }
    public String getNurselist() {
        return nurseList;
    }

    public void setNurselist(String nurseList) {
        this.nurseList = nurseList;
    }

    public Hospital getHospital() {
        return hospital;
    }

    public void setHospital(Hospital hospital) {
        this.hospital = hospital;
    }

}