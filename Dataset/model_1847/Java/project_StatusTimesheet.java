





import java.util.List;
import java.util.ArrayList;

public class project_StatusTimesheet extends TimesheetAttribute, TaskTimesheetAttribute {

    private String level;
    private String text;



    public project_StatusTimesheet(
        String level,        String text    ) {
        super(
        );
        this.level = level;
        this.text = text;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}