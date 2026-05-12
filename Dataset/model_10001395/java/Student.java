





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private int s_age;
    private String grade;
    private String studentfname;





    private FileBinary filebinary;


    public Student(
        int s_age,        String grade,        String studentfname    ) {
        this.s_age = s_age;
        this.grade = grade;
        this.studentfname = studentfname;
    }


    public int getS_age() {
        return s_age;
    }

    public void setS_age(int s_age) {
        this.s_age = s_age;
    }
    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }
    public String getStudentfname() {
        return studentfname;
    }

    public void setStudentfname(String studentfname) {
        this.studentfname = studentfname;
    }

    public FileBinary getFilebinary() {
        return filebinary;
    }

    public void setFilebinary(FileBinary filebinary) {
        this.filebinary = filebinary;
    }

}