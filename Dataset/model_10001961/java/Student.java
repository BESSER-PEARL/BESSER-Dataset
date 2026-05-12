





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private int studentRate;
    private String student_name;
    private int phone;
    private int student_ID;



    public Student(
        int studentRate,        String student_name,        int phone,        int student_ID    ) {
        this.studentRate = studentRate;
        this.student_name = student_name;
        this.phone = phone;
        this.student_ID = student_ID;
    }


    public int getStudentrate() {
        return studentRate;
    }

    public void setStudentrate(int studentRate) {
        this.studentRate = studentRate;
    }
    public String getStudent_name() {
        return student_name;
    }

    public void setStudent_name(String student_name) {
        this.student_name = student_name;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public int getStudent_id() {
        return student_ID;
    }

    public void setStudent_id(int student_ID) {
        this.student_ID = student_ID;
    }


}