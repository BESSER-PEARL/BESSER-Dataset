





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String password;
    private String employeeId;
    private String employeeName;
    private String managerId;
    private int noOfLeaves;
    private int jobLevel;
    private String leavesTaken;



    public Employee(
        String password,        String employeeId,        String employeeName,        String managerId,        int noOfLeaves,        int jobLevel,        String leavesTaken    ) {
        this.password = password;
        this.employeeId = employeeId;
        this.employeeName = employeeName;
        this.managerId = managerId;
        this.noOfLeaves = noOfLeaves;
        this.jobLevel = jobLevel;
        this.leavesTaken = leavesTaken;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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


}