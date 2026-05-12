





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private int noOfLeaves;
    private int jobLevel;
    private String employeeName;
    private String employeeId;
    private String password;
    private String managerId;
    private String leavesTaken;



    public Employee(
        int noOfLeaves,        int jobLevel,        String employeeName,        String employeeId,        String password,        String managerId,        String leavesTaken    ) {
        this.noOfLeaves = noOfLeaves;
        this.jobLevel = jobLevel;
        this.employeeName = employeeName;
        this.employeeId = employeeId;
        this.password = password;
        this.managerId = managerId;
        this.leavesTaken = leavesTaken;
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
    public String getEmployeename() {
        return employeeName;
    }

    public void setEmployeename(String employeeName) {
        this.employeeName = employeeName;
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


}