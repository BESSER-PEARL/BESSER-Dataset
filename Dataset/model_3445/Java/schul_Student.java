





import java.util.List;
import java.util.ArrayList;

public class schul_Student  {

    private String name;





    private schul_Student schul_student;




    private schul_Classroom schul_classroom;


    public schul_Student(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public schul_Student getSchul_student() {
        return schul_student;
    }

    public void setSchul_student(schul_Student schul_student) {
        this.schul_student = schul_student;
    }
    public schul_Classroom getSchul_classroom() {
        return schul_classroom;
    }

    public void setSchul_classroom(schul_Classroom schul_classroom) {
        this.schul_classroom = schul_classroom;
    }

}