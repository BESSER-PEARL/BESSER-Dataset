





import java.util.List;
import java.util.ArrayList;

public class project_NewTask extends TimesheetAttribute {

    private String id;
    private String text;



    public project_NewTask(
        String id,        String text    ) {
        super(
        );
        this.id = id;
        this.text = text;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}