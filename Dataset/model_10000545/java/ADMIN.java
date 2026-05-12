





import java.util.List;
import java.util.ArrayList;

public class ADMIN  {

    private String password;
    private String id;





    private List<FACULTY> facultys;




    private List<STUDENT> students;




    private List<PARENT> parents;


    public ADMIN(
        String password,        String id    ) {
        this.password = password;
        this.id = id;
        this.facultys = new ArrayList<>();
        this.students = new ArrayList<>();
        this.parents = new ArrayList<>();
    }

    public ADMIN(
        String password,        String id        ArrayList<FACULTY> facultys,        ArrayList<STUDENT> students,        ArrayList<PARENT> parents    ) {
        this.password = password;
        this.id = id;
        this.facultys = facultys;
        this.students = students;
        this.parents = parents;
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
    public List<PARENT> getParents() {
        return parents;
    }

    public void addParent(Parent parent) {
        this.parents.add(parent);
    }

}