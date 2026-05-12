





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String employeeId;
    private int jobLevel;
    private String leavesTaken;
    private String employeeName;
    private int noOfLeaves;
    private String password;
    private String managerId;



    public Employee(
        String employeeId,        int jobLevel,        String leavesTaken,        String employeeName,        int noOfLeaves,        String password,        String managerId    ) {
        this.employeeId = employeeId;
        this.jobLevel = jobLevel;
        this.leavesTaken = leavesTaken;
        this.employeeName = employeeName;
        this.noOfLeaves = noOfLeaves;
        this.password = password;
        this.managerId = managerId;
    }


    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
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


}