





import java.util.List;
import java.util.ArrayList;

public class myDsl_Teacher extends Person {






    private myDsl_Student mydsl_student;


    public myDsl_Teacher(
    ) {
        super(
        );
    }



    public myDsl_Student getMydsl_student() {
        return mydsl_student;
    }

    public void setMydsl_student(myDsl_Student mydsl_student) {
        this.mydsl_student = mydsl_student;
    }

}