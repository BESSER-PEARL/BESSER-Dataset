





import java.util.List;
import java.util.ArrayList;

public class mypackage_Student  {

    private String grade;
    private int level;
    private String studentFileName;



    public mypackage_Student(
        String grade,        int level,        String studentFileName    ) {
        this.grade = grade;
        this.level = level;
        this.studentFileName = studentFileName;
    }


    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public String getStudentfilename() {
        return studentFileName;
    }

    public void setStudentfilename(String studentFileName) {
        this.studentFileName = studentFileName;
    }


}