





import java.util.List;
import java.util.ArrayList;

public class Faculty  {

    private String mail_ID;
    private String name;
    private String emp_ID;





    private List<Student> students;


    public Faculty(
        String mail_ID,        String name,        String emp_ID    ) {
        this.mail_ID = mail_ID;
        this.name = name;
        this.emp_ID = emp_ID;
        this.students = new ArrayList<>();
    }

    public Faculty(
        String mail_ID,        String name,        String emp_ID        ArrayList<Student> students    ) {
        this.mail_ID = mail_ID;
        this.name = name;
        this.emp_ID = emp_ID;
        this.students = students;
    }

    public String getMail_id() {
        return mail_ID;
    }

    public void setMail_id(String mail_ID) {
        this.mail_ID = mail_ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmp_id() {
        return emp_ID;
    }

    public void setEmp_id(String emp_ID) {
        this.emp_ID = emp_ID;
    }

    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}