





import java.util.List;
import java.util.ArrayList;

public class barcode  {






    private List<student> students;


    public barcode(
    ) {
        this.students = new ArrayList<>();
    }

    public barcode(
        ArrayList<student> students    ) {
        this.students = students;
    }


    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}