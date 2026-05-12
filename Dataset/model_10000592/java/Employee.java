





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String employeeId;
    private String managerId;
    private int jobLevel;
    private String leavesTaken;
    private String password;
    private String employeeName;
    private int noOfLeaves;



    public Employee(
        String employeeId,        String managerId,        int jobLevel,        String leavesTaken,        String password,        String employeeName,        int noOfLeaves    ) {
        this.employeeId = employeeId;
        this.managerId = managerId;
        this.jobLevel = jobLevel;
        this.leavesTaken = leavesTaken;
        this.password = password;
        this.employeeName = employeeName;
        this.noOfLeaves = noOfLeaves;
    }


    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }
    public String getManagerid() {
        return managerId;
    }

    public void setManagerid(String managerId) {
        this.managerId = managerId;
    }
    public int getJoblevel() {
        return jobLevel;
    }

    public void setJoblevel(int jobLevel) {
        this.jobLevel = jobLevel;
    }
    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmployeename() {
        return employeeName;
    }

    public void setEmployeename(String employeeName) {
        this.employeeName = employeeName;
    }
    public int getNoofleaves() {
        return noOfLeaves;
    }

    public void setNoofleaves(int noOfLeaves) {
        this.noOfLeaves = noOfLeaves;
    }


}