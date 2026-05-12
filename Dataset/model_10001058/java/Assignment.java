





import java.util.List;
import java.util.ArrayList;

public class Assignment  {

    private int duedate;
    private int session;
    private String section;
    private String program;
    private String department;
    private String assignmentfile;
    private String _attr;
    private String assignmenttitle;
    private int class;
    private int _attr1;





    private List<student> students;


    public Assignment(
        int duedate,        int session,        String section,        String program,        String department,        String assignmentfile,        String _attr,        String assignmenttitle,        int class,        int _attr1    ) {
        this.duedate = duedate;
        this.session = session;
        this.section = section;
        this.program = program;
        this.department = department;
        this.assignmentfile = assignmentfile;
        this._attr = _attr;
        this.assignmenttitle = assignmenttitle;
        this.class = class;
        this._attr1 = _attr1;
        this.students = new ArrayList<>();
    }

    public Assignment(
        int duedate,        int session,        String section,        String program,        String department,        String assignmentfile,        String _attr,        String assignmenttitle,        int class,        int _attr1        ArrayList<student> students    ) {
        this.duedate = duedate;
        this.session = session;
        this.section = section;
        this.program = program;
        this.department = department;
        this.assignmentfile = assignmentfile;
        this._attr = _attr;
        this.assignmenttitle = assignmenttitle;
        this.class = class;
        this._attr1 = _attr1;
        this.students = students;
    }

    public int getDuedate() {
        return duedate;
    }

    public void setDuedate(int duedate) {
        this.duedate = duedate;
    }
    public int getSession() {
        return session;
    }

    public void setSession(int session) {
        this.session = session;
    }
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }
    public String getProgram() {
        return program;
    }

    public void setProgram(String program) {
        this.program = program;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public String getAssignmentfile() {
        return assignmentfile;
    }

    public void setAssignmentfile(String assignmentfile) {
        this.assignmentfile = assignmentfile;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public String getAssignmenttitle() {
        return assignmenttitle;
    }

    public void setAssignmenttitle(String assignmenttitle) {
        this.assignmenttitle = assignmenttitle;
    }
    public int getClass() {
        return class;
    }

    public void setClass(int class) {
        this.class = class;
    }
    public int get_attr1() {
        return _attr1;
    }

    public void set_attr1(int _attr1) {
        this._attr1 = _attr1;
    }

    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}