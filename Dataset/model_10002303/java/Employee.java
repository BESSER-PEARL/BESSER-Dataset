





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String leavesTaken;
    private String managerId;
    private int noOfLeaves;
    private String employeeId;
    private int jobLevel;
    private String password;
    private String employeeName;



    public Employee(
        String leavesTaken,        String managerId,        int noOfLeaves,        String employeeId,        int jobLevel,        String password,        String employeeName    ) {
        this.leavesTaken = leavesTaken;
        this.managerId = managerId;
        this.noOfLeaves = noOfLeaves;
        this.employeeId = employeeId;
        this.jobLevel = jobLevel;
        this.password = password;
        this.employeeName = employeeName;
    }


    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
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


}