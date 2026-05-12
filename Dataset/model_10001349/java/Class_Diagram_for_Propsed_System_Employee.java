





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Employee  {

    private int leavegroup;
    private String post;
    private int usergroup;
    private String empid;
    private String id;
    private int user_id;
    private int mobile;
    private String shift;
    private int depid;





    private Class_Diagram_for_Propsed_System_Shifts class_diagram_for_propsed_system_shifts;




    private Class_Diagram_for_Propsed_System_Posts class_diagram_for_propsed_system_posts;




    private Class_Diagram_for_Propsed_System_Allowance class_diagram_for_propsed_system_allowance;




    private List<Class_Diagram_for_Propsed_System_Attendance> class_diagram_for_propsed_system_attendances;




    private List<Class_Diagram_for_Propsed_System_Deductions> class_diagram_for_propsed_system_deductionss;




    private Class_Diagram_for_Propsed_System_Departments class_diagram_for_propsed_system_departments;


    public Class_Diagram_for_Propsed_System_Employee(
        int leavegroup,        String post,        int usergroup,        String empid,        String id,        int user_id,        int mobile,        String shift,        int depid    ) {
        this.leavegroup = leavegroup;
        this.post = post;
        this.usergroup = usergroup;
        this.empid = empid;
        this.id = id;
        this.user_id = user_id;
        this.mobile = mobile;
        this.shift = shift;
        this.depid = depid;
        this.class_diagram_for_propsed_system_attendances = new ArrayList<>();
        this.class_diagram_for_propsed_system_deductionss = new ArrayList<>();
    }

    public Class_Diagram_for_Propsed_System_Employee(
        int leavegroup,        String post,        int usergroup,        String empid,        String id,        int user_id,        int mobile,        String shift,        int depid        ArrayList<Class_Diagram_for_Propsed_System_Attendance> class_diagram_for_propsed_system_attendances,        ArrayList<Class_Diagram_for_Propsed_System_Deductions> class_diagram_for_propsed_system_deductionss    ) {
        this.leavegroup = leavegroup;
        this.post = post;
        this.usergroup = usergroup;
        this.empid = empid;
        this.id = id;
        this.user_id = user_id;
        this.mobile = mobile;
        this.shift = shift;
        this.depid = depid;
        this.class_diagram_for_propsed_system_attendances = class_diagram_for_propsed_system_attendances;
        this.class_diagram_for_propsed_system_deductionss = class_diagram_for_propsed_system_deductionss;
    }

    public int getLeavegroup() {
        return leavegroup;
    }

    public void setLeavegroup(int leavegroup) {
        this.leavegroup = leavegroup;
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
    public String getEmpid() {
        return empid;
    }

    public void setEmpid(String empid) {
        this.empid = empid;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public int getMobile() {
        return mobile;
    }

    public void setMobile(int mobile) {
        this.mobile = mobile;
    }
    public String getShift() {
        return shift;
    }

    public void setShift(String shift) {
        this.shift = shift;
    }
    public int getDepid() {
        return depid;
    }

    public void setDepid(int depid) {
        this.depid = depid;
    }

    public Class_Diagram_for_Propsed_System_Shifts getClass_diagram_for_propsed_system_shifts() {
        return class_diagram_for_propsed_system_shifts;
    }

    public void setClass_diagram_for_propsed_system_shifts(Class_Diagram_for_Propsed_System_Shifts class_diagram_for_propsed_system_shifts) {
        this.class_diagram_for_propsed_system_shifts = class_diagram_for_propsed_system_shifts;
    }
    public Class_Diagram_for_Propsed_System_Posts getClass_diagram_for_propsed_system_posts() {
        return class_diagram_for_propsed_system_posts;
    }

    public void setClass_diagram_for_propsed_system_posts(Class_Diagram_for_Propsed_System_Posts class_diagram_for_propsed_system_posts) {
        this.class_diagram_for_propsed_system_posts = class_diagram_for_propsed_system_posts;
    }
    public Class_Diagram_for_Propsed_System_Allowance getClass_diagram_for_propsed_system_allowance() {
        return class_diagram_for_propsed_system_allowance;
    }

    public void setClass_diagram_for_propsed_system_allowance(Class_Diagram_for_Propsed_System_Allowance class_diagram_for_propsed_system_allowance) {
        this.class_diagram_for_propsed_system_allowance = class_diagram_for_propsed_system_allowance;
    }
    public List<Class_Diagram_for_Propsed_System_Attendance> getClass_diagram_for_propsed_system_attendances() {
        return class_diagram_for_propsed_system_attendances;
    }

    public void addClass_diagram_for_propsed_system_attendance(Class_diagram_for_propsed_system_attendance class_diagram_for_propsed_system_attendance) {
        this.class_diagram_for_propsed_system_attendances.add(class_diagram_for_propsed_system_attendance);
    }
    public List<Class_Diagram_for_Propsed_System_Deductions> getClass_diagram_for_propsed_system_deductionss() {
        return class_diagram_for_propsed_system_deductionss;
    }

    public void addClass_diagram_for_propsed_system_deductions(Class_diagram_for_propsed_system_deductions class_diagram_for_propsed_system_deductions) {
        this.class_diagram_for_propsed_system_deductionss.add(class_diagram_for_propsed_system_deductions);
    }
    public Class_Diagram_for_Propsed_System_Departments getClass_diagram_for_propsed_system_departments() {
        return class_diagram_for_propsed_system_departments;
    }

    public void setClass_diagram_for_propsed_system_departments(Class_Diagram_for_Propsed_System_Departments class_diagram_for_propsed_system_departments) {
        this.class_diagram_for_propsed_system_departments = class_diagram_for_propsed_system_departments;
    }

}