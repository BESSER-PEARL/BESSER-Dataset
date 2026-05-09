





import java.util.List;
import java.util.ArrayList;

public class eTJ_StatusTimesheet extends TaskTimesheetAttribute, TimesheetAttribute {

    private String text;
    private String level;



    public eTJ_StatusTimesheet(
        String text,        String level    ) {
        super(
        );
        this.text = text;
        this.level = level;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }


}