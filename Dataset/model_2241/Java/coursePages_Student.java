





import java.util.List;
import java.util.ArrayList;

public class coursePages_Student extends Person {

    private String studentID;



    public coursePages_Student(
        String studentID    ) {
        super(
        );
        this.studentID = studentID;
    }


    public String getStudentid() {
        return studentID;
    }

    public void setStudentid(String studentID) {
        this.studentID = studentID;
    }


}