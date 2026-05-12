





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String leavesTaken;
    private int noOfLeaves;
    private String employeeId;
    private int jobLevel;
    private String password;
    private String employeeName;
    private String managerId;



    public Employee(
        String leavesTaken,        int noOfLeaves,        String employeeId,        int jobLevel,        String password,        String employeeName,        String managerId    ) {
        this.leavesTaken = leavesTaken;
        this.noOfLeaves = noOfLeaves;
        this.employeeId = employeeId;
        this.jobLevel = jobLevel;
        this.password = password;
        this.employeeName = employeeName;
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
    public String getManagerid() {
        return managerId;
    }

    public void setManagerid(String managerId) {
        this.managerId = managerId;
    }


}