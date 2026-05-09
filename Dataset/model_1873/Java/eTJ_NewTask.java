





import java.util.List;
import java.util.ArrayList;

public class eTJ_NewTask extends TimesheetAttribute {

    private String text;
    private String id;



    public eTJ_NewTask(
        String text,        String id    ) {
        super(
        );
        this.text = text;
        this.id = id;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}