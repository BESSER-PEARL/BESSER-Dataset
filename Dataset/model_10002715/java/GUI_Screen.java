





import java.util.List;
import java.util.ArrayList;

public class GUI_Screen  {

    private String Exit__;
    private int id;
    private String Error__;
    private String Message;
    private int DisplayList__;



    public GUI_Screen(
        String Exit__,        int id,        String Error__,        String Message,        int DisplayList__    ) {
        this.Exit__ = Exit__;
        this.id = id;
        this.Error__ = Error__;
        this.Message = Message;
        this.DisplayList__ = DisplayList__;
    }


    public String getExit__() {
        return Exit__;
    }

    public void setExit__(String Exit__) {
        this.Exit__ = Exit__;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getError__() {
        return Error__;
    }

    public void setError__(String Error__) {
        this.Error__ = Error__;
    }
    public String getMessage() {
        return Message;
    }

    public void setMessage(String Message) {
        this.Message = Message;
    }
    public int getDisplaylist__() {
        return DisplayList__;
    }

    public void setDisplaylist__(int DisplayList__) {
        this.DisplayList__ = DisplayList__;
    }


}