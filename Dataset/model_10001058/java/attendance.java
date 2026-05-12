





import java.util.List;
import java.util.ArrayList;

public class attendance  {

    private String day;
    private String absent;
    private String present;
    private String attribute;
    private int lecture;
    private String _attr;
    private String class;
    private int date;
    private String class1;
    private String leave;





    private student student;


    public attendance(
        String day,        String absent,        String present,        String attribute,        int lecture,        String _attr,        String class,        int date,        String class1,        String leave    ) {
        this.day = day;
        this.absent = absent;
        this.present = present;
        this.attribute = attribute;
        this.lecture = lecture;
        this._attr = _attr;
        this.class = class;
        this.date = date;
        this.class1 = class1;
        this.leave = leave;
    }


    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public String getAbsent() {
        return absent;
    }

    public void setAbsent(String absent) {
        this.absent = absent;
    }
    public String getPresent() {
        return present;
    }

    public void setPresent(String present) {
        this.present = present;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getLecture() {
        return lecture;
    }

    public void setLecture(int lecture) {
        this.lecture = lecture;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public String getClass() {
        return class;
    }

    public void setClass(String class) {
        this.class = class;
    }
    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
    public String getClass1() {
        return class1;
    }

    public void setClass1(String class1) {
        this.class1 = class1;
    }
    public String getLeave() {
        return leave;
    }

    public void setLeave(String leave) {
        this.leave = leave;
    }

    public student getStudent() {
        return student;
    }

    public void setStudent(student student) {
        this.student = student;
    }

}