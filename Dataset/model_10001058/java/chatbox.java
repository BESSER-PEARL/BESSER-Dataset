





import java.util.List;
import java.util.ArrayList;

public class chatbox  {

    private String messagetitle;
    private int messagedcription;
    private String _attr;
    private int messagetype;
    private String class;





    private student student;


    public chatbox(
        String messagetitle,        int messagedcription,        String _attr,        int messagetype,        String class    ) {
        this.messagetitle = messagetitle;
        this.messagedcription = messagedcription;
        this._attr = _attr;
        this.messagetype = messagetype;
        this.class = class;
    }


    public String getMessagetitle() {
        return messagetitle;
    }

    public void setMessagetitle(String messagetitle) {
        this.messagetitle = messagetitle;
    }
    public int getMessagedcription() {
        return messagedcription;
    }

    public void setMessagedcription(int messagedcription) {
        this.messagedcription = messagedcription;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public int getMessagetype() {
        return messagetype;
    }

    public void setMessagetype(int messagetype) {
        this.messagetype = messagetype;
    }
    public String getClass() {
        return class;
    }

    public void setClass(String class) {
        this.class = class;
    }

    public student getStudent() {
        return student;
    }

    public void setStudent(student student) {
        this.student = student;
    }

}