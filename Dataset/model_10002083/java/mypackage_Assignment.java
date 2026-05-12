





import java.util.List;
import java.util.ArrayList;

public class mypackage_Assignment  {

    private int number;
    private String Deadline;
    private String StrartDate;





    private mypackage_Student mypackage_student;




    private mypackage_Course mypackage_course;




    private mypackage_Tutor mypackage_tutor;


    public mypackage_Assignment(
        int number,        String Deadline,        String StrartDate    ) {
        this.number = number;
        this.Deadline = Deadline;
        this.StrartDate = StrartDate;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getDeadline() {
        return Deadline;
    }

    public void setDeadline(String Deadline) {
        this.Deadline = Deadline;
    }
    public String getStrartdate() {
        return StrartDate;
    }

    public void setStrartdate(String StrartDate) {
        this.StrartDate = StrartDate;
    }

    public mypackage_Student getMypackage_student() {
        return mypackage_student;
    }

    public void setMypackage_student(mypackage_Student mypackage_student) {
        this.mypackage_student = mypackage_student;
    }
    public mypackage_Course getMypackage_course() {
        return mypackage_course;
    }

    public void setMypackage_course(mypackage_Course mypackage_course) {
        this.mypackage_course = mypackage_course;
    }
    public mypackage_Tutor getMypackage_tutor() {
        return mypackage_tutor;
    }

    public void setMypackage_tutor(mypackage_Tutor mypackage_tutor) {
        this.mypackage_tutor = mypackage_tutor;
    }

}