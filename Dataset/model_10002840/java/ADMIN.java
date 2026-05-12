





import java.util.List;
import java.util.ArrayList;

public class ADMIN  {

    private String password;
    private String id;





    private List<STUDENT> students;




    private List<FACULTY> facultys;


    public ADMIN(
        String password,        String id    ) {
        this.password = password;
        this.id = id;
        this.students = new ArrayList<>();
        this.facultys = new ArrayList<>();
    }

    public ADMIN(
        String password,        String id        ArrayList<STUDENT> students,        ArrayList<FACULTY> facultys    ) {
        this.password = password;
        this.id = id;
        this.students = students;
        this.facultys = facultys;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<STUDENT> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }
    public List<FACULTY> getFacultys() {
        return facultys;
    }

    public void addFaculty(Faculty faculty) {
        this.facultys.add(faculty);
    }

}