





import java.util.List;
import java.util.ArrayList;

public class Exam  {

    private String ETime;
    private String EName;
    private String MaxGrade;





    private Course course;




    private Binary_File binary_file;


    public Exam(
        String ETime,        String EName,        String MaxGrade    ) {
        this.ETime = ETime;
        this.EName = EName;
        this.MaxGrade = MaxGrade;
    }


    public String getEtime() {
        return ETime;
    }

    public void setEtime(String ETime) {
        this.ETime = ETime;
    }
    public String getEname() {
        return EName;
    }

    public void setEname(String EName) {
        this.EName = EName;
    }
    public String getMaxgrade() {
        return MaxGrade;
    }

    public void setMaxgrade(String MaxGrade) {
        this.MaxGrade = MaxGrade;
    }

    public Course getCourse() {
        return course;
    }

    public void setCourse(Course course) {
        this.course = course;
    }
    public Binary_File getBinary_file() {
        return binary_file;
    }

    public void setBinary_file(Binary_File binary_file) {
        this.binary_file = binary_file;
    }

}