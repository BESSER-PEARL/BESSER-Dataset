





import java.util.List;
import java.util.ArrayList;

public class dropbox  {

    private int date;
    private int session;
    private String program;
    private String file;
    private String section;
    private int class;
    private String department;
    private String filetype;
    private String _attr;
    private int _attr1;





    private List<student> students;


    public dropbox(
        int date,        int session,        String program,        String file,        String section,        int class,        String department,        String filetype,        String _attr,        int _attr1    ) {
        this.date = date;
        this.session = session;
        this.program = program;
        this.file = file;
        this.section = section;
        this.class = class;
        this.department = department;
        this.filetype = filetype;
        this._attr = _attr;
        this._attr1 = _attr1;
        this.students = new ArrayList<>();
    }

    public dropbox(
        int date,        int session,        String program,        String file,        String section,        int class,        String department,        String filetype,        String _attr,        int _attr1        ArrayList<student> students    ) {
        this.date = date;
        this.session = session;
        this.program = program;
        this.file = file;
        this.section = section;
        this.class = class;
        this.department = department;
        this.filetype = filetype;
        this._attr = _attr;
        this._attr1 = _attr1;
        this.students = students;
    }

    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
    public int getSession() {
        return session;
    }

    public void setSession(int session) {
        this.session = session;
    }
    public String getProgram() {
        return program;
    }

    public void setProgram(String program) {
        this.program = program;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }
    public int getClass() {
        return class;
    }

    public void setClass(int class) {
        this.class = class;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public String getFiletype() {
        return filetype;
    }

    public void setFiletype(String filetype) {
        this.filetype = filetype;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
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