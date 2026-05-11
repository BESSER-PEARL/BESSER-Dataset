





import java.util.List;
import java.util.ArrayList;

public class schol_Student  {

    private String name;





    private List<schol_Student> schol_students;




    private schol_Classroom schol_classroom;


    public schol_Student(
        String name    ) {
        this.name = name;
        this.schol_students = new ArrayList<>();
    }

    public schol_Student(
        String name        ArrayList<schol_Student> schol_students    ) {
        this.name = name;
        this.schol_students = schol_students;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<schol_Student> getSchol_students() {
        return schol_students;
    }

    public void addSchol_student(Schol_student schol_student) {
        this.schol_students.add(schol_student);
    }
    public schol_Classroom getSchol_classroom() {
        return schol_classroom;
    }

    public void setSchol_classroom(schol_Classroom schol_classroom) {
        this.schol_classroom = schol_classroom;
    }

}