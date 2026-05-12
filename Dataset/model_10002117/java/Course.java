





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String Time;
    private String Day;
    private int Room;
    private String Course_name;
    private String Teacher;
    private int Course_Index;
    private int Student_ID;
    private String Status;
    private String Grade_earned;



    public Course(
        String Time,        String Day,        int Room,        String Course_name,        String Teacher,        int Course_Index,        int Student_ID,        String Status,        String Grade_earned    ) {
        this.Time = Time;
        this.Day = Day;
        this.Room = Room;
        this.Course_name = Course_name;
        this.Teacher = Teacher;
        this.Course_Index = Course_Index;
        this.Student_ID = Student_ID;
        this.Status = Status;
        this.Grade_earned = Grade_earned;
    }


    public String getTime() {
        return Time;
    }

    public void setTime(String Time) {
        this.Time = Time;
    }
    public String getDay() {
        return Day;
    }

    public void setDay(String Day) {
        this.Day = Day;
    }
    public int getRoom() {
        return Room;
    }

    public void setRoom(int Room) {
        this.Room = Room;
    }
    public String getCourse_name() {
        return Course_name;
    }

    public void setCourse_name(String Course_name) {
        this.Course_name = Course_name;
    }
    public String getTeacher() {
        return Teacher;
    }

    public void setTeacher(String Teacher) {
        this.Teacher = Teacher;
    }
    public int getCourse_index() {
        return Course_Index;
    }

    public void setCourse_index(int Course_Index) {
        this.Course_Index = Course_Index;
    }
    public int getStudent_id() {
        return Student_ID;
    }

    public void setStudent_id(int Student_ID) {
        this.Student_ID = Student_ID;
    }
    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public String getGrade_earned() {
        return Grade_earned;
    }

    public void setGrade_earned(String Grade_earned) {
        this.Grade_earned = Grade_earned;
    }


}