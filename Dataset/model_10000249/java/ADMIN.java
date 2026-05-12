





import java.util.List;
import java.util.ArrayList;

public class ADMIN  {

    private String id;
    private String password;





    private List<FACULTY> facultys;




    private List<STUDENT> students;


    public ADMIN(
        String id,        String password    ) {
        this.id = id;
        this.password = password;
        this.facultys = new ArrayList<>();
        this.students = new ArrayList<>();
    }

    public ADMIN(
        String id,        String password        ArrayList<FACULTY> facultys,        ArrayList<STUDENT> students    ) {
        this.id = id;
        this.password = password;
        this.facultys = facultys;
        this.students = students;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public List<FACULTY> getFacultys() {
        return facultys;
    }

    public void addFaculty(Faculty faculty) {
        this.facultys.add(faculty);
    }
    public List<STUDENT> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}