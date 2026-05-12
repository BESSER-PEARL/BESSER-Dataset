





import java.util.List;
import java.util.ArrayList;

public class Package2_Employee  {

    private String id;
    private String shift;
    private String post;
    private int usergroup;
    private int leavegroup;
    private int depid;
    private String empid;





    private List<Package2_Attendance> package2_attendances;




    private Package2_Shifts package2_shifts;




    private Package2_Departments package2_departments;




    private Package2_Posts package2_posts;




    private Package2_Allowance package2_allowance;


    public Package2_Employee(
        String id,        String shift,        String post,        int usergroup,        int leavegroup,        int depid,        String empid    ) {
        this.id = id;
        this.shift = shift;
        this.post = post;
        this.usergroup = usergroup;
        this.leavegroup = leavegroup;
        this.depid = depid;
        this.empid = empid;
        this.package2_attendances = new ArrayList<>();
    }

    public Package2_Employee(
        String id,        String shift,        String post,        int usergroup,        int leavegroup,        int depid,        String empid        ArrayList<Package2_Attendance> package2_attendances    ) {
        this.id = id;
        this.shift = shift;
        this.post = post;
        this.usergroup = usergroup;
        this.leavegroup = leavegroup;
        this.depid = depid;
        this.empid = empid;
        this.package2_attendances = package2_attendances;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getShift() {
        return shift;
    }

    public void setShift(String shift) {
        this.shift = shift;
    }
    public String getPost() {
        return post;
    }

    public void setPost(String post) {
        this.post = post;
    }
    public int getUsergroup() {
        return usergroup;
    }

    public void setUsergroup(int usergroup) {
        this.usergroup = usergroup;
    }
    public int getLeavegroup() {
        return leavegroup;
    }

    public void setLeavegroup(int leavegroup) {
        this.leavegroup = leavegroup;
    }
    public int getDepid() {
        return depid;
    }

    public void setDepid(int depid) {
        this.depid = depid;
    }
    public String getEmpid() {
        return empid;
    }

    public void setEmpid(String empid) {
        this.empid = empid;
    }

    public List<Package2_Attendance> getPackage2_attendances() {
        return package2_attendances;
    }

    public void addPackage2_attendance(Package2_attendance package2_attendance) {
        this.package2_attendances.add(package2_attendance);
    }
    public Package2_Shifts getPackage2_shifts() {
        return package2_shifts;
    }

    public void setPackage2_shifts(Package2_Shifts package2_shifts) {
        this.package2_shifts = package2_shifts;
    }
    public Package2_Departments getPackage2_departments() {
        return package2_departments;
    }

    public void setPackage2_departments(Package2_Departments package2_departments) {
        this.package2_departments = package2_departments;
    }
    public Package2_Posts getPackage2_posts() {
        return package2_posts;
    }

    public void setPackage2_posts(Package2_Posts package2_posts) {
        this.package2_posts = package2_posts;
    }
    public Package2_Allowance getPackage2_allowance() {
        return package2_allowance;
    }

    public void setPackage2_allowance(Package2_Allowance package2_allowance) {
        this.package2_allowance = package2_allowance;
    }

}