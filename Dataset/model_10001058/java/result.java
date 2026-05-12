





import java.util.List;
import java.util.ArrayList;

public class result  {

    private String subject;
    private int totalmarks;
    private String class;
    private String class1;
    private int midmarks;
    private int finalmarks;
    private int sessional;
    private int obtainedmarks;
    private String attribute;
    private String _attr;
    private int practical;





    private student student;


    public result(
        String subject,        int totalmarks,        String class,        String class1,        int midmarks,        int finalmarks,        int sessional,        int obtainedmarks,        String attribute,        String _attr,        int practical    ) {
        this.subject = subject;
        this.totalmarks = totalmarks;
        this.class = class;
        this.class1 = class1;
        this.midmarks = midmarks;
        this.finalmarks = finalmarks;
        this.sessional = sessional;
        this.obtainedmarks = obtainedmarks;
        this.attribute = attribute;
        this._attr = _attr;
        this.practical = practical;
    }


    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public int getTotalmarks() {
        return totalmarks;
    }

    public void setTotalmarks(int totalmarks) {
        this.totalmarks = totalmarks;
    }
    public String getClass() {
        return class;
    }

    public void setClass(String class) {
        this.class = class;
    }
    public String getClass1() {
        return class1;
    }

    public void setClass1(String class1) {
        this.class1 = class1;
    }
    public int getMidmarks() {
        return midmarks;
    }

    public void setMidmarks(int midmarks) {
        this.midmarks = midmarks;
    }
    public int getFinalmarks() {
        return finalmarks;
    }

    public void setFinalmarks(int finalmarks) {
        this.finalmarks = finalmarks;
    }
    public int getSessional() {
        return sessional;
    }

    public void setSessional(int sessional) {
        this.sessional = sessional;
    }
    public int getObtainedmarks() {
        return obtainedmarks;
    }

    public void setObtainedmarks(int obtainedmarks) {
        this.obtainedmarks = obtainedmarks;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public int getPractical() {
        return practical;
    }

    public void setPractical(int practical) {
        this.practical = practical;
    }

    public student getStudent() {
        return student;
    }

    public void setStudent(student student) {
        this.student = student;
    }

}