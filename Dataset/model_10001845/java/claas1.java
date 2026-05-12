





import java.util.List;
import java.util.ArrayList;

public class claas1  {

    private String name;
    private int id;





    private List<student> students;




    private teachers teachers;


    public claas1(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
        this.students = new ArrayList<>();
    }

    public claas1(
        String name,        int id        ArrayList<student> students    ) {
        this.name = name;
        this.id = id;
        this.students = students;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }
    public teachers getTeachers() {
        return teachers;
    }

    public void setTeachers(teachers teachers) {
        this.teachers = teachers;
    }

}