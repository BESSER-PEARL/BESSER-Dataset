





import java.util.List;
import java.util.ArrayList;

public class classmate_Classroom  {

    private String name;





    private List<classmate_Student> classmate_students;




    private classmate_School classmate_school;


    public classmate_Classroom(
        String name    ) {
        this.name = name;
        this.classmate_students = new ArrayList<>();
    }

    public classmate_Classroom(
        String name        ArrayList<classmate_Student> classmate_students    ) {
        this.name = name;
        this.classmate_students = classmate_students;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<classmate_Student> getClassmate_students() {
        return classmate_students;
    }

    public void addClassmate_student(Classmate_student classmate_student) {
        this.classmate_students.add(classmate_student);
    }
    public classmate_School getClassmate_school() {
        return classmate_school;
    }

    public void setClassmate_school(classmate_School classmate_school) {
        this.classmate_school = classmate_school;
    }

}