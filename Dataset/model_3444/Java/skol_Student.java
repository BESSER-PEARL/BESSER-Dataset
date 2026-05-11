





import java.util.List;
import java.util.ArrayList;

public class skol_Student  {

    private String name;





    private skol_Classroom skol_classroom;




    private skol_Student skol_student;


    public skol_Student(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public skol_Classroom getSkol_classroom() {
        return skol_classroom;
    }

    public void setSkol_classroom(skol_Classroom skol_classroom) {
        this.skol_classroom = skol_classroom;
    }
    public skol_Student getSkol_student() {
        return skol_student;
    }

    public void setSkol_student(skol_Student skol_student) {
        this.skol_student = skol_student;
    }

}