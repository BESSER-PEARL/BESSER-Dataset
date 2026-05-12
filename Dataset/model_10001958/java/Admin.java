





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String mail_ID;
    private String name;





    private List<Student> students;




    private List<Faculty> facultys;


    public Admin(
        String mail_ID,        String name    ) {
        this.mail_ID = mail_ID;
        this.name = name;
        this.students = new ArrayList<>();
        this.facultys = new ArrayList<>();
    }

    public Admin(
        String mail_ID,        String name        ArrayList<Student> students,        ArrayList<Faculty> facultys    ) {
        this.mail_ID = mail_ID;
        this.name = name;
        this.students = students;
        this.facultys = facultys;
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

    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }
    public List<Faculty> getFacultys() {
        return facultys;
    }

    public void addFaculty(Faculty faculty) {
        this.facultys.add(faculty);
    }

}