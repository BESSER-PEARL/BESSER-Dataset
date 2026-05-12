





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String leavesTaken;
    private int noOfLeaves;
    private String password;
    private int jobLevel;
    private String employeeId;
    private String managerId;
    private String employeeName;



    public Employee(
        String leavesTaken,        int noOfLeaves,        String password,        int jobLevel,        String employeeId,        String managerId,        String employeeName    ) {
        this.leavesTaken = leavesTaken;
        this.noOfLeaves = noOfLeaves;
        this.password = password;
        this.jobLevel = jobLevel;
        this.employeeId = employeeId;
        this.managerId = managerId;
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
    public String getManagerid() {
        return managerId;
    }

    public void setManagerid(String managerId) {
        this.managerId = managerId;
    }
    public String getEmployeename() {
        return employeeName;
    }

    public void setEmployeename(String employeeName) {
        this.employeeName = employeeName;
    }


}