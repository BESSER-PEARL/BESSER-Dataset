





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String password;
    private String employeeName;
    private int jobLevel;
    private String employeeId;
    private String managerId;
    private int noOfLeaves;
    private String leavesTaken;



    public Employee(
        String password,        String employeeName,        int jobLevel,        String employeeId,        String managerId,        int noOfLeaves,        String leavesTaken    ) {
        this.password = password;
        this.employeeName = employeeName;
        this.jobLevel = jobLevel;
        this.employeeId = employeeId;
        this.managerId = managerId;
        this.noOfLeaves = noOfLeaves;
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
    public String getManagerid() {
        return managerId;
    }

    public void setManagerid(String managerId) {
        this.managerId = managerId;
    }
    public int getNoofleaves() {
        return noOfLeaves;
    }

    public void setNoofleaves(int noOfLeaves) {
        this.noOfLeaves = noOfLeaves;
    }
    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
    }


}