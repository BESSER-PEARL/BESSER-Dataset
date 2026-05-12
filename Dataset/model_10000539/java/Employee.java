





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String password;
    private int jobLevel;
    private String employeeId;
    private String employeeName;
    private String leavesTaken;
    private int noOfLeaves;
    private String managerId;



    public Employee(
        String password,        int jobLevel,        String employeeId,        String employeeName,        String leavesTaken,        int noOfLeaves,        String managerId    ) {
        this.password = password;
        this.jobLevel = jobLevel;
        this.employeeId = employeeId;
        this.employeeName = employeeName;
        this.leavesTaken = leavesTaken;
        this.noOfLeaves = noOfLeaves;
        this.managerId = managerId;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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
    public String getManagerid() {
        return managerId;
    }

    public void setManagerid(String managerId) {
        this.managerId = managerId;
    }


}