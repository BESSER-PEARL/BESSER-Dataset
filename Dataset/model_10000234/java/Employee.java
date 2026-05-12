





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private int jobLevel;
    private String employeeId;
    private String employeeName;
    private String password;
    private String managerId;
    private String leavesTaken;
    private int noOfLeaves;



    public Employee(
        int jobLevel,        String employeeId,        String employeeName,        String password,        String managerId,        String leavesTaken,        int noOfLeaves    ) {
        this.jobLevel = jobLevel;
        this.employeeId = employeeId;
        this.employeeName = employeeName;
        this.password = password;
        this.managerId = managerId;
        this.leavesTaken = leavesTaken;
        this.noOfLeaves = noOfLeaves;
    }


    public int getJoblevel() {
        return jobLevel;
    }

    public void setJoblevel(int jobLevel) {
        this.jobLevel = jobLevel;
    }
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }
    public String getEmployeename() {
        return employeeName;
    }

    public void setEmployeename(String employeeName) {
        this.employeeName = employeeName;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getManagerid() {
        return managerId;
    }

    public void setManagerid(String managerId) {
        this.managerId = managerId;
    }
    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
    }
    public int getNoofleaves() {
        return noOfLeaves;
    }

    public void setNoofleaves(int noOfLeaves) {
        this.noOfLeaves = noOfLeaves;
    }


}