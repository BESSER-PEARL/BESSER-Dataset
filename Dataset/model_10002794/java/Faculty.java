





import java.util.List;
import java.util.ArrayList;

public class Faculty  {

    private String name;
    private String mail_ID;
    private String emp_ID;





    private List<Student> students;


    public Faculty(
        String name,        String mail_ID,        String emp_ID    ) {
        this.name = name;
        this.mail_ID = mail_ID;
        this.emp_ID = emp_ID;
        this.students = new ArrayList<>();
    }

    public Faculty(
        String name,        String mail_ID,        String emp_ID        ArrayList<Student> students    ) {
        this.name = name;
        this.mail_ID = mail_ID;
        this.emp_ID = emp_ID;
        this.students = students;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMail_id() {
        return mail_ID;
    }

    public void setMail_id(String mail_ID) {
        this.mail_ID = mail_ID;
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