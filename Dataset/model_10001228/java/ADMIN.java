





import java.util.List;
import java.util.ArrayList;

public class ADMIN  {

    private String id;
    private String password;





    private List<STUDENT> students;




    private List<PARENT> parents;




    private List<FACULTY> facultys;


    public ADMIN(
        String id,        String password    ) {
        this.id = id;
        this.password = password;
        this.students = new ArrayList<>();
        this.parents = new ArrayList<>();
        this.facultys = new ArrayList<>();
    }

    public ADMIN(
        String id,        String password        ArrayList<STUDENT> students,        ArrayList<PARENT> parents,        ArrayList<FACULTY> facultys    ) {
        this.id = id;
        this.password = password;
        this.students = students;
        this.parents = parents;
        this.facultys = facultys;
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
    public List<FACULTY> getFacultys() {
        return facultys;
    }

    public void addFaculty(Faculty faculty) {
        this.facultys.add(faculty);
    }

}