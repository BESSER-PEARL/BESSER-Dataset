





import java.util.List;
import java.util.ArrayList;

public class Show_all_grades  {

    private String Course_name;
    private int Student_ID;
    private String First_Name;
    private String Last_Name;
    private String Teacher;
    private String Grade_earned;





    private Home_page home_page;


    public Show_all_grades(
        String Course_name,        int Student_ID,        String First_Name,        String Last_Name,        String Teacher,        String Grade_earned    ) {
        this.Course_name = Course_name;
        this.Student_ID = Student_ID;
        this.First_Name = First_Name;
        this.Last_Name = Last_Name;
        this.Teacher = Teacher;
        this.Grade_earned = Grade_earned;
    }


    public String getCourse_name() {
        return Course_name;
    }

    public void setCourse_name(String Course_name) {
        this.Course_name = Course_name;
    }
    public int getStudent_id() {
        return Student_ID;
    }

    public void setStudent_id(int Student_ID) {
        this.Student_ID = Student_ID;
    }
    public String getFirst_name() {
        return First_Name;
    }

    public void setFirst_name(String First_Name) {
        this.First_Name = First_Name;
    }
    public String getLast_name() {
        return Last_Name;
    }

    public void setLast_name(String Last_Name) {
        this.Last_Name = Last_Name;
    }
    public String getTeacher() {
        return Teacher;
    }

    public void setTeacher(String Teacher) {
        this.Teacher = Teacher;
    }
    public String getGrade_earned() {
        return Grade_earned;
    }

    public void setGrade_earned(String Grade_earned) {
        this.Grade_earned = Grade_earned;
    }

    public Home_page getHome_page() {
        return home_page;
    }

    public void setHome_page(Home_page home_page) {
        this.home_page = home_page;
    }

}