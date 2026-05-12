





import java.util.List;
import java.util.ArrayList;

public class ADMIN  {

    private String id;
    private String password;





    private List<STUDENT> students;




    private List<FACULTY> facultys;




    private List<PARENT> parents;


    public ADMIN(
        String id,        String password    ) {
        this.id = id;
        this.password = password;
        this.students = new ArrayList<>();
        this.facultys = new ArrayList<>();
        this.parents = new ArrayList<>();
    }

    public ADMIN(
        String id,        String password        ArrayList<STUDENT> students,        ArrayList<FACULTY> facultys,        ArrayList<PARENT> parents    ) {
        this.id = id;
        this.password = password;
        this.students = students;
        this.facultys = facultys;
        this.parents = parents;
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
    public List<FACULTY> getFacultys() {
        return facultys;
    }

    public void addFaculty(Faculty faculty) {
        this.facultys.add(faculty);
    }
    public List<PARENT> getParents() {
        return parents;
    }

    public void addParent(Parent parent) {
        this.parents.add(parent);
    }

}