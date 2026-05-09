





import java.util.List;
import java.util.ArrayList;

public class presentation_ToolTip extends Widget {

    private String group;
    private String autoHide;
    private String text;
    private String visible;
    private String message;



    public presentation_ToolTip(
        String group,        String autoHide,        String text,        String visible,        String message    ) {
        super(
        );
        this.group = group;
        this.autoHide = autoHide;
        this.text = text;
        this.visible = visible;
        this.message = message;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getAutohide() {
        return autoHide;
    }

    public void setAutohide(String autoHide) {
        this.autoHide = autoHide;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }


}