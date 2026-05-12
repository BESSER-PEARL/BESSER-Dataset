





import java.util.List;
import java.util.ArrayList;

public class Quiz  {

    private String quiztitle;
    private String department;
    private String quizfile;
    private int date;
    private String _attr;
    private String subject;
    private int timeduration;
    private int scale;





    private List<student> students;


    public Quiz(
        String quiztitle,        String department,        String quizfile,        int date,        String _attr,        String subject,        int timeduration,        int scale    ) {
        this.quiztitle = quiztitle;
        this.department = department;
        this.quizfile = quizfile;
        this.date = date;
        this._attr = _attr;
        this.subject = subject;
        this.timeduration = timeduration;
        this.scale = scale;
        this.students = new ArrayList<>();
    }

    public Quiz(
        String quiztitle,        String department,        String quizfile,        int date,        String _attr,        String subject,        int timeduration,        int scale        ArrayList<student> students    ) {
        this.quiztitle = quiztitle;
        this.department = department;
        this.quizfile = quizfile;
        this.date = date;
        this._attr = _attr;
        this.subject = subject;
        this.timeduration = timeduration;
        this.scale = scale;
        this.students = students;
    }

    public String getQuiztitle() {
        return quiztitle;
    }

    public void setQuiztitle(String quiztitle) {
        this.quiztitle = quiztitle;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public String getQuizfile() {
        return quizfile;
    }

    public void setQuizfile(String quizfile) {
        this.quizfile = quizfile;
    }
    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public int getTimeduration() {
        return timeduration;
    }

    public void setTimeduration(int timeduration) {
        this.timeduration = timeduration;
    }
    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }

    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}