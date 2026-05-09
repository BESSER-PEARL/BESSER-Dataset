





import java.util.List;
import java.util.ArrayList;

public class eTJ_StatusStatusSheet extends TaskStatusSheetAttribute {

    private String level;
    private String text;



    public eTJ_StatusStatusSheet(
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