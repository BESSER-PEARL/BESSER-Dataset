





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String managerId;
    private int jobLevel;
    private String employeeName;
    private String leavesTaken;
    private String employeeId;
    private String password;
    private int noOfLeaves;



    public Employee(
        String managerId,        int jobLevel,        String employeeName,        String leavesTaken,        String employeeId,        String password,        int noOfLeaves    ) {
        this.managerId = managerId;
        this.jobLevel = jobLevel;
        this.employeeName = employeeName;
        this.leavesTaken = leavesTaken;
        this.employeeId = employeeId;
        this.password = password;
        this.noOfLeaves = noOfLeaves;
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
    public String getEmployeename() {
        return employeeName;
    }

    public void setEmployeename(String employeeName) {
        this.employeeName = employeeName;
    }
    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
    }
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getNoofleaves() {
        return noOfLeaves;
    }

    public void setNoofleaves(int noOfLeaves) {
        this.noOfLeaves = noOfLeaves;
    }


}