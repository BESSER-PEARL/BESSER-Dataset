





import java.util.List;
import java.util.ArrayList;

public class mypackage_Student  {

    private int level;
    private String grade;
    private String studentFileName;



    public mypackage_Student(
        int level,        String grade,        String studentFileName    ) {
        this.level = level;
        this.grade = grade;
        this.studentFileName = studentFileName;
    }


    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }
    public String getStudentfilename() {
        return studentFileName;
    }

    public void setStudentfilename(String studentFileName) {
        this.studentFileName = studentFileName;
    }


}