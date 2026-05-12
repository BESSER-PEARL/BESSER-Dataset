





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String leavesTaken;
    private int noOfLeaves;
    private String password;
    private String managerId;
    private String employeeName;
    private int jobLevel;
    private String employeeId;



    public Employee(
        String leavesTaken,        int noOfLeaves,        String password,        String managerId,        String employeeName,        int jobLevel,        String employeeId    ) {
        this.leavesTaken = leavesTaken;
        this.noOfLeaves = noOfLeaves;
        this.password = password;
        this.managerId = managerId;
        this.employeeName = employeeName;
        this.jobLevel = jobLevel;
        this.employeeId = employeeId;
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


}